from src.rag_pipeline import pipeline


def main():

    query = input("\nAsk a question: ")

    answer = pipeline(query)

    print("\n" + "=" * 80)
    print("ANSWER")
    print("=" * 80)

    if answer:
        print(answer)
    else:
        print("No answer could be generated.")


if __name__ == "__main__":
    main()