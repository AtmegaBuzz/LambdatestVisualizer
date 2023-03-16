


def filter_keyval_query_builder(key:str,val:str):

    query = {"bool":{"must":[]}}
    if key!="" and val!="":
        
        # filter for keyword if val is string
        if not val.isdigit():
            key += ".keyword"

        query = {
            "bool":{
                "must":[
                    {
                        "match":{key:val}
                    }
                ]
            }
        }
    

    return query