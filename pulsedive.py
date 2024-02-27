from taxii2client.v21 import Server
from taxii2client.v20 import Collection

server = Server(url='https://pulsedive.com/taxii2/api/collections?accept=application%2Ftaxii%2Bjson%3Bversion%3D2.1&pretty=1&key=bbcff74cf8442edcc8d52a4b61ec9a58912e0b018bbb473c0f08136595676723')
collection = Collection("https://pulsedive.com/taxii2/api/collections?accept=application%2Ftaxii%2Bjson%3Bversion%3D2.1&pretty=1&key=bbcff74cf8442edcc8d52a4b61ec9a58912e0b018bbb473c0f08136595676723")

print(collection.get_objects())
# print(server.description)