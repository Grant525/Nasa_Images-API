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
    link = photos_data["collection"]["items"][i]["href"]
    data = photos_data["collection"]["items"][i]["data"][0]
    photos.append({
        "title": data.get("title"),
        "nasa_id": data.get("nasa_id"),
        "date_created": data.get("date_created"),
        "description": data.get("description"),
        "link" : link
    })

df = pd.DataFrame(photos)
#with open(",")
print(df)

