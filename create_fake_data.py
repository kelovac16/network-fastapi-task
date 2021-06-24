from faker import Factory
from elasticsearch import Elasticsearch
import json

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


def create_names(fake):
    for x in range(100):
        go = es.index(
            index="network",
            body={
                "cell_id": fake.pystr(min_chars=2, max_chars=2),
                "site_id": fake.pystr(min_chars=2, max_chars=2),
                "controller_id": fake.pystr(min_chars=2, max_chars=2),
                "dlchbw": fake.pyint(min_value=1, max_value=100, step=1),
                "freq_band": fake.pyint(min_value=1, max_value=100, step=1)
            }
        )
        print(json.dumps(go))


if __name__ == '__main__':
    fake = Factory.create()
    create_names(fake)
