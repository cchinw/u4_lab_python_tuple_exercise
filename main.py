
# Create a list named students containing some student names (strings).
# Print out the second student's name.
# Print out the last student's name.
students = ['Jenna', 'Molly', 'Nghiem', 'Chinwendu']
print(students[1])
print(students[3])

# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Use a for loop to print out the string "food goes here is a good food".
foods = ('Fried Rice', 'Jollof Rice', 'Efo-riro', 'Nkwobi', 'amala')
for word in foods:
    print(word + ' is a good food')

# Using a for loop, print just the last two food strings from foods.
for word in foods:
    print(foods[2:4])

# Create a dictionary named home_town containing the keys of city, state and population.
# Print a string with this format:
# "I was born in city, state - population of population"
home_town = {'city': 'Lagos', 'state': 'Lagos', 'population': 153888000}
print('I was born in ' + home_town['city'] + ', ' +
      home_town['state'] + '- population of ' + (str)(home_town['population']))

# Iterate over the key: value pairs in home_town and print a string for each item, for example:
# "city = Arcadia"
# "state = California"
# "population = 58000"
for i, j in home_town.items():
    print(i, '=', j)

# Create an empty list named cohort.
# Using a for loop, add one dictionary to the cohort list for each student name. Each dictionary should have this shape:
#  {
#    'student': 'Tina',
#    'fav_food' 'Cheeseburger'
#  }
# Iterate over cohort printing out each element.
cohort = []
for index in range(0, len(students)):
    cohort.append({
        'student': students[index],
        'fav_food': foods[index]
    })
for student in cohort:
    print(student)

# Using the list of students and list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
# Iterate over awesome_students printing out each string.
awesome_students = ['{} is awesome!'.format(student) for student in students]
for i in awesome_students:
    print(i)

# Using the tuple foods and list comprehension within a for loop, print each food string that contains the letter a.
tup_foods = [food for food in foods if 'a' in food]
print(tup_foods)
