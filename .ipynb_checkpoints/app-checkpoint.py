from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from elasticsearch import Elasticsearch
import logging

app = FastAPI()
es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200}])


class Network(BaseModel):
    cell_id: str
    site_id: str
    controller_id: str
    dlchbw: int
    freq_band: int


@app.get("/network5")
def get_network():
    res = es.search(index="network5", body={
        "query": {
            "bool": {
                "must": [
                    {
                        "match_all": {
                        }
                    }
                ],
                "must_not": [
                ],
                "should": [
                ]
            }
        },
        "from": 0,
        "size": 100
    })
    return res['hits']['hits']


@app.post("/network5")
def create_network(network: Network):
    body = {
        'cell_id': network.cell_id,
        'site_id': network.site_id,
        'controller_id': network.controller_id,
        'dlchbw': network.dlchbw,
        'freq_band': network.freq_band,
    }
    try:
        res = es.index(index="network5", body=body, id=network.cell_id, doc_type="base")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return res


@app.get("/network5/search/{term}")
def search_customer(term: str):
    body = {
        "query": {
            "query_string": {
                "query": "*" + term + "*",
                "fields": ["cell_id", "site_id"],
                "default_operator": "and"
            }
        }
    }

    res = es.search(index="network5", body=body)

    return res['hits']['hits']


if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
