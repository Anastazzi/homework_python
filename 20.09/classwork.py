import random

def create_city(population, size):
    return{'Население': population, 'Размер города': size}

def create_region(names, cities):
    d = dict()
    for names, cities in zip(names, cities):
        d[names] = cities
    return d
        
cities = [create_city(random.randint(10000, 200000), random.randint(345000, 670000)) for _ in range(1, 10)]
names = ['Sochi', 'Volgograd', 'Belgorod', 'Kiev', 'Moscow', 'Astrahan', 'Tagil', 'Samara', 'Sevastopol', 'Volzhsky']

print(create_region(names, cities))