import json
from elasticsearch import Elasticsearch
es = Elasticsearch("http://localhost:9200")
es.info().body

with open('sample.json', encoding='UTF-8') as raw_data:
    json_docs = json.load(raw_data) 
    for car in json_docs:
        es.index(index='cars', document=car)
    