# 📄 Document Question Answering System (RAG with Gemini)

This project is a **Document Question Answering system** built using **Retrieval-Augmented Generation (RAG)**.  
It allows users to upload documents and ask questions about their content. The system retrieves relevant information from the document and generates answers using **Google Gemini Large Language Models**.

The application provides a simple web interface built with **Streamlit**, enabling users to interact with documents and extract useful insights efficiently.

---

## 🚀 Overview

Large Language Models cannot directly access private documents or external data.  
This project addresses that limitation by combining **document retrieval with generative AI**.

The system processes documents, converts their content into vector embeddings, and stores them in a searchable index. When a user asks a question, the system retrieves the most relevant information and uses the **Gemini LLM** to generate a meaningful response.

---

## ⚙️ How the System Works

The application follows a **Retrieval-Augmented Generation (RAG) pipeline**:

1. **Document Upload**  
   The user uploads a document through the Streamlit interface.

2. **Document Processing**  
   The document is loaded and split into smaller text segments.

3. **Embedding Generation**  
   Each text segment is converted into vector embeddings using **Gemini embedding models**.

4. **Vector Index Creation**  
   These embeddings are stored in a vector index for efficient similarity search.

5. **Query Processing**  
   When the user asks a question, the system searches the index to find the most relevant document segments.

6. **Answer Generation**  
   The retrieved context is passed to the **Gemini language model**, which generates the final answer.

---

## 🧠 Technologies Used

- **Python**
- **LlamaIndex** – Document indexing and retrieval
- **Google Gemini API** – Large Language Model and embeddings
- **Streamlit** – Web application interface
- **Python Logging** – Application logging
- **Custom Exception Handling** – Error tracking and debugging

---

## 🔑 Prerequisites

Before running the project, make sure you have:

- **Python 3.9 or higher**
- **Google Gemini API Key**

You can obtain a Gemini API key from:

https://ai.google.dev/

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Sriram611/document-qa-system.git
cd document-qa-system
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Setup

Create a `.env` file in the project root directory and add your Gemini API key:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run StreamlitApp.py
```

Once the application starts, open the following address in your browser:

```
http://localhost:8501
```

---

## 💡 Example Usage

1. Upload a document.
2. Enter a question related to the document.
3. The system retrieves relevant information and generates an answer.

This helps users quickly understand large documents and extract key information.

---

## 🔍 Use Cases

This system can be used for:

- Research document analysis
- Business document exploration
- Academic paper understanding
- Knowledge base question answering
- Automated document assistance
