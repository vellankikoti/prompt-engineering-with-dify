import json

def suggest_optimizations(log_file):
    with open(log_file, 'r') as f:
        logs = json.load(f)

    for log in logs:
        if log['success'] is False:
            print(f"Prompt: {log['prompt']} needs optimization")
            print("Suggestions:")
            print("- Try simplifying the prompt.")
            print("- Adjust model parameters like temperature or max_tokens.")
            print("- Consider using a different model.\n")

if __name__ == "__main__":
    log_file = "logs.json"
    suggest_optimizations(log_file)
