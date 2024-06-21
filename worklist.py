'''1.Suppose you want to write a program that prints numbers from 1 to 10, formatted like this:

Current value: 1
Current value: 2
...
Current value: 10'''

for number in range(1,10):
    print(f"Current value: {number}")

'''2.Try the above exercise using a while loop. You’ll 
need to define a counter and an appropriate stopping condition. 
And you’ll need to manually increment the counter after every loop.'''

counter= 1
while counter <= 10 :
    print('current value:',counter)
    counter= counter+1

'''3.Use nested loops to print the following output:

111111111
222222222
...
888888888
999999999
'''

new_line= ''
for i in range(1,10):
    for j in range(0,9):
        new_line += str(i)
    print(new_line)
    new_line=''


# 4.You are given a list of countries. For each country in the list find the length of each country:


countries = ['Thailand', 'Vietnam', 'Malaysia', 'UAE']

for country in countries:
    print(f"{country} contains {len(country)} letters!")

'''5. Given a list of tuples,use a new list, it removes people whose job titles containthe word "SQL" from the list. You can use the
 in operator to checkif a given job title contains the word "SQL". Use the following
 data containing employee names, job titles, and salaries:'''


new_hires = [('Mark Adams', 'SQL Analyst', 4000),
             ('Leslie Burton', 'HR Specialist', 2300),
             ('Dorothy Castillo', 'UX Designer', 3100)]

new_list=[]

for person in new_hires[:]:
    if not 'SQL' in person[1]: 
        new_list.append(person)  

print(new_list)

'''6.Use the iteration method you think is best for this exercise. Create a function named get_results_range(result_dict) that accepts the 
following dictionary and returns the difference between the best and worst exam results'''


result_dict = {
    'Dominic Vargas': 67,
    'Marion Riley': 89,
    'Candice White': 45,
    'Doreen Goodwin': 82,
    'Janet Hunter': 98,
    'Jaime Page': 32,
    'Neil Fernandez': 76,
    'Jana Frank': 28,
    'Adrienne Perkins': 98,
    'Rosa Mccarthy': 34
}

def get_results_range(result_dict):
    max_number = 0
    min_number = 100  # Assuming scores are between 0 and 100

    for score in result_dict.values():
        if score > max_number:
            max_number = score
        if score < min_number:
            min_number = score

    return max_number - min_number

x= (get_results_range(result_dict))
print(x)


'''7.We want to manufacture key rings with the car makes found in the people_cars dictionary below. The size of each key ring will depend 
on the number of letters in the car make name. Create the set named car_make_lengths and add all unique car make length values to it.
Then, print the following sentence:
There will be {x} different sizes of key rings.'''

people_cars = {'Adam': 'Volvo', 'Kate': 'BMW', 'Mark': 'BMW', 'Hannah': 'Ford', 'Max': 'Volvo', 'Celine':'Fiat'}

car_make_lenghts= set()

for car in people_cars.values():
    car_make_lenghts.add(len(car))
print(f"There will be ,{len(car_make_lenghts)}, different sizes of key rings")

