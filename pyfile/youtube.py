import requests
import json

url = "https://youtube138.p.rapidapi.com/channel/videos/"

payload = {
	"id": "UCJ5v_MCY6GNUBTO8-D3XoAg",
	"filter": "videos_latest",
	"cursor": "",
	"hl": "en",
	"gl": "US"
}
headers = {
	"x-rapidapi-key": "ee6f1a9e8cmsh64ba9ca648a4d3ap16164fjsnb5152d7cd4ad",
	"x-rapidapi-host": "youtube138.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

data = response.json()

with open ("/home/deepak/projects/practice/practice/datafile/youtube.json","w") as json_file:
    json.dump(data, json_file, indent=4)