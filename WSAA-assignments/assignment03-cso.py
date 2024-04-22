#link to data "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en"
import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en"

def getexcheq():
    response = requests.get(url)
    return response.json()
    with open("cso.json", "wt") as fp:
        print(json.dumps(getexcheq()), file = fp)
             
getexcheq()