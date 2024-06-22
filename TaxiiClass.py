from taxii2client.v21 import Server
import json
import sys

class TaxiiClient:
    def __init__(self):
        self.url = "https://threatfeed.cyware.com/ctixapi/ctix21/taxii2"
        self.username = "81d00f39-c255-480c-bbfb-63df51246409"
        self.password = "d960df79-8b9f-4729-a58c-fc6ad3d1e464"
        self.server = None
        self.collections = []
        self.initialize_server()

    def initialize_server(self):
        try:
            self.server = Server(url=self.url, user=self.username, password=self.password)
            print("Server initialized successfully!")
        except Exception as e:
            raise Exception("Error initializing server:", e)

    def fetch_collections(self):
        try:
            for api_root in self.server.api_roots:
                for collection in api_root.collections:
                    self.collections.append(collection)
        except Exception as e:
            print(f"Error occurred while fetching collections: {e}")

    def fetch_data(self, limit, reference_time=None):
        fetched_objects = set()
        total_fetched = 0
        # print('total collections',self.collections)

        

        # for collection in self.collections:
        #     last_created_time=None
        #     print('each collection',collection.id)
        #     total_fetched=0
            # while total_fetched < limit:
            #     try:
            #         print(f'Fetching data from collection {collection.id} (total fetched: {total_fetched})..{last_created_time}')
            #         # response = collection.get_objects(limit=min(1000, limit - total_fetched),added_after=last_created_time)
            #         response = collection.get_objects(limit=2,added_after=last_created_time)
            #         if not response:
            #             break
            #         print('from collection id',collection.id,json.dumps(response, indent=4))
            #         for obj in response['objects']:
            #             created_time = obj['created']
            #             fetched_objects.add(obj['id'])
            #             total_fetched += 1
            #             last_created_time = created_time

            #         break

            #     except Exception as e:
            #         print(f"Error fetching data: {e}")
            #         break

            # Initial request to get the first batch of objects
        # col = {}
        # num_collections = 0
        # for api_root in self.server.api_roots:
        #     try:
        #         # Count the number of collections
        #         num_collections += len(api_root.collections)
                
        #         for collection in api_root.collections:
        #             col[collection.id] = collection

        #     except Exception as e:
        #         print(f"Error occurred while fetching collections: {e}")
        #         continue
        # collection = col['8a8723f3-1239-4d30-b9a5-3dc44a513b50']
        # response = collection.get_objects(limit=1000)
        # print('total response ',print(json.dumps(response, indent=4)))
        # print('no of objects',len(response['objects']))
        # count=0
        # while response:
            # Loop through each object in the response
            # for obj in response['objects']:
                # Print object details
                # print(json.dumps(obj, indent=4))
                
            # Check if there are more objects to fetch
            # if response.get('more', False):
                # print(f'more objects detected {count}',collection.id,response['next'])
                # Make the next request using the 'next' property
                # response = collection.get_objects(limit=1000, next=response['next'])
            # else:
            #     # No more objects to fetch, break the loop
            #     break
            # count=count+1
        col = {}
        num_collections = 0
        for api_root in self.server.api_roots:
            try:
                # Count the number of collections
                num_collections += len(api_root.collections)
                
                for collection in api_root.collections:
                    col[collection.id] = collection

            except Exception as e:
                print(f"Error occurred while fetching collections: {e}")
                continue
            collection = col['8a8723f3-1239-4d30-b9a5-3dc44a513b50']
        # for collection in self.collections:
            response = collection.get_objects(limit=1000)
            while response:
                    # Loop through each object in the response
                    count=0
                    for obj in response['objects']:
                        # Print object details
                        count=count+1
                        print(json.dumps(obj, indent=4))
                        print('object count',count)
                        
                    # Check if there are more objects to fetch
                    if response.get('more', True):
                        print(f'more objects detected {count}',collection.id,response['next'])
                        # Make the next request using the 'next' property
                        response = collection.get_objects(limit=10, next=response['next'])
                        print('more response objects based on more',json.dumps(response, indent=4))
                    else:
                        print('no more objects found',json.dumps(response, indent=4))
                        # No more objects to fetch, break the loop
                        break
            sys.exit()
    def execute(self, limit, filter_by_date=False, day=1, month=1, year=2023):
        if not self.server:
            print("Server not initialized. Please check server initialization.")
            return

        self.fetch_collections()

        if filter_by_date:
            reference_time = f"{year:04d}-{month:02d}-{day:02d}T00:00:00.000Z"
        else:
            reference_time = None

        self.fetch_data(limit, reference_time)

# Usage
try:
    taxii_client = TaxiiClient()
    limit = 10000
    filter_by_date = 'no'

    if filter_by_date == "yes":
        day = int(input("Enter day: "))
        month = int(input("Enter month: "))
        year = int(input("Enter year: "))
    else:
        day, month, year = 1, 1, 2023

    taxii_client.execute(limit, filter_by_date, day, month, year)

except Exception as e:
    print(e)
