import os
from app.memory import MemoryDB
from openai import OpenAI

def get_sonar_output(prompt):

    # Set up the OpenAI client for Perplexity Sonar
    api_key = os.getenv("PERPLEXITY_API_KEY")
    if not api_key:
        raise ValueError("PERPLEXITY_API_KEY environment variable not set.")
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.perplexity.ai"
    )
    response = client.chat.completions.create(
        model="sonar-pro",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def main():
    memory = MemoryDB()

    while True:
        action = input("\nChoose action: [store/retrieve/search/list/delete/exit]: ").strip().lower()
        if action == "store":
            prompt = input("Prompt: ")
            print("Querying Sonar-Pro for output...")
            try:
                output = get_sonar_output(prompt)
                print(f"Sonar-Pro Output: {output}")
                memory.store(prompt, output)
                print("Stored.")
            except Exception as e:
                print(f"Error querying Sonar-Pro: {e}")

        elif action == "retrieve":
            prompt = input("Prompt to retrieve: ")
            output = memory.retrieve(prompt)
            print(f"Output: {output}")

        elif action == "search":
            keyword = input("Keyword to search: ")
            results = memory.search(keyword)
            for k, v in results:
                print(f"Prompt: {k} | Output: {v}")

        elif action == "list":
            for k, v in memory.all_memories():
                print(f"Prompt: {k} | Output: {v}")

        elif action == "delete":
            prompt = input("Prompt to delete: ")
            memory.delete(prompt)
            print("Deleted (if existed).")

        elif action == "exit":
            memory.close()
            break

        else:
            print("Unknown action.")

if __name__ == "__main__":
    main()
