from taxii2client.v21 import Server
from taxii2client.v21 import Collection

server = Server("https://otx.alienvault.com/taxii")
print(server.title)
print(server.description)
print(server.api_roots[0])
print(server.contact)
# print('collection1 objects are',collection1.get_objects())
api_root = server.api_roots[0]
collection = api_root.collections[0]
print('collection name',collection)
# print('data objects from collection are',collection.get_objects())
print(collection.can_read,collection.can_write,collection.media_types)

