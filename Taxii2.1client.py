from taxii2client.v21 import Server
import json

url = input("Enter TAXII server URL: ")
username = input("Enter username: ")
password = input("Enter password: ")

try:
    server = Server(url=url, user=username, password=password)
    print("Server initialized successfully!")
    
    col = {}
    num_collections = 0
    for api_root in server.api_roots:
        try:
            # Count the number of collections
            num_collections += len(api_root.collections)
            
            for collection in api_root.collections:
                col[collection.id] = collection

        except Exception as e:
            print(f"Error occurred while fetching collections: {e}")
            continue

    print(f"Number of collections found: {num_collections}")

    # Hardcoded collection ID
    collection_id = 'da01d857-df1a-484a-b5fa-f0426b5880af'
    collection = col.get(collection_id)

    if collection:
        limit = int(input("Enter limit: "))
        
        filter_by_date = input("Do you want to add a filter based on date? (yes/no): ").lower()
        if filter_by_date == "yes":
            day = int(input("Enter day: "))
            month = int(input("Enter month: "))
            year = int(input("Enter year: "))
            added_after = f"{year:04d}-{month:02d}-{day:02d}T00:00:00.000Z"
        else:
            added_after = None
        
        response = collection.get_objects(limit=limit, added_after=added_after)
        print('Fetching data ..')
        print(json.dumps(response, indent=4))
    else:
        print("Collection not found.")
        
except Exception as e:
    print("Error initializing server:", e)
