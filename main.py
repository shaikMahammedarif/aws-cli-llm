from llm_client import get_aws_command
from aws_command_executor import execute_aws_command

def main():
    print("🔷 Welcome to AWS LLM Helper (Powered by Gemini)")
    while True:
        query = input("🧠 Enter your AWS request (or 'exit'): ")
        if query.lower() in ['exit', 'quit']:
            break

        aws_command = get_aws_command(query)
        print(f"✅ Gemini Generated:\n{aws_command}\n")

        result = execute_aws_command(aws_command)
        print(f"📦 Output:\n{result}\n")

if __name__ == "__main__":
    main()
