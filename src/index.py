import sys
from pathlib import Path

from fastapi import FastAPI

sys.path.append(Path(__file__).parent)

from dotenv import load_dotenv

from retriever.retriever import retrieve_service


load_dotenv()

app = FastAPI(
    title="genia service",
    description="This is a RESTful API for the GENIA (personal-project) project, which provides named entity recognition services.",
    version="0.1.0"
)

app.include_router(retrieve_service)