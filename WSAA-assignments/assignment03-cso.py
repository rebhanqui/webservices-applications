#link to data "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en"
import json
import requests

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en"

#get dataset from link using function getdata()
def getdata():
    response = requests.get(url)
    data = response.json()
    print(response)
    with open("cso.json", "wt") as fp:
        print(json.dumps(data), file = fp)

#call function
getdata()
    

