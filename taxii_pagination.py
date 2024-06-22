from taxii2client.v21 import Server, as_pages,ApiRoot,Status
import json
import sys
server = Server(url="https://threatfeed.cyware.com/ctixapi/ctix21/taxii2",user='81d00f39-c255-480c-bbfb-63df51246409',password='d960df79-8b9f-4729-a58c-fc6ad3d1e464')


col = {}
 
for api_roots in server.api_roots:
    api_root = api_roots.collections
    try:
        for collections in api_roots.collections:
            col[collections.id] = collections 
            
 
    except:
        # print('')
        continue
# collection3 =  col['8a8723f3-1239-4d30-b9a5-3dc44a513b50']
collection3= col['da01d857-df1a-484a-b5fa-f0426b5880af']
response = collection3.get_objects(limit=10,added_after='2024-03-12T00:36:50.180Z')
print('filtered data',len(response['objects']))
print('filterd',json.dumps(response, indent=4))
page_no = 1
for envelope in as_pages(collection3.get_objects,per_request=7):
    print('\nPage # {}'.format(page_no))
    # print('an envelope is',envelope)
    # Parse the envelope as JSON
    # stix_objects = json.loads(envelope.text)
 
    # Pretty-print the STIX objects
    print('length of an envelope',len(envelope['objects']))
    print('data from pagination',json.dumps(envelope, indent=4))
 
    page_no += 1

sys.exit()    