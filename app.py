import os
from dotenv import load_dotenv

import gradio as gr
from groq import Groq

from embed_and_retrieve import retrieve


# ==================================================
# Load Environment Variables
# ==================================================

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL_NAME = "llama-3.3-70b-versatile"


# ==================================================
# Helper Functions
# ==================================================

def build_context(results):
    """
    Combine retrieved chunks into a single context string.
    """

    documents = results["documents"][0]

    return "\n\n".join(documents)


def extract_sources(results):
    """
    Extract unique source names from retrieved metadata.
    Source attribution is programmatically guaranteed.
    """

    sources = []

    for metadata in results["metadatas"][0]:

        source = metadata["source"]

        if source not in sources:
            sources.append(source)

    return sources


# ==================================================
# Generation
# ==================================================

def generate_answer(question, context):
    """
    Generate a grounded answer using only retrieved context.
    """

    system_prompt = """
You are a meal planning and cooking assistant.

Answer the user's question using ONLY the information
contained in the provided context.

Do NOT use outside knowledge.

If the context does not contain enough information
to answer the question, respond exactly:

I don't have enough information on that.
"""

    user_prompt = f"""
CONTEXT:

{context}

QUESTION:

{question}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    return response.choices[0].message.content


# ==================================================
# End-to-End RAG Function
# ==================================================

def ask(question: str):
    """
    Full RAG pipeline:
    Retrieval -> Context Building -> Generation
    """

    results = retrieve(
        query=question,
        top_k=4
    )

    context = build_context(results)

    sources = extract_sources(results)

    answer = generate_answer(
        question,
        context
    )

    return {
        "answer": answer,
        "sources": sources
    }


# ==================================================
# Evaluation Tests
# ==================================================

def run_evaluation():

    evaluation_queries = [

        "What are the basic steps involved in creating a meal plan?",

        "What food safety practices should be followed when preparing meals in advance?",

        "What advice is given to beginners who want to learn how to cook?",

        "What are the best restaurants in New York City?"
    ]

    print("\n" + "=" * 80)
    print("RUNNING EVALUATION")
    print("=" * 80)

    for query in evaluation_queries:

        result = ask(query)

        print("\nQUESTION:")
        print(query)

        print("\nANSWER:")
        print(result["answer"])

        print("\nSOURCES:")
        for source in result["sources"]:
            print("-", source)

        print("\n" + "-" * 80)


# ==================================================
# Gradio Interface
# ==================================================

def handle_query(question):

    result = ask(question)

    source_text = "\n".join(
        f"• {source}"
        for source in result["sources"]
    )

    return (
        result["answer"],
        source_text
    )


with gr.Blocks() as demo:

    gr.Markdown(
        "# Meal Planning RAG Assistant"
    )

    gr.Markdown(
        "Ask questions about meal planning, nutrition, cooking skills, food safety, and meal prep."
    )

    question_box = gr.Textbox(
        label="Your Question",
        placeholder="Example: What should a balanced meal consist of?"
    )

    ask_button = gr.Button("Ask")

    answer_box = gr.Textbox(
        label="Answer",
        lines=8
    )

    sources_box = gr.Textbox(
        label="Sources",
        lines=5
    )

    ask_button.click(
        handle_query,
        inputs=question_box,
        outputs=[answer_box, sources_box]
    )

    question_box.submit(
        handle_query,
        inputs=question_box,
        outputs=[answer_box, sources_box]
    )


# ==================================================
# Main
# ==================================================

if __name__ == "__main__":

    run_evaluation()

    demo.launch()
