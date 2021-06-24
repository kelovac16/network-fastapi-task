from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

request_body = {
    "settings": {
        "number_of_shards": 5,
        "number_of_replicas": 1
    },

    'mappings': {
        'network': {
            'properties': {
                'cell_id': {'index': 'not_analyzed', 'type': 'string'},
                'site_id': {'index': 'not_analyzed', 'type': 'string'},
                'controller_id': {'index': 'not_analyzed', 'type': 'string'},
                'dlchbw': {'index': 'not_analyzed', 'type': 'integer'},
                'freq_band': {'index': 'not_analyzed', 'type': 'integer'},
            }}}
}


print("creating 'cell-revenue' index...")
res = es.index(index="network", body=request_body, doc_type='base')
print("index 'base-cell-revenue' is created")
