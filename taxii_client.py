from taxii2client.v21 import Server ,Collection
import sys
import json

url = 'https://otx.alienvault.com/taxii'
username = "6a699d84d5e21eceb77b9c4c37e60412a418884a1fd4068a5a3ac0e2e9717ec0"
password = "d960df79-8b9f-4729-a58c-fc6ad3d1e464"
server = Server(url=url, user=username, password=password)

col = {}
num_collections = 0

for api_root in server.api_roots:
    # Count the number of collections
    num_collections += len(api_root.collections)
    
print('total number of collection',num_collections)
for collection in api_root.collections:
    col[collection.id] = collection
    # print('each collection id',collection.id,collection.can_read)
    # print("collection.title: ", collection.title)
    # print("collection.description: ", collection.description)
    # print("collection.id: ", collection.id)
    # print('collection.custom_properties: ',collection.custom_properties)
    # print('collection.can_read: ',collection.can_read)
    # print('collection.can_write: ',collection.can_write)
    # print('collection.media_types: ',collection.media_types)
    response = collection.get_objects(limit=1000)
    print('response objects',response)
#     bundledata = {
#     "type": "bundle",
#     "id": "bundle--63fe3b22-0201-47cf-85d0-97c02164528d",
#     "objects": response
# }
    # print(json.dumps(response, indent=4))
#     response.pop("more")
#     response.pop("next")
#     file_path = r'C:\Users\H565438\OneDrive - Honeywell\Desktop\Scadafence\Taxii-Clients\testnew.json'
# with open(file_path, "w") as json_file:
#     json.dump(response, json_file, indent=4)
    # print('total number of collection',num_collections)s

