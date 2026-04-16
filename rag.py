from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def build_collection(sources: dict):
    chunks = []
    metadata = []
    
    for source_name, text in sources.items():
        step = 450
        size = 500
        for i in range(0, len(text), step):
            chunk = text[i:i+size]
            if len(chunk) > 100:
                chunks.append(chunk)
                metadata.append(source_name)
    
    return chunks, metadata

def retrieve(collection, topic: str, n=6):
    chunks, metadata = collection
    
    if not chunks:
        return ""
    
    vectorizer = TfidfVectorizer()
    all_texts = [topic] + chunks
    matrix = vectorizer.fit_transform(all_texts)
    
    scores = cosine_similarity(matrix[0:1], matrix[1:]).flatten()
    top_indices = scores.argsort()[-n:][::-1]
    
    output = ""
    for i in top_indices:
        output += f"\n\n--- FROM: {metadata[i]} ---\n{chunks[i]}"
    
    return output