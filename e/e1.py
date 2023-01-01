import datetime
import pprint

import pytz
import requests




if __name__ == '__main__':
 stat = datetime.datetime.now()
 for n in ["nizan" ]:
  name = n
  Nationalize_by_name = "https://api.nationalize.io/?"
  response = requests.get(Nationalize_by_name, params={'name': name})
  if response.status_code > 400:
   raise Exception("this name does not exist")
  # print(response.json()['country'])
  l = []
  for i in response.json()['country']:
    l.append(i['probability'])
  for i in response.json()['country']:
   if max(l) == i['probability']:
    country = i['country_id']
  # print(country)

  CountryRest = f"https://restcountries.com/v3.1/alpha/{country}"
  respo =  requests.get(CountryRest)
  if respo.status_code  > 400:
   raise Exception ("404")
  # print(respo.json())
  for i in respo.json():
   ful_contry_name = i['name']['common']
   region = i["region"]
   languages = i["languages"]
   languages_list = []
   time_zone = (i["timezones"])[0]
   print(time_zone)



   # print(time_zone)

   for l in languages.values():
     languages_list.append(l)


  print(f"Your name is the most popular in the state of"
        f" {ful_contry_name}, which is located on the continent of {region}.\n"
        f" and use it in language {languages_list}")
 print(datetime.datetime.now() - stat)