# LOOPS

# For loop
people = ['John', 'Sara', 'Tim', 'Bob']
for person in people:
    print('Current Person: ', person)

# Iterate by squence index
for i in range(len(people)):
    print("Current Person: ", people[i])

for i in range(10):
    print(i)            # 0 - 9

for i in range(0, 10):
    print(i)

# While loop 

count = 0
while count <= 10:
    print('Count: ', count)
    count = count + 1