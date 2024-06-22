from taxii2client.v21 import Server
import json
import sys

url = "https://pulsedive.com/taxii2/"
username = "taxii2"
password = "bbcff74cf8442edcc8d52a4b61ec9a58912e0b018bbb473c0f08136595676723"
# reference_time="2022-11-20T15:56:04.100Z" // optional date object to filter out objects based on created date
reference_time=None #set as none ot not appy any date filter
server = None
try:
    server = Server(url=url, user=username, password=password)
    print("Server initialized successfully!")
    
    col = {}
    num_collections = 0

    for collection in server.api_roots[0].collections:
        if collection.can_read:  
            response = collection.get_objects(limit=1000,added_after=reference_time)
            print(f'collection of id {collection.id} is processing')
            if 'more' not in response:
                print('Collection is empty')
                count=0 #setting to zero in case of empty collection
            else:
                count=len(response['objects']) #incase of collections which has less than 1000 object, total number of objects is stored as count else be set as 1000
            while response:
                    # Check if there are more objects to fetch
                    if 'more' not in response:
                        # No more objects to fetch, break the loop
                        break
                    if response.get('more', True):
                        print(f'number of objects fetched {count} from collection {collection.id}')
                        print('more response objects:',json.dumps(response, indent=4))
                        if 'next' not in response:
                            print('Collection is empty')
                            # No more objects to fetch, break the loop
                            break
                        # Make the next request using the 'next' property
                        response = collection.get_objects(limit=1000, next=response['next'],added_after=reference_time)
                        count=count+len(response['objects'])
                    else:
                        print('no more objects found',json.dumps(response, indent=4))
                        # No more objects to fetch, break the loop
                        break
        else:
            print(f'collection id {collection.id} does not have read access')                    

except Exception as e:
    print("Error initializing server:", e)
