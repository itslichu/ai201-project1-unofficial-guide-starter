import json
import chromadb
from sentence_transformers import SentenceTransformer


# --------------------------------------------------
# Load embedding model
# --------------------------------------------------
# This model converts text into vectors (embeddings)
# that capture semantic meaning.
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_collection():
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_collection(name="meal_planning_rag")
    return collection

# --------------------------------------------------
# Load chunks from chunks.json
# --------------------------------------------------
def load_chunks(file_path="chunks.json"):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


# --------------------------------------------------
# Create ChromaDB collection
# --------------------------------------------------
def create_collection():
    client = chromadb.PersistentClient(path="./chroma_db")

    # Delete existing collection if it exists
    try:
        client.delete_collection("meal_planning_rag")
    except Exception:
        pass

    collection = client.create_collection(
        name="meal_planning_rag"
    )

    return collection


# --------------------------------------------------
# Embed and store chunks
# --------------------------------------------------
def embed_and_store(chunks, collection):
    """
    Generate embeddings for all chunks and store
    them in ChromaDB.
    """

    documents = []
    embeddings = []
    ids = []
    metadatas = []

    for idx, chunk in enumerate(chunks):

        text = chunk["text"]

        metadata = {
            "source": chunk["metadata"]["source"],
            "title": chunk["metadata"]["title"],
            "chunk_index": idx
        }

        # Convert text into vector embedding
        embedding = model.encode(text).tolist()

        documents.append(text)
        embeddings.append(embedding)
        ids.append(str(idx))
        metadatas.append(metadata)

    # Insert documents, embeddings, and metadata
    # into ChromaDB
    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )

    print(f"Stored {len(documents)} chunks in ChromaDB.")


# --------------------------------------------------
# Retrieval Function
# --------------------------------------------------
def retrieve(query: str, top_k: int = 4):
    """
    Retrieve the most relevant chunks for a query.
    """

    collection = get_collection()
    # Embed the user query
    query_embedding = model.encode(query).tolist()

    # Similarity search
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results


# --------------------------------------------------
# Pretty-print retrieval results
# --------------------------------------------------
def print_results(query, results):
    print("\n" + "=" * 80)
    print("QUERY:")
    print(query)
    print("=" * 80)

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    for i in range(len(documents)):
        print(f"\nResult #{i+1}")
        print(f"Source: {metadatas[i]['source']}")
        print(f"Title: {metadatas[i]['title']}")
        print(f"Chunk Position: {metadatas[i]['chunk_index']}")
        print(f"Distance Score: {distances[i]:.4f}")

        print("\nChunk Text:")
        print("-" * 40)
        print(documents[i][:700])

        if len(documents[i]) > 700:
            print("...")

        print("-" * 40)


# --------------------------------------------------
# Main
# --------------------------------------------------
def main():

    print("Loading chunks...")
    chunks = load_chunks()

    print("Creating ChromaDB collection...")
    collection = create_collection()

    print("Embedding and storing chunks...")
    embed_and_store(chunks, collection)

    # --------------------------------------------
    # Evaluation Queries
    # --------------------------------------------
    evaluation_queries = [
        "What are the basic steps involved in creating a meal plan?",
        "What food safety practices should be followed when preparing meals in advance?",
        "What advice is given to beginners who want to learn how to cook?"
    ]

    for query in evaluation_queries:
        results = retrieve(
            query=query,
            collection=collection,
            top_k=4
        )

        print_results(query, results)


if __name__ == "__main__":
    main()
