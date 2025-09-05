import requests
import json

def ask_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {"model": "llama3", "prompt": prompt}
    
    res = requests.post(url, json=payload, stream=True)
    output = ""
    for line in res.iter_lines():
        if line:
            try:
                data = json.loads(line.decode("utf-8"))  
                if "response" in data:
                    output += data["response"]
            except json.JSONDecodeError:
                continue 
    return output

if __name__ == "__main__":
    while True:
        q = input("You: ")
        if q.lower() in ["exit", "quit"]:
            break
        ans = ask_ollama(q)
        print("AI:", ans)
