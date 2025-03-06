from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import os

# Ensure model directory exists for local loading
os.makedirs("models", exist_ok=True)

# Try loading from local directory first, else download
try:
    tokenizer = AutoTokenizer.from_pretrained("models/t5-small")
    model = AutoModelForSeq2SeqLM.from_pretrained("models/t5-small")
    print("✅ Loaded T5 model from local storage.")
except:
    print("⚠️ Downloading T5 model from Hugging Face...")
    tokenizer = AutoTokenizer.from_pretrained("t5-small")
    model = AutoModelForSeq2SeqLM.from_pretrained("t5-small")

def generate_answer(query, context):
    """Generate an answer using the T5 model."""
    input_text = f"question: {query}  context: {context}"
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    output_ids = model.generate(input_ids)
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)
