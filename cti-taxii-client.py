from taxii2client.v21 import Server
from taxii2client.v21 import Collection

import json

server = Server("https://otx.alienvault.com/taxii")
collection = Collection("https://otx.alienvault.com/taxii")

print(server.title)
print(server.description)
api_root = server.api_roots[0]
collection = api_root.collections[0]
temp=json.dumps(collection.get_objects())
print(temp)

