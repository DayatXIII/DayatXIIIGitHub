import datetime

currentDate = datetime.date.today()

#print(currentDate)
#print(currentDate.strftime("%d %B %Y"))
#print(currentDate.day)
#print(currentDate.month)
#print(currentDate.year)

#userInput = input("Please enter your birthdate (dd/mm/yyyy)")
#birthDate = datetime.datetime.strptime(userInput, "%d/%m/%Y").date()
birthDate = datetime.datetime.strptime("19/11/1986", "%d/%m/%Y").date();

days = currentDate - birthDate
print(currentDate)
print(days.days)