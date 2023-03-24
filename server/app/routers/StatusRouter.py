import datetime
from fastapi import APIRouter
from models import StatusCodePost
from utils import filter_keyval_query_builder
from ESearch import es

router = APIRouter()


@router.get("/statusCode")
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



@router.post("/statusCode")
def postStatusCode(statusCode:StatusCodePost,key:str,val:str):

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



@router.get("/statusPieData")
def statusCodeLogs(key:str,val:str):

    query = filter_keyval_query_builder(key,val)

    res = es.search(
                index="network_logs",

                body={
                    "_source":[],
                    "size":0,
                    "query":{
                        "bool":{
                            "must":query
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
   
    return res["aggregations"]["by_statusCode"]["buckets"]

