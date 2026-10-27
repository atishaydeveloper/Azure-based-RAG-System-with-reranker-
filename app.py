# App UI with Gradio
from azure.search.documents.indexes import SearchIndexClient
from azure.core.credentials import AzureKeyCredential
from end_to_end import graph
from dotenv import load_dotenv
import os

import gradio as gr

load_dotenv()

search_endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
admin_key = os.getenv("AZURE_SEARCH_ADMIN_KEY")

client = SearchIndexClient(
    endpoint=search_endpoint,
    credential=AzureKeyCredential(admin_key)
)

def get_existing_indexes():
    indexes = client.list_indexes()

    return [
        index.name
        for index in indexes
    ]


def run_rag(mode, pdf_file, existing_index, question):

    if not question or not question.strip():
        return "Please enter a question.", ""

    # -----------------------------
    # New PDF
    # -----------------------------

    if mode == "New PDF":

        if pdf_file is None:
            return "Please upload a PDF first.", ""

        state = {
            "index_chosen": "new",
            "file_path": pdf_file,
            "query": question,
        }

    # -----------------------------
    # Existing PDF
    # -----------------------------

    else:

        if not existing_index:
            return "Please select an existing document.", ""

        state = {
            "index_chosen": "existing",
            "index_name": existing_index,
            "query": question,
        }

    try:

        final_state = graph.invoke(state)

        answer = final_state.get(
            "answer",
            "No answer was generated."
        )

        retrieved_chunks = final_state.get(
            "retrieved_chunks",
            ""
        )

        return answer, retrieved_chunks

    except Exception as e:

        return (
            f"Error while running RAG pipeline:\n\n{str(e)}",
            ""
        )


# ---------------------------------------------------------
# Refresh existing indexes
# ---------------------------------------------------------

def refresh_indexes():
    indexes = get_existing_indexes()

    return gr.update(
        choices=indexes,
        value=indexes[0] if indexes else None
    )


# ---------------------------------------------------------
# UI
# ---------------------------------------------------------

with gr.Blocks(
    title="PDF RAG Assistant"
) as demo:

    gr.Markdown(
        """
        # PDF RAG Assistant

        Ask questions about your PDF documents using
        **Azure AI Search + Vector Search + LangGraph**.
        """
    )

    # -----------------------------------------------------
    # Document selection
    # -----------------------------------------------------

    gr.Markdown("## 1. Select Document")

    mode = gr.Radio(
        choices=[
            "New PDF",
            "Existing PDF"
        ],
        value="New PDF",
        label="Document source"
    )

    # New PDF section

    with gr.Group() as new_pdf_group:

        pdf_file = gr.File(
            label="Upload PDF",
            file_types=[".pdf"],
            type="filepath"
        )

    # Existing PDF section

    with gr.Group(visible=False) as existing_group:

        existing_index = gr.Dropdown(
            label="Select Existing Document",
            choices=get_existing_indexes(),
            interactive=True
        )

        refresh_button = gr.Button(
            "Refresh Documents"
        )

    # -----------------------------------------------------
    # Question
    # -----------------------------------------------------

    gr.Markdown("## 2. Ask a Question")

    question = gr.Textbox(
        label="Question",
        placeholder="What is this document about?",
        lines=3
    )

    ask_button = gr.Button(
        "Ask",
        variant="primary"
    )

    # -----------------------------------------------------
    # Answer
    # -----------------------------------------------------

    gr.Markdown("## 3. Answer")

    answer = gr.Markdown(
        label="Answer"
    )

    # -----------------------------------------------------
    # Retrieved chunks
    # -----------------------------------------------------

    with gr.Accordion(
        "Retrieved Sources",
        open=False
    ):

        sources = gr.Textbox(
            label="Retrieved Chunks",
            lines=15,
            interactive=False
        )

    # -----------------------------------------------------
    # UI interactions
    # -----------------------------------------------------

    def toggle_source(mode):

        if mode == "New PDF":

            return (
                gr.update(visible=True),
                gr.update(visible=False)
            )

        else:

            return (
                gr.update(visible=False),
                gr.update(visible=True)
            )

    mode.change(
        fn=toggle_source,
        inputs=mode,
        outputs=[
            new_pdf_group,
            existing_group
        ]
    )

    refresh_button.click(
        fn=refresh_indexes,
        inputs=None,
        outputs=existing_index
    )

    ask_button.click(
        fn=run_rag,
        inputs=[
            mode,
            pdf_file,
            existing_index,
            question
        ],
        outputs=[
            answer,
            sources
        ]
    )


# ---------------------------------------------------------
# Launch
# ---------------------------------------------------------

if __name__ == "__main__":
    demo.launch()