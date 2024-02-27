import json
import os
from OTXv2 import OTXv2
# store OTX API key in environment variable OTX_API_KEY
API_KEY = "6a699d84d5e21eceb77b9c4c37e60412a418884a1fd4068a5a3ac0e2e9717ec0"

otx = OTXv2(API_KEY)
pulse_id = '57204e9b3c4c3e015d93cb12'
indicators = otx.get_pulse_indicators(pulse_id=pulse_id)
print('Indicators aree:',indicators)

for indicator in indicators:
    print(indicator['indicator'] + ',' + indicator['type'] + ',' + str(indicator['id']))