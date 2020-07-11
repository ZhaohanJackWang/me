TODO: Reflect on what you learned this week and what is still unclear.

Data sources:
- data.gov.au
- data.gov.uk
- data.gov

Initial ideas:
- relation of extreme rainfall to carbon emission
- air quality to corona virus cases (reflects government policies and level of production)

I/O:
mode: read "r"; write "w"

import requests
import json

url = "https://jsonplaceholder.typicode.com/todos/1"

r = requests.get(url)
if r.status_code is 200:
    the_json = json.loads(r.text)
    print(the_json)
    print(json.dumps(the_json, indent=4))
