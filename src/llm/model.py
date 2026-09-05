from langchain_groq import ChatGroq
from src.utils.settings import settings
from langchain_google_genai import ChatGoogleGenerativeAI

# def get_model():
#     try:
#         model = ChatGroq(
#             api_key=settings.GROQ_API_KEY,
#             model=settings.MODEL
#         )
#         return model
#     except Exception as e:
#         raise RuntimeError(f"Failed to initialize the model: {e}")
# Migrating to Google Platform
def get_model():
    try:
        google_model = ChatGoogleGenerativeAI(
            model=settings.GOOGLE_MODEL,
            api_key=settings.GOOGLE_API_KEY,
            temperature=0.4,
            max_output_tokens=1024
        )
        return google_model
    except Exception as e:
        raise RuntimeError(f"Failed to initialize the Google model: {e}")