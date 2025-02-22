import numpy as np

def get_word_embedding_concept(word, embedding_dim=100):
    return np.random.rand(embedding_dim)

def calculate_sequence_embedding_concept(sequence, embedding_dim=100):
    words = sequence.split()
    embeddings = [get_word_embedding_concept(word, embedding_dim) for word in words]
    return np.mean(embeddings, axis=0)
