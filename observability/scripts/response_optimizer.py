import json

def suggest_optimizations(log_file):
    with open(log_file, 'r') as f:
        logs = json.load(f)

    for log in logs:
        if log['success'] is False:
            print(f"Prompt: {log['prompt']} in category {log['category']} needs optimization")
            print("Suggestions:")
            print("- Simplify the prompt for clarity.")
            print("- Adjust model parameters like temperature or max_tokens.")
            print("- Explore alternative models for better results.\n")

if __name__ == "__main__":
    log_file = "logs.json"
    suggest_optimizations(log_file)
