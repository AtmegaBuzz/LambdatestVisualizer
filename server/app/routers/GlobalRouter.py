import datetime
from fastapi import APIRouter
from utils import filter_keyval_query_builder
from ESearch import es

router = APIRouter()


@router.get("/")
def home(key:str,val:str):

    yearly_log_count = []

    query = filter_keyval_query_builder(key,val)

    for i in range(365):

        date = (datetime.datetime.today() - datetime.timedelta(days=i)).strftime("%Y-%m-%d")
    

        res = es.count(
                index="network_logs",
                body={
                    "query":{
                        "bool":{
                            "must":[
                                {
                                    "match":{"datetime":date}
                                },
                                {"bool":{"must":query}}
                            ]
                        }
                    }
                }
            )

        yearly_log_count.append(res["count"])

    return yearly_log_count




@router.get("/logs")
def logs(key:str,val:str,multiMatch:str=None):

    
    if multiMatch and multiMatch.strip()!="":
        query = {
            "multi_match":{
                "query": multiMatch,
                "type": "phrase",
            },
        }

    else:
        es_query = filter_keyval_query_builder(key,val)
        query={
            "bool":{
                "must":[
                    {"bool":{"must":es_query}}
                ]
            }
        }

    

    resp = es.search(
        index="network_logs",
        size=10,
        query=query,
        sort=[
            {'datetime':{"order":"desc"}}
        ]
    )

    return resp["hits"]["hits"]

