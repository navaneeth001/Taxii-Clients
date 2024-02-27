from taxii2client.v21 import Server
server = Server(url="https://pulsedive.com/taxii2?accept=application%2Ftaxii%2Bjson%3Bversion%3D2.1&key=bbcff74cf8442edcc8d52a4b61ec9a58912e0b018bbb473c0f08136595676723")
print(server.title)
print(server.description)
print(server.api_roots[0])
print(server.contact)

api_root = server.api_roots[0]
collection = api_root.collections[0]
print(collection.can_read,collection.can_write,collection.media_types)
