from src.embeddings.ollama_embd import get_embedding
from src.embeddings.similarity import cosine_similarity

e1 = get_embedding("Banana")
e2 = get_embedding("Apple")
e3 = get_embedding("Car")

print("Banana embedding sample:", e1[:10])
print("Apple embedding sample:", e2[:10])
print("Car embedding sample:", e3[:10])

print("Similarity between 'Banana' and 'Apple':", cosine_similarity(e1, e2))
print("Similarity between 'Banana' and 'Car':", cosine_similarity(e1, e3))
