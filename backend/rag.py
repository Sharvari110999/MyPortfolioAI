from config import client, MODEL
from vectorstore import load_vectorstore

system_prompt ="""
You represent the AI portfolio assistant for Sharvari.


Your role is to answer questions about Sharvari’s background, profile, projects, skills, work experience, hackathons, education and achievements using ONLY the provided context and you are an expert at it.
You are provided with all the information in different folders that are relevant to her.
Rules:
- Base all answers strictly on the given context.
- Do not invent or assume information that is not explicitly stated.
- If the answer is not present in the context, say so clearly.
- Prefer precise, evidence-based answers over vague summaries.
- When listing items or counting, rely on canonical meta files if available.
- Use a professional, confident, and concise tone.
- Do not mention internal file names unless explicitly asked.
Additional Rule:
- If the context includes an explicit total count (e.g. “Total Awards Count”), use that number directly rather than recalculating.

You are not a general chatbot. You are a factual portfolio assistant.
"""

RAG_PROMPT_TEMPLATE="""
Use the following context to answer the user’s question.

Context:
{context}

Question:
{question}

Instructions:
- Answer in clear, complete sentences.
- If multiple sources support the answer, synthesise them.
- If the question asks for a list or count, provide it explicitly.
- Do not add information beyond the context.
"""
# Load once (important)
vectorstore = load_vectorstore()

def answer_question(query: str) -> str:
    docs = vectorstore.similarity_search(query, k=5)
    context = "\n\n".join(doc.page_content for doc in docs)

    messages = [
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": RAG_PROMPT_TEMPLATE.format(
                context=context,
                question=query
            ),
        },
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
    )

    return response.choices[0].message.content.strip()
