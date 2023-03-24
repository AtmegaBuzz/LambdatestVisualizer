import datetime
from fastapi import APIRouter
from models import MimeTypePost
from utils import filter_keyval_query_builder
from ESearch import es


router = APIRouter()

@router.get("/mimeType")
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


@router.post("/mimeType")
def postMimeType(mimeType:MimeTypePost,key:str,val:str):


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
                                    {"match" : { "params.response.mimeType.keyword":mimeType.mimeType}},
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



@router.get("/mimePieData")
def mimeTypesLog(key:str,val:str):

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



