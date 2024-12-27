import json
from collections import defaultdict

def analyze_logs(log_file):
    with open(log_file, 'r') as f:
        logs = json.load(f)

    category_summary = defaultdict(list)

    for log in logs:
        category = log.get('category', 'Uncategorized')
        category_summary[category].append(log)

    for category, entries in category_summary.items():
        print(f"Category: {category}")
        for log in entries:
            print(f"Prompt: {log['prompt']}")
            print(f"Model: {log['model']}")
            print(f"Response Time: {log['response_time']} ms")
            print(f"Success: {log['success']}\n")

if __name__ == "__main__":
    log_file = "logs.json"  # Replace with your actual log file
    analyze_logs(log_file)
