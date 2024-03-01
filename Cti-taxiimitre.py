from taxii2client.v20 import Server
from taxii2client.v20 import Collection
server = Server("https://cti-taxii.mitre.org/stix")
collection = Collection("https://cti-taxii.mitre.org/stix/collections/95ecc380-afe9-11e4-9b6c-751b66dd541e")
print('collection media_types',collection.media_types)
# print('collection is',collection.get_objects())
print('api roots are',server.api_roots)
print('Server contact',server.contact)
print(server.title)
print(server.description)
