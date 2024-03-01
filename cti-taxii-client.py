from taxii2client.v21 import Server

server = Server("https://otx.alienvault.com/taxii")
print(server.title)
print(server.description)
api_root = server.api_roots[0]
collection = api_root.collections[0]
print('collection name',collection)
print(collection.can_read,collection.can_write,collection.media_types)

