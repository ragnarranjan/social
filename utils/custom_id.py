def generate_new_id(collection):
    id = 1
    get_id = collection.find_one(sort = [("id",-1)])
    if get_id and get_id.get("id"):  #---get id is for the condion to prevent from getting none as bcz if if there is noting then it will be giving None
        id = get_id.get("id") + 1
    return id
