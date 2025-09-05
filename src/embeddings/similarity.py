import numpy as np

def cosine_similarity(vec_1:list,vec_2:list)->float:

    """Compute the cosine similarity between two vectors."""

    v1 = np.array(vec_1)
    v2 = np.array(vec_2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    
    if norm_v1 == 0 or norm_v2 == 0:
        return 0

    return np.dot(v1, v2) / (norm_v1 * norm_v2)