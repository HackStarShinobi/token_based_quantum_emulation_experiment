from ngram_model import train_ngram_model_concept, generate_word_sequence_concept
from embeddings import calculate_sequence_embedding_concept
from similarity import calculate_semantic_coherence_concept
from quantum_simulation import hadamard_gate_simulation_concept

def run_experiment(corpus, seed, sequence_length=10, embedding_dim=100, noise_level=0.1):
    ngram_model = train_ngram_model_concept(corpus)
    generated_sequence = generate_word_sequence_concept(ngram_model, seed, sequence_length)
    coherence_score = calculate_semantic_coherence_concept(generated_sequence, embedding_dim)
    
    sequence_embedding = calculate_sequence_embedding_concept(generated_sequence, embedding_dim)
    transformed_embedding = hadamard_gate_simulation_concept(sequence_embedding, noise_level)
    
    transformed_coherence_score = calculate_semantic_coherence_concept(' '.join(map(str, transformed_embedding)), embedding_dim)
    
    return coherence_score, transformed_coherence_score
