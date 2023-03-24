import os
from dotenv import load_dotenv
from elasticsearch import Elasticsearch

# Load .env variables 
load_dotenv()


ES_HOST = os.getenv("ELASTICSEARCH_HOSTS")
es = Elasticsearch(ES_HOST)