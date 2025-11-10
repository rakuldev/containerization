import requests

def get_req():
    api_url = "https://opensky-network.org/api/states/all?origin_country=srilanka&category=20"
    response = requests.get(api_url)
    print(response.json())
    print("-----------")
    print(response.status_code)

def post_req():
    api_url = "https://opensky-network.org/api/states/all?time=1458564121&icao24=3c4"
    data = {'states': [['3c6444', 'changes']]}
    response = requests.get(api_url, json=data)
    print(response.json())
    print("-----------")
    print(response.status_code)


if __name__=="__main__":
    get_req()