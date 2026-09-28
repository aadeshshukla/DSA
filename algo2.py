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

import torch
import torch.nn.functional as F

def scaled_dot_product_attention(q, k, v, mask=None):
    d_k = q.size(-1)
    # Compute attention scores: (batch, seq_len, seq_len)
    scores = torch.matmul(q, k.transpose(-2, -1)) / (d_k ** 0.5)
    
    if mask is not None:
        scores = scores.masked_fill(mask == 0, float("-inf"))
        
    weights = F.softmax(scores, dim=-1)
    output = torch.matmul(weights, v)
    return output, weights

# Example: (batch=1, tokens=3, embed_dim=4)
torch.manual_seed(42)
Q = torch.randn(1, 3, 4)
K = torch.randn(1, 3, 4)
V = torch.randn(1, 3, 4)

output, weights = scaled_dot_product_attention(Q, K, V)
print("Attention Output Shape:", output.shape)
print("Attention Weights:\n", weights)
