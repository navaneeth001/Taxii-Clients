from taxii2client.v21 import Server, as_pages,ApiRoot
import json
import sys
server = Server(url="https://threatfeed.cyware.com/ctixapi/ctix21/taxii2",user='81d00f39-c255-480c-bbfb-63df51246409',password='d960df79-8b9f-4729-a58c-fc6ad3d1e464')

# print('server.details : ', server)
 
roots = []
for api in server.api_roots:
    roots.append(api.url)
    # print('roots are :', server.default.url)

# defining details about collections with api_root
default = ApiRoot(url=server.default.url,user='81d00f39-c255-480c-bbfb-63df51246409',password='d960df79-8b9f-4729-a58c-fc6ad3d1e464')
 
collection_no = 1
 
for collections in default.collections:
 
    # print()
    # print('Collection {}'.format(collection_no))
    # print()
    # print("collection.title: ", collections.title)
    # print("collection.description: ", collections.description)
    # print("collection.id: ", collections.id)
    # print('collection.custom_properties: ',collections.custom_properties)
    # print('collection.can_read: ',collections.can_read)
    # print('collection.can_write: ',collections.can_write)
    # print('collection.media_types: ',collections.media_types)
    # print()
 
    collection_no += 1    
# print('collection count', collection_no)
# sys.exit()
#fetching objects from a particular collection
col = {}
 
for api_roots in server.api_roots:
    api_root = api_roots.collections
    try:
        for collections in api_roots.collections:
            col[collections.id] = collections 
 
    except:
        # print('')
        continue
collection3 =  col['da01d857-df1a-484a-b5fa-f0426b5880af']
response = collection3.get_objects()
 
# Print the STIX objects
# print('objects from ',json.dumps(response, indent=4))

# get an object by object id

col = {}
 
for api_roots in server.api_roots:
    try:
        for collections in api_roots.collections:
            col[collections.id] = collections 
    except:
        # print('')
        continue
 
collection3 = col['39d4411c-5727-4d79-89d6-12bc3a2ae129']
# Retrieve a specific object by ID
response = collection3.get_object(obj_id='indicator--6f4a6ada-943a-44b6-90c2-edc228259dfd')
 
# # Print the STIX object
# print(json.dumps(response, indent=4))
    
def filter(object_id, object_version, collection=collection3):
    x =  collection.get_object(obj_id=object_id, modified=object_version)
    return x

    
get_version = filter('indicator--6f4a6ada-943a-44b6-90c2-edc228259dfd','2024-03-09T00:19:06.908Z')
 
# Print the STIX object
# print(json.dumps(get_version, indent=4))

# Pagination
page_no = 1
for envelope in as_pages(collection3.get_objects, per_request=1):
    # print('\nPage # {}'.format(page_no))
    # print('an envelope is',envelope)
    # Parse the envelope as JSON
    # stix_objects = json.loads(envelope.text)
 
    # Pretty-print the STIX objects
    print('data from pagination',json.dumps(envelope, indent=4))
 
    page_no += 1