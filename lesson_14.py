import requests
import datetime
import threading


def nationalize_by_name(name: list):
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
    respo = requests.get(CountryRest)
    if respo.status_code > 400:
        raise Exception("404")
    # print(respo.json())
    for i in respo.json():
        ful_contry_name = i['name']['common']
        region = i["region"]
        languages = i["languages"]
        languages_list = []
        time_zone = (i["timezones"])[0]
        # print(time_zone)

        # print(time_zone)

        for l in languages.values():
            languages_list.append(l)

    print(f"{name} is the most popular in the state of"
          f" {ful_contry_name}, which is located on the continent of {region}.\n"
          f" and use it in language {languages_list}")
    print()
if __name__ == '__main__':
 stat = datetime.datetime.now()
 t = []
 for n in ["Kenyon", "Deshawn", "Michaela", "Molly", "Barrett", "Steven", "Brisa", "Zackery", "Kamora", "Sara", "Jaycee",
         "Leland", "Danny", "Ashlee", "Royce", "Bryce", "Anabel", "Skyler", "Cristian", "Shannon", "Aditya", "Asher",
         "Quintin", "Hunter", "Rose", "Ronin", "Zion", "Rayne", "Nyasia", "Sanaa", "Dominic", "Tyshawn", "Gillian",
         "Clayton", "Easton", "Julio", "Coby", "Melany", "Bradyn", "Jazlene", "Myah", "Zayden", "Noemi", "Brooks",
         "Mckenzie"]:
    t1 = threading.Thread(target=nationalize_by_name, args=(n,))
    t1.start()
    t.append(t1)
 for i in t:
     i.join()
 print(datetime.datetime.now()-stat)