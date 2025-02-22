import numpy as np

def hadamard_gate_simulation_concept(sequence_embedding, noise_level=0.1):
    noise = np.random.normal(0, noise_level, size=sequence_embedding.shape)
    return sequence_embedding + noise
