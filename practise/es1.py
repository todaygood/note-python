import elasticsearch
from datetime import datetime

es = elasticsearch.Elasticsearch('http://pcentos.hujun.com:9200')
resp= es.info()

print(resp)


def insert_rec_into_db():
    doc = {'author':"Hujun ",
           'text':'ElasticSearch: cool.bonsai cool.',
            'timestamp': datetime.now(),
           }

    resp = es.index(index="test-index", id=1, document=doc)
    resp=es.get(index="test-index", id=1)
    print(resp['_source'])

"""
client.indices.refresh(index='test-index')

resp = client.search(index='test-index',query={"match_all":{}})
print("Got %d hits:"% resp['hits']['total']['value'])

for hit in resp['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
"""

def gendata():
    mywords = ['foo', 'bar', 'baz']
    for word in mywords:
        yield {
            "_index": "mywords",
            "word": word,
        }


(es, gendata())

elasticsearch.
