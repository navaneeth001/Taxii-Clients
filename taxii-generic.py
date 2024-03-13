from taxii2client.v21 import Server, as_pages,ApiRoot,Collection
import json

server = Server(url="https://threatfeed.cyware.com/ctixapi/ctix21/taxii2",user='81d00f39-c255-480c-bbfb-63df51246409',password='d960df79-8b9f-4729-a58c-fc6ad3d1e464')

print('server.details : ', server)
 
roots = []
for api in server.api_roots:
    roots.append(api.url)
    print('roots are :', server.default.url)

### defining details about collections with api_root
default = ApiRoot(url=server.default.url,user='81d00f39-c255-480c-bbfb-63df51246409',password='d960df79-8b9f-4729-a58c-fc6ad3d1e464')
collection = Collection()
collection_no = 1
 
for collections in default.collections:
 
    print()
    print('Collection {}'.format(collection_no))
    print()
    print("collection.title: ", collections.title)
    print("collection.description: ", collections.description)
    print("collection.id: ", collections.id)
    print('collection.custom_properties: ',collections.custom_properties)
    print('collection.can_read: ',collections.can_read)
    print('collection.can_write: ',collections.can_write)
    print('collection.media_types: ',collections.media_types)
    print()
 
    collection_no += 1    


###fetching objects from a particular collection
col = {}
 
for api_roots in server.api_roots:
    api_root = api_roots.collections
    try:
        for collections in api_roots.collections:
            col[collections.id] = collections 
            print('each collection',collections)
 
    except:
        print('')
        continue
collection3 =  col['7f9137a7-59ff-4fc6-957a-a90cc66c91b5']
response = collection3.get_objects()
 
# Print the STIX objects
print('objects from ',json.dumps(response, indent=4))

### get an object by object id

col = {}
 
for api_roots in server.api_roots:
    try:
        for collections in api_roots.collections:
            col[collections.id] = collections 
    except:
        print('')
        continue
 
collection3 = col['39d4411c-5727-4d79-89d6-12bc3a2ae129']


# Retrieve a specific object by ID
response = collection3.get_object(obj_id='indicator--6f4a6ada-943a-44b6-90c2-edc228259dfd')
 
# # Print the STIX object
print(json.dumps(response, indent=4))
    
def filter(object_id, object_version, collection=collection3):
    x =  collection.get_object(obj_id=object_id, modified=object_version)
    return x

    
get_version = filter('indicator--6f4a6ada-943a-44b6-90c2-edc228259dfd','2024-03-09T00:19:06.908Z')
 
# Print the STIX object
print(json.dumps(get_version, indent=4))