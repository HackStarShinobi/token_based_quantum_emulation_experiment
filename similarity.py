import numpy as np

def cosine_similarity_concept(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    return dot_product / (norm_vec1 * norm_vec2)

def calculate_semantic_coherence_concept(sequence, embedding_dim=100):
    sequence_embedding = calculate_sequence_embedding_concept(sequence, embedding_dim)
    words = sequence.split()
    coherence_scores = []
    for word in words:
        word_embedding = get_word_embedding_concept(word, embedding_dim)
        coherence_score = cosine_similarity_concept(word_embedding, sequence_embedding)
        coherence_scores.append(coherence_score)
    return np.mean(coherence_scores)
