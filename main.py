from experiment import run_experiment
from utils import print_experiment_results

# Example corpus and seed
corpus = [
    "quantum computing is a fascinating field",
    "the principles of quantum mechanics are complex",
    "superposition and entanglement are key concepts"
]
seed = ["quantum", "computing"]

# Run the experiment
coherence_score, transformed_coherence_score = run_experiment(corpus, seed)

# Print the results
print_experiment_results(coherence_score, transformed_coherence_score)
