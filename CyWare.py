from taxii2client.v21 import Server, ApiRoot
from cytaxii2 import cytaxii2
import json

server = Server(url="https://threatfeed.cyware.com/ctixapi/ctix21/taxii2/",user='81d00f39-c255-480c-bbfb-63df51246409',password='d960df79-8b9f-4729-a58c-fc6ad3d1e464')
# print('collection is',collection.get_objects())
# cytaxii_object = cytaxii2.cytaxii2('https://threatfeed.cyware.com/ctixapi/ctix21/taxii2/', '81d00f39-c255-480c-bbfb-63df51246409', 'd960df79-8b9f-4729-a58c-fc6ad3d1e464', version=2.1)

print('api roots are',server.api_roots[0])
print('Server contact',server.contact)

# print(server.title)
temp1=ApiRoot(url="https://threatfeed.cyware.com/ctixapi/ctix21/taxii2/",user='81d00f39-c255-480c-bbfb-63df51246409',password='d960df79-8b9f-4729-a58c-fc6ad3d1e464')
# print('ApiRoot data is',temp1.collections())
api_root = server.api_roots[0]
print('api_root data is',api_root)

collection = api_root.collections[0]
temp=json.dumps(collection.get_objects())
# print(temp)

# print(server.description)
# print('cytaxii_object from api',cytaxii_object.collection_request())
# collections=cytaxii_object.collection_request()
# temp=json.dumps(collections)
# print(temp)
# poll_response = cytaxii_object.poll_request(collection_id='46cc884e-fd37-4436-95b3-ac73710df3dc', added_after=None, limit=2, object_id=None)
# temp=json.dumps(poll_response)
# print(temp)

# collection_data = cytaxii_object.collections(collection_id="6ab49abf-a67b-42cd-a90c-045644a515c0")
# print(collection_data)

# discovery_response = cytaxii_object.discovery_request()
# print('discovery_response is',discovery_response)
# print('get objects are',collection.get_objects())