


def filter_keyval_query_builder(key:str,val:str):

    '''
        The function takes a key-value pair as string inputs and returns an Elasticsearch query list. 
        If the value is a string, ".keyword" is appended to the key and the query dictionary 
        is created using the "match" operator.
    '''

    query = []

    if key.strip()!="" and val.strip()!="":
        
        # filter for keyword if val is string
        if not val.isdigit():
            key += ".keyword"

        
        query = [{"match":{key:val}}]
    

    return query

    

