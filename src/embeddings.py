from sentence_transformers import SentenceTransformer

# Load model only once
model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embedding(text):
    return model.encode(
        text,
        normalize_embeddings=True
    )


def get_embeddings(texts):
    return model.encode(
        texts,
        batch_size=64,
        normalize_embeddings=True,
        show_progress_bar=True
    )