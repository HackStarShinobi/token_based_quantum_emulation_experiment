import random
from collections import defaultdict

def train_ngram_model_concept(corpus, n=2):
    model = defaultdict(lambda: defaultdict(int))
    for sentence in corpus:
        tokens = sentence.split()
        for i in range(len(tokens) - n):
            ngram = tuple(tokens[i:i + n])
            next_token = tokens[i + n]
            model[ngram][next_token] += 1
    return model

def generate_word_sequence_concept(model, seed, length=10):
    sequence = list(seed)
    for _ in range(length):
        ngram = tuple(sequence[-len(seed):])
        next_token_candidates = list(model[ngram].keys())
        if not next_token_candidates:
            break
        next_token = random.choice(next_token_candidates)
        sequence.append(next_token)
    return ' '.join(sequence)
