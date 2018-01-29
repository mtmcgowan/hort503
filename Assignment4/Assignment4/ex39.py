# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
    }

# Create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
    }

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is : {city}")

# Study Drills

# 1. Do this same kind of mapping with cities and states/regions in your country or some other country.

# add some more states
states['Washington'] = 'WA'
states['Idaho'] = 'ID'
states['Kansas'] = 'KS'

# add some more cities
cities['WA'] = 'Pullman'
cities['ID'] = 'Moscow'
cities['Kansas'] = 'Colby'

city = cities.get('WI', 'Not there...')
print(f"The city for the state 'MI' is : {city}")

# count the number of items in the list
states.count('New York')
states.sort()

# 2. What more can be done with dicts?
# You can modify numerics with math
inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
print(inventory)
inventory["bananas"] += 200
print(inventory)

# 3. What can't be done with dicts?
# You can't use a list as a dictionary key

