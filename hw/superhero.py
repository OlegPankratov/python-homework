import requests

base_url = "https://superheroapi.com/api/2619421814940190/"

def get_hero_id_by_name(name):
    response = requests.get(base_url + "search/" + name)
    return response.json()['results'][0]['id']

def get_hero_intelligence_by_id(id):
    response = requests.get(base_url + id + "/powerstats")
    return response.json()['intelligence']

def get_most_intelligence_hero(heroes):
    max_intelligence = 0
    for hero_int in heroes.keys():
        if int(hero_int) > max_intelligence:
            max_intelligence = int(hero_int)
    return heroes[str(max_intelligence)]

hero_names = ['Hulk', 'Captain America', 'Thanos']
heroes = {}
for name in hero_names:
    hero_id = get_hero_id_by_name(name)
    hero_intelligence = get_hero_intelligence_by_id(hero_id)
    heroes[hero_intelligence] = name

print(get_most_intelligence_hero(heroes))
