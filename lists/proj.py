# find Number of Days Avove Average temparatire





numsDays = int(input("how many days Temparature"))
print(numsDays)
total = 0
temp =[]


for i in range(numsDays):
    nextDay = int(input( "DAY " + str(i+1) +"'s high Temp: "))
    temp.append(nextDay)
    total += temp[i]

avg = round(total/ numsDays, 2)

print(avg)

