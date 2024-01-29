from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException
from src.retriever.embedder import Embeddings
from src.retriever.storage import Storage
from llama_index import (SimpleDirectoryReader, StorageContext, ServiceContext, VectorStoreIndex)


retrieve_service: APIRouter = APIRouter()

load_dotenv()

@retrieve_service.get("/retrieve")
async def search_engine( query: str):
    storage = Storage()
    Embeddings = Embeddings()

    #storage_context= StorageContext.from_defaults(vector_store=storage.vector_store)
    service_context= ServiceContext.from_defaults(llm=None, embed_model=Embeddings.embedder)

    index_vector_data = VectorStoreIndex.from_vector_store(
        vector_store=storage.vector_store, service_context=service_context
    )


    query_engine_azureopenai = index_vector_data.as_retriever()

    response = query_engine_azureopenai.retrieve(query)

    return response