from cabby import create_client
api_key='bbcff74cf8442edcc8d52a4b61ec9a58912e0b018bbb473c0f08136595676723'
def main():
    testClient = create_client(
    discovery_url='https://pulsedive.com/taxii2?accept=application%2Ftaxii%2Bjson%3Bversion%3D2.1',
    use_https=True,
    version='2.1',
    discovery_path='/',
    headers={'Authorization':'Basic YmJjZmY3NGNmODQ0MmVkY2M4ZDUyYTRiNjFlYzlhNTg5MTJlMGIwMThiYmI0NzNjMGYwODEzNjU5NTY3NjcyMw==','Accept':'application%2Ftaxii%2Bjson%3Bversion%3D2.1'}
    )
    
    discover_services = testClient.discover_services()
    collections =testClient.get_collections()
    services =testClient.get_services()
    for collection in collections:
            print(collection)
    print('discover_services',discover_services)        
    print('services',services)
if __name__ == "__main__":
    main()