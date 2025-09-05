def get_embedding(text:str, model:str="llama3") -> list[float]:
    import requests
    import json

    url = "http://localhost:11434/api/embeddings"
    payload = {"model": model, "input": text}
    
    res = requests.post(url, json=payload)
    if res.status_code != 200:
        raise Exception(f"Request failed with status code {res.status_code}: {res.text}")
    
    data = res.json()
    if "embedding" not in data:
        raise Exception(f"Unexpected response format: {data}")
    
    return data["embedding"]
# src/embeddings/ollama_embd.py