import os
import re
import json
from pathlib import Path

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


# -----------------------------
# Text Cleaning
# -----------------------------
def clean_text(text: str) -> str:
    """
    Clean document text by:
    - removing extra whitespace
    - collapsing multiple newlines
    - trimming leading/trailing spaces
    """
    text = re.sub(r"\r\n?", "\n", text)
    text = re.sub(r"\n\s*\n+", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)

    return text.strip()


# -----------------------------
# Document Loading
# -----------------------------
def load_documents(directory: str = "documents"):
    """
    Load all .txt files from the specified directory
    and create LangChain Document objects.
    """
    documents = []

    directory_path = Path(directory)

    if not directory_path.exists():
        raise FileNotFoundError(
            f"Directory '{directory}' not found."
        )

    for file_path in directory_path.glob("*.txt"):
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            raw_text = f.read()

        cleaned_text = clean_text(raw_text)

        document = Document(
            page_content=cleaned_text,
            metadata={
                "source": file_path.name,
                "title": file_path.stem
            }
        )

        documents.append(document)

    return documents


# -----------------------------
# Chunking
# -----------------------------
def chunk_documents(documents):
    """
    Split documents using RecursiveCharacterTextSplitter.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    return chunks


# -----------------------------
# Save Chunks
# -----------------------------
def save_chunks(chunks, output_file="chunks.json"):
    """
    Save chunks to JSON format.
    """

    output = []

    for chunk in chunks:
        output.append({
            "text": chunk.page_content,
            "metadata": {
                "source": chunk.metadata.get("source", ""),
                "title": chunk.metadata.get("title", "")
            }
        })

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)


# -----------------------------
# Statistics
# -----------------------------
def print_stats(documents, chunks):
    """
    Print summary statistics.
    """

    avg_chunk_length = (
        sum(len(chunk.page_content) for chunk in chunks)
        / len(chunks)
        if chunks
        else 0
    )

    print("\n=== INGESTION SUMMARY ===")
    print(f"Documents loaded: {len(documents)}")
    print(f"Total chunks created: {len(chunks)}")
    print(f"Average chunk length: {avg_chunk_length:.2f} characters")


# -----------------------------
# Main Pipeline
# -----------------------------
def main():
    print("Loading documents...")

    documents = load_documents("documents")

    print("Chunking documents...")

    chunks = chunk_documents(documents)

    print("Saving chunks...")

    save_chunks(chunks, "chunks.json")

    print_stats(documents, chunks)

    print("\nChunks saved to chunks.json")

    print("\n===== SAMPLE CHUNKS =====")

    seen_sources = set()
    sample_count = 0

    for chunk in chunks:

        source = chunk.metadata["source"]

        if source in seen_sources:
            continue

        seen_sources.add(source)
        sample_count += 1

        print(f"\nChunk {sample_count}")
        print(f"Source: {source}")
        print(f"Length: {len(chunk.page_content)} chars")
        print("-" * 50)
        print(chunk.page_content[:300])

        if len(chunk.page_content) > 300:
            print("...")

        if sample_count == 5:
            break

if __name__ == "__main__":
    main()
