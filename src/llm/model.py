from langchain_groq import ChatGroq
from src.utils.settings import settings


def get_model():
    try:
        model = ChatGroq(
            api_key=settings.GROQ_API_KEY,
            model=settings.MODEL
        )
        return model
    except Exception as e:
        raise RuntimeError(f"Failed to initialize the model: {e}")
