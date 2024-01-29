import os
import httpx
import json
import requests
from langchain.embeddings import AzureOpenAIEmbeddings

#TODO:  add a proper exception class for this module
#TODO:  Test langchain-community
#from langchain_community.embeddings import AzureOpenAIEmbeddings


class Embeddings:
    def __init__(self):
        self.access_token =  os.getenv("ACCESS_TOKEN")
        self.embedder = AzureOpenAIEmbeddings(
            azure_ad_token = self.access_token,
            model="gut_gpt_004",
            api_version="2023-05-15",
            azure_endpoint= os.getenv("AZURE_ENDPOINT")
        )