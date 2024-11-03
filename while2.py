total = 0
ticket_price = 100
max_people = 5
count = 0

while count < max_people:
    age = int(input())

    if(age) > 3:
        total += ticket_price
    
    count += 1

print(total)