# question 1
student=['sachin','alex','herman','joe','kareem','frank']
print(student[1])
print(student[-1])


# question 2

foods=('apple','banana','orange','grape','watermelon','kiwi')
for food in foods:
    print(food  + " is a good food")

# question 3

for i in range(-2,0):
    print( foods[i] )
    

# question 4

home_town = {
    "city":'mangaf',
    "state":'fahaheel',
    "population":'1000000'
}
x=home_town["city"]
y=home_town["state"]
z=home_town["population"]
print("I was born in "+ ( x )  +", " + ( y ) + " - population of " + ( z ))



# question 5
for key, value in home_town.items():
    print(key,value)


# # question 6

cohort = []
for name in cohort:
    cohort.append('student':'tina')
# a={'student': 'Tina'}
# cohort.append(dict(a))
# print(cohort)

# for quantity in foods.items():
    
#     cohort.append([foods]*quantity)

# print(fruits_list)



# question 7
awesome_students= student
print(awesome_students)
