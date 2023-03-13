import datetime
from elasticsearch import Elasticsearch
from fastapi import FastAPI




app = FastAPI()
es = Elasticsearch("http://localhost:9200")


@app.get("/")
def home():

    yearly_log_count = []


    for i in range(365):

        date = (datetime.datetime.today() - datetime.timedelta(days=i)).strftime("%Y-%m-%d")
    

        res = es.count(
                index="network_logs",
                body={
                    "query":{
                        "match":{
                            "datetime":date,
                        },
                        
                    }
                }
            )

        yearly_log_count.append(res["count"])

    return {"count":yearly_log_count}


@app.get("/mimeType")
def filter():

    yearly_log_count = []

    for i in range(365):

        date = (datetime.datetime.today() - datetime.timedelta(days=i)).strftime("%Y-%m-%d")
    

        res = es.search(
                index="network_logs",

                body={
                    "_source":[],
                    "size":0,
                    "query":{
                        "match":{
                                "datetime":date,
                        },
                    },
                    "aggs":{
                        "by_mimeType":{
                            "terms":{
                                "field":f"params.response.mimeType.keyword",
                                "order":{
                                    "_count":"desc"
                                },
                            }
                        }
                    }
                }
            )
        yearly_log_count.append(res["aggregations"]["by_mimeType"]["buckets"])

    return {"count":yearly_log_count}

@app.get("/statusCode")
def filter():

    yearly_log_count = []

    for i in range(365):

        date = (datetime.datetime.today() - datetime.timedelta(days=i)).strftime("%Y-%m-%d")
    

        res = es.search(
                index="network_logs",

                body={
                    "_source":[],
                    "size":0,
                    "query":{
                        "match":{
                                "datetime":date,
                        },
                    },
                    "aggs":{
                        "by_statusCode":{
                            "terms":{
                                "field":f"params.response.status",
                                "order":{
                                    "_count":"desc"
                                },
                            }
                        }
                    }
                }
            )
        yearly_log_count.append(res["aggregations"]["by_statusCode"]["buckets"])
    print(len(yearly_log_count))
    return {"count":yearly_log_count}

