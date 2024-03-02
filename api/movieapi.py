import requests


async def get_home_data():
    data = requests.get("http://localhost:8000/").json()
    print(data)
    return data
