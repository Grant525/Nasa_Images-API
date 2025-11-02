import requests
import json
import pandas as pd

url = "https://images-api.nasa.gov/search?q=Earth"
api_key = "WZflQNeWlQt2VNPyBFosptPDqwXmIDh7zYjYqcCI"
query_params = {"q" : "Earth", "media_type": "image"}

response = requests.get(url, params=query_params)
photos_data = response.json()
type = response.headers.get("Content-Type")
cleaned_data = json.dumps(photos_data, indent=2)
photos = []
for i in range(len(photos_data["collection"]["items"])):
    x = photos_data["collection"]["items"][i]["links"][0]["href"]
    photos.append(x)
df = pd.DataFrame(photos)
#with open(",")
print(df)