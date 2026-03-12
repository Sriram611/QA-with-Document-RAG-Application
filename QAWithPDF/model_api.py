import os
import sys
from dotenv import load_dotenv

from llama_index.llms.google_genai import GoogleGenAI
import google.generativeai as genai

from exception import CustomException
from logger import logger


load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)


def load_model():
    """
    Loads a Gemini model for LLM inference.

    Returns:
        GoogleGenAI: Gemini LLM instance
    """

    try:
        logger.info("Loading Gemini model...")

        model = GoogleGenAI(
            model="models/gemini-2.5-flash",
            api_key=GOOGLE_API_KEY
        )

        logger.info("Gemini model loaded successfully")

        return model

    except Exception as e:
        logger.error("Error loading Gemini model")
        raise CustomException(e, sys)