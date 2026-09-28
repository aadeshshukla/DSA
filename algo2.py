import numpy as np

def cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> float:
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    
    if norm_v1 == 0 or norm_v2 == 0:
        return 0.0
    return float(dot_product / (norm_v1 * norm_v2))

# Example usage:
vec_a = np.array([0.15, 0.82, -0.34, 0.55])
vec_b = np.array([0.18, 0.79, -0.31, 0.50])
print("Similarity Score:", round(cosine_similarity(vec_a, vec_b), 4))
