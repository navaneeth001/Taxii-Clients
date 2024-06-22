from taxii2client.v21 import Server
import json

class TaxiiClient:
    def __init__(self, url, username, password, reference_time=None):
        self.url = url
        self.username = username
        self.password = password
        self.reference_time = reference_time
        self.server = self.initialize_server()

    def initialize_server(self):
        try:
            server = Server(url=self.url, user=self.username, password=self.password)
            print("Server initialized successfully!")
            return server
        except Exception as e:
            print("Error initializing server:", e)
            return None

    def process_collections(self):
        if self.server is None:
            print("Server not initialized!")
            return

        try:
            print('number of collections',len(self.server.api_roots[0].collections))
            for collection in self.server.api_roots[0].collections:
                if collection.can_read:
                    print(f'collection of id {collection.id} is processing')
                    response = collection.get_objects(limit=1000, added_after=self.reference_time)
                    if 'more' not in response:
                        print('Collection is empty')
                        count = 0
                    else:
                        count = len(response['objects'])
                        print('no of objects is',count)
                    while response and count<10000: #fetching the first 10000 objects from a collection
                        if 'more' not in response:
                            break
                        if response.get('more', True):
                            print(f'number of objects fetched {count} from collection {collection.id}')
                            print('Response objects:', json.dumps(response, indent=4))
                            if 'next' not in response:
                                print('Collection is empty')
                                break
                            response = collection.get_objects(limit=1000, next=response['next'], added_after=self.reference_time)
                            count += len(response['objects'])
                        else:
                            print('no more objects found', json.dumps(response, indent=4))
                            break
                else:
                    print(f'collection id {collection.id} does not have read access')
        except Exception as e:
            print("Error processing collections:", e)

# Example usage: give details of any Taxii server below
# url = "https://threatfeed.cyware.com/ctixapi/ctix21/taxii2"
# username = "81d00f39-c255-480c-bbfb-63df51246409"
# password = "d960df79-8b9f-4729-a58c-fc6ad3d1e464"

url = "https://pulsedive.com/taxii2"
username = "taxii2"
password = "bbcff74cf8442edcc8d52a4b61ec9a58912e0b018bbb473c0f08136595676723"

# url = "https://otx.alienvault.com/taxii"
# username = "6a699d84d5e21eceb77b9c4c37e60412a418884a1fd4068a5a3ac0e2e9717ec0"
# password = "bbcff74cf8442edcc8d52a4b61ec9a58912e0b018bbb473c0f08136595676723"

reference_time = None #Replace with a valid timestamp to filter the results based on created date
taxii_client = TaxiiClient(url, username, password, reference_time)
taxii_client.process_collections()
