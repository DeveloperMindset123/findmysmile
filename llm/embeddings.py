import pymongo
from llama_index.vector_stores.mongodb import MongoDBAtlasVectorSearch
from llama_index.core import VectorStoreIndex
from llama_index.core import StorageContext
from llama_index.core import SimpleDirectoryReader
import os

def get_mongo_client():
  """Establish connection to the MongoDB."""
  try:
    mongo_uri = os.environ["MONGO_URI"]
    client = pymongo.MongoClient(mongo_uri)
    print("Connection to MongoDB successful")
    mongodb_client = pymongo.MongoClient(mongo_uri)
    store = MongoDBAtlasVectorSearch(client)
    storage_context = StorageContext.from_defaults(vector_store=store)
    docs = SimpleDirectoryReader(
    input_files=["./data"]
    ).load_data()
    index = VectorStoreIndex.from_documents(
        docs, storage_context=storage_context
    )
    return index
    
  except pymongo.errors.ConnectionFailure as e:
    print(f"Connection failed: {e}")
    return None

