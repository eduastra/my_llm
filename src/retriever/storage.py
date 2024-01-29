import os

from azure.identity import ClientSecretCredential
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
from llama_index.vector_stores.cogsearch import CognitiveSearchVectorStore


class Storage:
    clientSecretCredential: ClientSecretCredential

    def __init__(self):
        load_dotenv()
        self.az_search_endpoint = os.getenv("AZ_SEARCH_ENDPOINT")
        self.az_query_key = os.getenv("AZ_QUERY_KEY")
        self.az_admin_key = os.getenv("AZ_ADMIN_KEY")
        self.tenant_id = os.getenv("TENANT_ID")
        self.client = os.getenv("CLIENT_ID")
        self.key =  os.getenv("KEY_SECRET")
        self.clientSecretCredential = ClientSecretCredential(tenant_id=self.tenant_id,  
                                                             client_id=self.client,  
                                                             client_secret=self.key)
        self.cognitive_search_credential = AzureKeyCredential(str(self.az_admin_key))
        self.index_name = "" #TODO: set a name for index
        self.index_client = SearchIndexClient(
            endpoint=str(self.az_search_endpoint),
            credential=str(self.clientSecretCredential)
        )
        self.search_client = SearchClient(
            endpoint=str(self.az_search_endpoint),
            index_name=self.index_name,
            credential=str(self.clientSecretCredential)
        )
        self.metadata_fields = {}
        self.vector_store = CognitiveSearchVectorStore(
            search_or_index_client=self.search_client,
            filterable_metadata_field_keys=self.metadata_fields,
            id_field_key="id",
            chunk_field_key="content",
            embedding_field_key="content_vector",
            metadata_string_field_key="metadata",
            doc_id_field_key="doc_id")