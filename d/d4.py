import string, datetime


def alphabet_indexes(english_alphabet: list[str]):
    index = map((' ' + string.ascii_lowercase).find, map(str.lower, english_alphabet))
    return list(index)


def chak_voels(w):
    if w in ['a', 'e', 'i', 'o', 'u']:
        return False
    else:
        return True


def filter_vowels(word: str):
    adults = filter(chak_voels, word)
    return ''.join(list(adults))


# print(filter_vowels("helloo"))




def f(date):
    if date.strftime('%A') not in ['Friday','Saturday']:
        return True
    else:
        return False
def filter_Fridays_Saturdays(datelist:list):
    date = list(map(datetime.datetime.strptime,datelist,['%d-%m-%Y']*len(datelist)))
    return list(filter(f,date))

d = filter_Fridays_Saturdays( ['12-12-2021', '18-12-2021', '19-12-2021','22-12-2022','23-12-2022'])
# print(d)


def len_string(string_list: list[str]):
    return sorted(string_list, key=len)

# print(len_string(['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']))

buses = [
        {
           "delays": ['1h 20m', '25m', '3h', '2h 1m'],
           "status": 'bad',
           "name": "Jacob",
           "route_num": 560
        },
       {
           "delays": ['20m', '5m', '3h'],
           "status": 'great',
           "name": "Moshe",
           "route_num": 769
        },
       {
           "delays": ['2h 3m'],
           "status": 'good',
           "name": "Jack",
           "route_num": 766
        },
       {
           "delays": ['6h'],
           "status": 'great',
           "name": "Mark",
           "route_num": 876
        },
         {
           "delays": ['2h 3m'],
           "status": 'good',
           "name": "Anna",
           "route_num": 456
        },
]


def buss_dictionary(dictionary):
    return sorted(dictionary, key=lambda b: (b["status"], len(b['delays']), b['name']), reverse=True)

# print(buss_dictionary(buses))

def dabell_a(list_strings:list[str]):
    return filter(lambda a:a.count("a")>=2,list_strings)

g= dabell_a( ["apple", "ananas", "banana", "pear"])
# print(list(g))