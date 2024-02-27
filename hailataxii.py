import pprint

from cabby import create_client

HailATaxiiFeedList=[
    'guest.Abuse_ch',
    'guest.CyberCrime_Tracker',
    'guest.EmergingThreats_rules',
    'guest.Lehigh_edu',
    'guest.MalwareDomainList_Hostlist',
    'guest.blutmagie_de_torExits',
    'guest.dataForLast_7daysOnly',
    'guest.dshield_BlockList',
    'guest.phishtank_com'
]

client = create_client(
    'hailataxii.com',
    use_https=False,
    discovery_path='/taxii-discovery-service')

print (":client is",client)
services = client.discover_services()
print ("services are",services)
for service in services:
    print('Service type= {s.type} , address= {s.address}' .format(s=service))

collections = client.get_collections(
    uri='http://hailataxii.com/taxii-data')
print ("collections",collections)

