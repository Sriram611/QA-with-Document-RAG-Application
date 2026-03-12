import streamlit as st
import os

from QAWithPDF.data_ingestion import load_data
from QAWithPDF.embedding import download_gemini_embedding
from QAWithPDF.model_api import load_model


def save_uploaded_file(uploaded_file):
    os.makedirs("Data", exist_ok=True)

    file_path = os.path.join("Data", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path


def main():
    st.set_page_config(page_title="QA with Documents")

    st.header("QA with Documents (Information Retrieval)")

    uploaded_file = st.file_uploader("Upload your document")

    user_question = st.text_input("Ask your question")

    if uploaded_file is not None:

        file_path = save_uploaded_file(uploaded_file)

        if st.button("Submit & Process"):

            with st.spinner("Processing..."):

                documents = load_data("Data")

                model = load_model()

                query_engine = download_gemini_embedding(model, documents)

                st.success("Document processed successfully")

                if user_question:
                    response = query_engine.query(user_question)
                    st.write(response.response)


if __name__ == "__main__":
    main()