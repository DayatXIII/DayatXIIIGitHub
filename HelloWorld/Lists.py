#Lists in Python
guests = ["Dayat", "Mizah", "Cloud", "Squall"]
scores = [52,68,45,30,89]

#update lists
guests[0] = "DayatXIII"

#append lists
guests.append("Rinoa")

#remove lists
guests.remove("Squall")

#delete lists
del guests[2]

#print item in the last index
print(guests[-1])

#looping thru a list
for steps in range(3) :
    print(guests[steps])

#Looping thru a list
lengthValueInList = len(guests)
for steps in range(lengthValueInList) :
    print(guests[steps])

#Looping thru a list
for totalGuests in guests :
    print(totalGuests)