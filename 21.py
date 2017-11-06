# The stolen breakfast drone

def find_unique_delivery_id(delivery_ids):
    return reduce(lambda x,y: x ^ y, delivery_ids)

ls = [1,2,3,4,3,2,1]
find_unique_delivery_id(ls)
