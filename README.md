# Azure-Powered PDF RAG Pipeline with LangGraph

An end-to-end Retrieval-Augmented Generation (RAG) application that integrates Azure cloud services, LangGraph orchestration, and a Gradio interface to process PDF documents and generate context-aware answers.

The project explores how individual AI and cloud components can be integrated into a structured, production-oriented application rather than a standalone RAG experiment.

## Overview

Retrieval-Augmented Generation (RAG) combines information retrieval with large language models (LLMs), allowing responses to be generated using relevant information retrieved from external documents.

This project implements a PDF-based RAG pipeline using Microsoft Azure services and LangGraph. It supports document storage, vector indexing, retrieval, and answer generation through a user-facing interface.

A key design decision is the use of **conditional routing and state management in LangGraph** to control the workflow based on whether a vector index needs to be created or an existing index can be reused.

## Architecture

The application integrates the following components:

| Component          | Responsibility                                                                                |
| ------------------ | --------------------------------------------------------------------------------------------- |
| Azure Blob Storage | Stores PDF documents used as the knowledge source.                                            |
| Azure AI Search    | Indexes document content and provides search and retrieval capabilities.                      |
| Azure AI Foundry   | Provides access to LLM capabilities for answer generation.                                    |
| LangGraph          | Orchestrates workflow execution through graph-based state management and conditional routing. |
| Gradio             | Provides a user interface for interacting with the RAG application.                           |

### High-Level Workflow

```text
                PDF Documents
                      |
                      v
              Azure Blob Storage
                      |
                      v
           Document Processing
                      |
                      v
             Azure AI Search
                      |
              Index Management
                      |
             +--------+--------+
             |                 |
             v                 v
       Create Index       Reuse Index
             |                 |
             +--------+--------+
                      |
                      v
             Document Retrieval
                      |
                      v
              LangGraph Workflow
                      |
                      v
              Azure AI Foundry
                      |
                      v
             Generated Response
                      |
                      v
                Gradio UI
```

*Note: This diagram represents the conceptual workflow. The exact execution sequence depends on the application's graph configuration.*

## Key Features

### 1. PDF-Based Knowledge Retrieval

Uses PDF documents stored in Azure Blob Storage as the source of information for retrieval-augmented responses.

### 2. Azure AI Search Integration

Integrates Azure AI Search to support document indexing and retrieval, enabling the application to find relevant information before generating a response.

### 3. Conditional Workflow Routing

Uses LangGraph to implement conditional execution paths based on index availability and workflow requirements.

This approach provides more control over application execution than a simple, linear RAG chain.

### 4. Stateful Orchestration

Uses LangGraph's graph-based workflow model to organize processing steps and manage the state required for execution.

### 5. LLM-Powered Answer Generation

Uses Azure AI Foundry to access language model capabilities and generate responses based on retrieved document context.

### 6. Interactive User Interface

Provides a Gradio interface through which users can interact with the RAG application.

## Technology Stack

* **Programming Language:** Python
* **Cloud Platform:** Microsoft Azure
* **Document Storage:** Azure Blob Storage
* **Search and Retrieval:** Azure AI Search
* **LLM Services:** Azure AI Foundry
* **Workflow Orchestration:** LangGraph
* **User Interface:** Gradio

## Project Objectives

The primary objective was to understand how cloud infrastructure, retrieval systems, LLMs, and workflow orchestration fit together within an AI application.

The project focused on:

* Integrating multiple Azure services into a single application.
* Understanding the document ingestion and indexing workflow.
* Connecting retrieval results to LLM-based answer generation.
* Implementing conditional routing with LangGraph.
* Managing workflow execution through graph-based orchestration.
* Building an interactive interface for application usage.
* Applying concepts learned through Microsoft Azure AI Fundamentals (AI-901) to a practical implementation.

## Getting Started

### Prerequisites

Before running the application, ensure you have:

* Python installed.
* An Azure subscription with the required resources configured.
* An Azure Blob Storage account containing the source PDF documents.
* An Azure AI Search service and the required index configuration.
* Access to an Azure AI Foundry model deployment.
* Appropriate Azure credentials and permissions.
* The Python dependencies required by the project.

### Installation

Clone the repository:

```bash
git clone <repository-url>
cd <repository-directory>
```

Create and activate a virtual environment:

**Windows**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

**Linux/macOS**

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

### Configuration

Configure the Azure service endpoints, resource identifiers, model deployment details, and authentication settings required by the application.

Depending on the implementation, authentication may use Azure Identity credentials, API keys, or other supported authentication mechanisms.

**Security considerations:**

* Do not commit API keys, access tokens, or other secrets to version control.
* Store sensitive configuration in environment variables or an appropriate secrets manager.
* Ensure Azure resources have the minimum permissions required by the application.

### Run the Application

Start the application using its configured entry-point script.

For example, if the entry point is `app.py`:

```bash
python app.py
```

The exact command depends on the repository structure and the application's Gradio launch configuration.

## Potential Improvements

The current implementation is a learning-oriented, production-focused prototype. Several areas could be strengthened before using it as a production service.

* **Evaluation:** Introduce retrieval-quality metrics and answer-quality evaluation.
* **Observability:** Add structured logging, tracing, latency measurements, and failure monitoring.
* **Authentication:** Implement appropriate user authentication and access controls.
* **Error Handling:** Improve handling of failed document ingestion, indexing errors, retrieval failures, and model errors.
* **Scalability:** Evaluate asynchronous processing, concurrent requests, and ingestion workloads.
* **Deployment:** Package the application for a suitable cloud hosting environment.
* **Security:** Review secrets management, network access, data permissions, and document-level authorization.
* **Testing:** Add unit tests and integration tests for individual graph nodes and end-to-end workflows.

## Learning Outcomes

This project provided practical experience integrating:

* Azure cloud services for document storage, search, and AI capabilities.
* Retrieval-augmented generation for document-based question answering.
* LangGraph for conditional routing and stateful workflow orchestration.
* Gradio for building an interactive AI application.
* Cloud components into a cohesive application architecture.

The broader takeaway was that building useful AI systems involves more than connecting an LLM to a retrieval function. It also requires deliberate decisions about orchestration, indexing, service integration, failure handling, and deployment.

## Future Direction

Potential next steps include improving retrieval evaluation, introducing more robust observability, refining document ingestion, and strengthening deployment and security practices.

These improvements would help move the application from a learning-oriented prototype toward a more reliable and maintainable AI service.

## Acknowledgements

This project builds on concepts explored while preparing for and completing the Microsoft Azure AI Fundamentals (AI-901) certification.

The implementation provided an opportunity to apply those concepts through a practical integration of Azure services, LangGraph, and LLM-based document retrieval.

---

**Project Focus:** Retrieval-Augmented Generation · Azure AI · LangGraph · Cloud Integration · LLM Applications
