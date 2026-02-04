import sys
import math
import time
import json
from typing import List, Tuple

from pydantic import BaseModel, Field
from dotenv import load_dotenv
from litellm import completion, RateLimitError

from evaluation.test import TestQuestion, load_tests
from implementation.answer import answer_question, fetch_context

# ============================================================
# ENV
# ============================================================
load_dotenv(override=True)

# LiteLLM requires provider prefix
JUDGE_MODEL = "groq/llama-3.1-8b-instant"

# ============================================================
# DATA MODELS
# ============================================================
class RetrievalEval(BaseModel):
    mrr: float
    ndcg: float
    keywords_found: int
    total_keywords: int
    keyword_coverage: float


class AnswerEval(BaseModel):
    feedback: str
    accuracy: float
    completeness: float
    relevance: float


# ============================================================
# SAFE GROQ CALL (GLOBAL)
# ============================================================
def safe_completion(
    *,
    model: str,
    messages: list,
    temperature: float = 0,
    base_sleep: int = 8,
    max_retries: int = 10,
):
    """
    Safe LiteLLM completion wrapper for Groq with global throttling.
    """
    retries = 0
    while True:
        try:
            response = completion(
                model=model,
                messages=messages,
                temperature=temperature,
            )
            # global throttle AFTER success
            time.sleep(base_sleep)
            return response

        except RateLimitError as e:
            retries += 1
            if retries > max_retries:
                raise e
            wait = base_sleep + retries * 2
            print(f"[RateLimit] sleeping {wait}s (retry {retries})")
            time.sleep(wait)


# ============================================================
# RETRIEVAL METRICS
# ============================================================
def calculate_mrr(keyword: str, retrieved_docs: list) -> float:
    keyword = keyword.lower()
    for rank, doc in enumerate(retrieved_docs, start=1):
        if keyword in doc.page_content.lower():
            return 1.0 / rank
    return 0.0


def calculate_dcg(relevances: List[int], k: int) -> float:
    dcg = 0.0
    for i in range(min(k, len(relevances))):
        dcg += relevances[i] / math.log2(i + 2)
    return dcg


def calculate_ndcg(keyword: str, retrieved_docs: list, k: int = 10) -> float:
    keyword = keyword.lower()
    relevances = [
        1 if keyword in doc.page_content.lower() else 0
        for doc in retrieved_docs[:k]
    ]
    dcg = calculate_dcg(relevances, k)
    idcg = calculate_dcg(sorted(relevances, reverse=True), k)
    return dcg / idcg if idcg > 0 else 0.0


def evaluate_retrieval(test: TestQuestion) -> RetrievalEval:
    retrieved_docs = fetch_context(test.question)

    mrrs = [calculate_mrr(k, retrieved_docs) for k in test.keywords]
    ndcgs = [calculate_ndcg(k, retrieved_docs) for k in test.keywords]

    keywords_found = sum(1 for m in mrrs if m > 0)

    return RetrievalEval(
        mrr=sum(mrrs) / len(mrrs) if mrrs else 0.0,
        ndcg=sum(ndcgs) / len(ndcgs) if ndcgs else 0.0,
        keywords_found=keywords_found,
        total_keywords=len(test.keywords),
        keyword_coverage=(keywords_found / len(test.keywords) * 100)
        if test.keywords else 0.0,
    )


# ============================================================
# ANSWER EVALUATION
# ============================================================
def evaluate_answer(test: TestQuestion) -> Tuple[AnswerEval, str, list]:
    # 1. Generate RAG answer (THIS already calls Groq once)
    generated_answer, retrieved_docs = answer_question(test.question)

    # 2. Judge prompt
    judge_messages = [
        {
            "role": "system",
            "content": (
                "You are an expert evaluator. Respond ONLY in valid JSON.\n"
                "{\n"
                '  "feedback": string,\n'
                '  "accuracy": number (1-5),\n'
                '  "completeness": number (1-5),\n'
                '  "relevance": number (1-5)\n'
                "}\n"
                "No extra text."
            ),
        },
        {
            "role": "user",
            "content": f"""
Question:
{test.question}

Generated Answer:
{generated_answer}

Reference Answer:
{test.reference_answer}
""",
        },
    ]

    # 3. SAFE judge call (Groq via LiteLLM)
    judge_response = safe_completion(
        model=JUDGE_MODEL,
        messages=judge_messages,
        temperature=0,
    )

    # 4. Parse JSON
    raw = judge_response.choices[0].message.content
    parsed = json.loads(raw)
    answer_eval = AnswerEval.model_validate(parsed)

    return answer_eval, generated_answer, retrieved_docs


# ============================================================
# RUNNERS
# ============================================================
def evaluate_all_retrieval():
    tests = load_tests()
    for i, test in enumerate(tests):
        yield test, evaluate_retrieval(test), (i + 1) / len(tests)


def evaluate_all_answers():
    tests = load_tests()
    for i, test in enumerate(tests):
        result = evaluate_answer(test)[0]
        yield test, result, (i + 1) / len(tests)


def run_cli_evaluation(test_number: int):
    tests = load_tests()

    test = tests[test_number]

    print("=" * 80)
    print("QUESTION:", test.question)
    print("KEYWORDS:", test.keywords)
    print("=" * 80)

    r = evaluate_retrieval(test)
    print("MRR:", r.mrr)
    print("nDCG:", r.ndcg)
    print("Coverage:", r.keyword_coverage)

    a, ans, _ = evaluate_answer(test)
    print("\nANSWER:", ans)
    print("\nFEEDBACK:", a.feedback)
    print("Scores:", a.accuracy, a.completeness, a.relevance)


def main():
    if len(sys.argv) != 2:
        print("Usage: python eval.py <test_index>")
        sys.exit(1)

    run_cli_evaluation(int(sys.argv[1]))


if __name__ == "__main__":
    main()
