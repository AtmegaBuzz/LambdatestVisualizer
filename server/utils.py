


def filter_keyval_query_builder(key:str,val:str):

    
    query = []

    if key.strip()!="" and val.strip()!="":
        
        # filter for keyword if val is string
        if not val.isdigit():
            key += ".keyword"

        
        query = [{"match":{key:val}}]
    

    return query

    

