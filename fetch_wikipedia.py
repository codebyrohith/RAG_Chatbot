# fetch_wikipedia.py
from datasets import load_dataset
import json
import os

# Ensure the "data" directory exists
os.makedirs("data", exist_ok=True)

# Load Wikipedia dataset (first 1000 articles)
print("📥 Fetching Wikipedia data...")
dataset = load_dataset("wikipedia", "20220301.simple", split="train[:1000]", trust_remote_code=True)
texts = dataset["text"][:1000]  # Get first 1000 articles

# Save dataset to JSON file
data_path = "data/wikipedia_sample.json"
with open(data_path, "w") as f:
    json.dump(texts, f)

print(f"✅ Wikipedia dataset saved successfully to {data_path}!")
