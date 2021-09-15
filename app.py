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


@app.get("/network")
def get_network():
    res = es.search(index="network", body={
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


@app.post("/network")
def create_network(network: Network):
    body = {
        'cell_id': network.cell_id,
        'site_id': network.site_id,
        'controller_id': network.controller_id,
        'dlchbw': network.dlchbw,
        'freq_band': network.freq_band,
    }
    try:
        res = es.index(index="network", body=body, id=network.cell_id, doc_type='base')
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/network/search/{term}")
def search_network(term: str):
    body = {
        "query": {
            "query_string": {
                "query": "*" + term + "*",
                "fields": ["cell_id", "site_id", "controller_id"],
                "default_operator": "and"
            }
        },
        "from": 0,
        "size": 50
    }

    res = es.search(index="network", body=body)

    return res['hits']['hits']


@app.get("/network/cell/{term}")
def search_by_cell_id(term: str):
    body = {
        "query": {
            "query_string": {
                "query": "*" + term + "*",
                "fields": ["cell_id"]
            }
        },
        "from": 0,
        "size": 50
    }

    res = es.search(index="network", body=body)

    return res['hits']['hits']


@app.get("/network/site/{term}")
def search_by_site_id(term: str):
    body = {
        "query": {
            "query_string": {
                "query": "*" + term + "*",
                "fields": ["site_id"]
            }
        },
        "from": 0,
        "size": 50
    }

    res = es.search(index="network", body=body)

    return res['hits']['hits']


@app.get("/network/controller/{term}")
def search_by_controller_id(term: str):
    body = {
        "query": {
            "query_string": {
                "query": "*" + term + "*",
                "fields": ["controller_id"]
            }
        },
        "from": 0,
        "size": 50
    }

    res = es.search(index="network", body=body)

    return res['hits']['hits']


if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
