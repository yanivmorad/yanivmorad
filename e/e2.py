import requests

api = "https://api.publicapis.org/entries"
response = requests.get(api)
for i in response.json()["entries"]:
   # if i["Category"] not in ["Animals","Anime","Anti-Malware","Art & Design","Blockchain","Authentication & Authorization"]:
   #      print(i["Category"])
   #      print(i["Description"])
  if i["Category"] =="Development":
      print(i["Description"])