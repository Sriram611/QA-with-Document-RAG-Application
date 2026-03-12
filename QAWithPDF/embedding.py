from llama_index.core import VectorStoreIndex, Settings
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding

from QAWithPDF.data_ingestion import load_data
from QAWithPDF.model_api import load_model

import sys
from exception import CustomException
from logger import logger


def download_gemini_embedding(model, documents):
    """
    Initializes Gemini embeddings and creates a vector index.

    Returns:
    QueryEngine for querying the vector database.
    """

    try:
        logger.info("Initializing Gemini embedding model...")

        embed_model = GoogleGenAIEmbedding(
            model_name="gemini-embedding-001"
        )

        # Apply global settings
        Settings.llm = model
        Settings.embed_model = embed_model
        Settings.chunk_size = 1000
        Settings.chunk_overlap = 100

        logger.info("Creating vector index...")

        index = VectorStoreIndex.from_documents(documents)

        logger.info("Vector index created successfully")

        # persist index locally
        index.storage_context.persist(persist_dir="storage")

        logger.info("Index stored in storage directory")

        query_engine = index.as_query_engine()

        return query_engine

    except Exception as e:
        logger.error("Error in embedding creation")
        raise CustomException(e, sys)