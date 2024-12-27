import json

def analyze_logs(log_file):
    with open(log_file, 'r') as f:
        logs = json.load(f)
    
    for log in logs:
        print(f"Prompt: {log['prompt']}")
        print(f"Model: {log['model']}")
        print(f"Response Time: {log['response_time']} ms")
        print(f"Success: {log['success']}\n")

if __name__ == "__main__":
    log_file = "logs.json"  # Replace with your actual log file
    analyze_logs(log_file)
