import re

#print command displays a message on the screen

#print("Hello World")
#print("Hello Python")

#print("""Hello World 
#Hello Python""")

#print("Hello World \nHello Python")

#print("What is your first name?");
#firstName = input();
#print("What is your last name?");
#lastName = input();
#print("So your name is " + firstName + " " + lastName + "?");

area = 0;
height = 10;
width = 20;
area = height * width /2;
print("The area of the triangle would be %.2f" % area);
print("The first number is {0:d}, + \
the second number is {1:d}, + \
the third number is {2:d}".format(10, 20, 30))

mystring = "Hello!!!, he<> sa(id) --and @went &"
mystring = re.sub("[!,<>()-@&]", "", mystring)

print(mystring)