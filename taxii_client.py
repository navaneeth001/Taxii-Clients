from cabby import create_client
api_key='bbcff74cf8442edcc8d52a4b61ec9a58912e0b018bbb473c0f08136595676723'
def main():
    testClient = create_client(
    discovery_url='https://pulsedive.com/taxii2'+'/?accept=application%2Ftaxii%2Bjson%3Bversion%3D2.1&pretty=1&key=' + api_key,
    # use_https=True,
    # discovery_path='/',
    headers={'Authorization': f'Apikey {api_key}'}
    )
    collections =testClient.set_auth(password='bbcff74cf8442edcc8d52a4b61ec9a58912e0b018bbb473c0f08136595676723' )


    # discover_services = testClient.discover_services()
    collections =testClient.get_collections()
    services =testClient.get_services()
    for collection in collections:
            print(collection)
    # print('discover_services',discover_services)        
    print('services',services)
if __name__ == "__main__":
    main()