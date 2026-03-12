from llama_index.core import SimpleDirectoryReader
import sys
from exception import CustomException
from logger import logger


def load_data(data_path):
    """
    Load documents from a specified directory.

    Parameters:
    data_path (str): Path to directory containing documents.

    Returns:
    list: Loaded documents
    """
    try:
        logger.info("Data loading started...")

        loader = SimpleDirectoryReader(data_path)
        documents = loader.load_data()

        logger.info("Data loading completed")

        return documents

    except Exception as e:
        logger.error("Exception occurred while loading data")
        raise CustomException(e, sys)