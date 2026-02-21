# Simple ML Data Preprocessing Example

# Sample data
data = {
    "names": ["Alice", "Bob", "Charlie"],
    "ages": [25, 30, 22],
    "scores": [85.5, 92.0, 78.5]
}

# Normalize scores (0-1 range)
min_score = min(data["scores"])
max_score = max(data["scores"])

normalized_scores = [
    (score - min_score) / (max_score - min_score) 
    for score in data["scores"]
]

print("Original scores:", data["scores"])
print("Normalized scores:", normalized_scores)

# Feature scaling using z-score
import statistics
mean = statistics.mean(data["ages"])
std = statistics.stdev(data["ages"])

z_scores = [(age - mean) / std for age in data["ages"]]
print("Z-scores for ages:", z_scores)

# Create labeled dataset
dataset = []
for i in range(len(data["names"])):
    dataset.append({
        "name": data["names"][i],
        "age": data["ages"][i],
        "score": normalized_scores[i],
        "label": "high" if normalized_scores[i] > 0.5 else "low"
    })

for record in dataset:
    print(record)
