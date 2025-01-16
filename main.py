import random
from collections import defaultdict


def read_corpus(file_path):
    """Reads text from a file and returns it as a string."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def build_transition_table(corpus, n=1):
    """Builds an n-gram Markov chain transition table from the given corpus."""
    words = corpus.split()
    transitions = defaultdict(list)
    for i in range(len(words) - n):
        state = tuple(words[i : i + n])
        next_word = words[i + n]
        transitions[state].append(next_word)
    return transitions


def generate_text(transition_table, start_state, length=50):
    """Generates text using the given transition table and start state."""
    state = start_state
    result = list(state)
    for _ in range(length):
        next_words = transition_table.get(state)
        if not next_words:
            break
        next_word = random.choice(next_words)
        result.append(next_word)
        state = tuple(result[-len(state) :])
    return " ".join(result)


# File paths for the corpora
file1 = "corpus1.txt"
file2 = "corpus2.txt"

# Read and combine corpora
corpus1 = read_corpus(file1)
corpus2 = read_corpus(file2)
combined_corpus = corpus1 + " " + corpus2

# Build transition table
n = 2  # Use bigrams (2-grams) for the Markov chain
transition_table = build_transition_table(combined_corpus, n)

# Generate text
start_state = random.choice(list(transition_table.keys()))
generated_text = generate_text(transition_table, start_state, length=100)

print("Generated Text:")
print(generated_text)
