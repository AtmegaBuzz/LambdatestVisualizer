import datetime
import json
from elasticsearch import Elasticsearch
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import MimeTypePost, StatusCodePost


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows all origins
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods
    allow_headers=["*"]
)
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

    return yearly_log_count


@app.get("/mimeType")
def getMimeType():

    mime_typs = []

    res = es.search(
            index="network_logs",

            body={
                "_source":[],
                "size":0,
                "aggs":{
                    "by_mimeType":{
                        "terms":{
                            "field":f"params.response.mimeType.keyword",
                        }
                    }
                }
            }
        )
    
    mime_typs = [mimeType["key"] for mimeType in res["aggregations"]["by_mimeType"]["buckets"]]
    return mime_typs



@app.get("/mimeTypesLog")
def mimeTypesLog():

    res = es.search(
                index="network_logs",

                body={
                    "_source":[],
                    "size":0,
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
   
    return res["aggregations"]["by_mimeType"]["buckets"]



@app.post("/mimeType")
def postMimeType(mimeType:MimeTypePost):

    yearly_log_count = []

    for i in range(365):

        date = (datetime.datetime.today() - datetime.timedelta(days=i)).strftime("%Y-%m-%d")
    

        res = es.search(
                index="network_logs",

                body={
                    "_source":[],
                    "size":0,
                    "query":{
                        "bool":{
                            "must":[
                                    {"match" : { "datetime":date, }},
                                    {"match" : { "params.response.mimeType.keyword":mimeType.mimeType}}
                            ]
                        }  
                        
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

        if  len(res["aggregations"]["by_mimeType"]["buckets"])!=0:
            yearly_log_count.append((res["aggregations"]["by_mimeType"]["buckets"][0]["doc_count"]))
        else:
            yearly_log_count.append(0)

    return {"count":yearly_log_count}


@app.get("/statusCode")
def getStatusCode():

    mime_typs = []

    res = es.search(
            index="network_logs",

            body={
                "_source":[],
                "size":0,
                "aggs":{
                    "by_statusCode":{
                        "terms":{
                            "field":f"params.response.status",
                        }
                    }
                }
            }
        )
    
    mime_typs = [mimeType["key"] for mimeType in res["aggregations"]["by_statusCode"]["buckets"]]
    return mime_typs



@app.post("/statusCode")
def postStatusCode(statusCode:StatusCodePost):

    yearly_log_count = []

    for i in range(365):

        date = (datetime.datetime.today() - datetime.timedelta(days=i)).strftime("%Y-%m-%d")

        res = es.search(
                index="network_logs",

                body={
                    "_source":[],
                    "size":0,
                    "query":{
                        "bool":{
                            "must":[
                                    {"match" : { "datetime":date, }},
                                    {"match" : { "params.response.status":statusCode.statusCode}}
                            ]
                        }  
                        
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

        if  len(res["aggregations"]["by_statusCode"]["buckets"])!=0:
            yearly_log_count.append((res["aggregations"]["by_statusCode"]["buckets"][0]["doc_count"]))
        else:
            yearly_log_count.append(0)

    return {"count":yearly_log_count}



@app.get("/statusCodeLogs")
def statusCodeLogs():

    res = es.search(
                index="network_logs",

                body={
                    "_source":[],
                    "size":0,
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
   
    return res["aggregations"]["by_statusCode"]["buckets"]

