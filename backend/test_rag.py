from rag import answer_question

if __name__ == "__main__":
    question = "Why should we hire her?"
    answer = answer_question(question)
    print("\nANSWER:\n")
    print(answer)
