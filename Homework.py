#Write a program to check whether the given number is in between 1 and 100 or not

number=int(input("Enter a number"))

if number >=1 and number<=100:
    print("The number exists")
else:
    print("The number does'nt exist")

#2. Check whether the user input number is even or odd and  display it to user.
num=int(input("Enter a number"))
if (num % 2==0):
    print('It is even')
else:
    print("It is odd")

#3. Write a program that asks the user for a number  in the range of 1 to 12. 
#The program should display the corresponding month, where 
#1=january, 2=february,3=march,4=april,5=may,6=june,7=july, 
#8=august,9=september,10=october,11=november,12=december. The program should display an error 
#message if the user enters a number that is outside the range of 1 to 12.

month_number=int(input("Enter a month number"))
months={1:"january",2:"february",3:"march",4:"april",5:"may",6:"june",7:"july",8:"august",9:"september",10:"october",11:"november",12:"december"}
if month_number in months:
    print(months[month_number])
else:
    print("invalid month number")
# 4. A school has following rules for grading system:
 #       a. Below 25 - F
 #       b. 25 to 45 - E
  #      c. 45 to 50 - D
   #     d. 50 to 60 - C
     #   e. 60 to 80 - B
    #    f. Above 80 - A
      #  Ask user to enter marks and print the corresponding grade.
marks = int(input("Enter your marks: "))
if marks>=80 and marks<=100:
    print("Grade=A")
elif marks>=60 and marks<80:
    print("Grade=B")
elif marks>=50 and marks<60:
    print("Grade=C")

elif marks>=45 and marks<50:
    print("Grade=D")
elif marks>=25 and marks<45:
    print("Grade=E")
else :
    print("Grade=F")

#5. Write a program to check whether a number is divisible by  7 or not.
numberr=int(input("Enter your number: "))
if (numberr%7==0):
    print("It is divisible by 7")
else:
    print("It is not divisible by 7")
#6. Write a program to accept two numbers and mathematical operators and  perform operation accordingly.
num1=int(input("Enter your first number: "))
num2=int(input("Enter your second number: "))
operator=(input("Enter your operator: "))
if operator == "+":
    print(num1+num2)
elif operator=="-" :
    print(num1-num2)
elif operator== "/" :
    print(num1/num2)
elif operator== "*" :
    print(num1*num2)
    
else: 
    print("Invalid operator5")

#7. Write a Python program to check car loan eligibility:Salary >= 50,000 and Credit Score >= 700: "Eligible"
# Otherwise: "Not Eligible"
salary = float(input("Enter your salary: "))
credit_score = int(input("Enter your credit score: "))

if salary >= 50000 and credit_score >= 700:
    print("Eligible for car loan")
else:
    print("Not Eligible for car loan")

 #8. Write a Python program that takes an integer input n n. From given number, 
#check if it is divisible by both 3 and 5, and print "FizzBuzz" if true. 
# If the number is divisible only by 5, print "Buzz." If it is divisible only by 3, print "Fizz." 
#Finally, if the number is not divisible by either 3 or 5, print the number itself.

n= int(input("n: "))
if (n%3==0 and n%5==0) :
    print("FizzBuzz")
elif (n%3==0):
    print("Fizz")
elif (n%5==0):
    print("Buzz")
else :
    print(n)

#9. Write a Python program that takes a character input and checks whether it is a vowel or consonant.
character=str(input("Enter your character: "))
if character==('a','e','i','o','u'):
    print('It is a Vowel')
else :
    print("It is consonant")

#10. Write a Python program to input marks and determine the grade based on the following conditions:
#90-100: A
#80-89: B
#70-79: C
#Below 70: Fail
marks=float(input("Enter your marks: "))
if (marks>=90 and marks<=100):
    print("Grade=A")
elif (marks>=80 and marks<90):
    print("Grade=B")
elif(marks>=70 and marks<=79):
    print("Grade=C")
elif (marks)<70 :
    print("Fail")
else :
    print("Invalid marks")

#11. Write a Python program to categorize a person’s age:
#Age < 13: Child
#13 <= Age <= 19: Teenager
#Age > 19: Adult
age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")
else:
    print("Adult")

#12.Write a Python program to check if a given character is uppercase, lowercase, or a digit.

character= input("Enter a single character: ")

if character.isupper():
    print("It is Uppercase letter")
elif character.islower():
    print("It is Lowercase letter")
elif character.isdigit():
    print("It is a Digit")
else:
    print("Invalid input")

#13. Write a Python program that takes a color as input ("Red", "Yellow", "Green") and
#  outputs the corresponding action ("Stop", "Get Ready", "Go").

color = input("Enter a color (Red, Yellow, Green): ")

if color == "Red":
    print("Stop")
elif color == "Yellow":
    print("Get Ready")
elif color == "Green":
    print("Go")
else:
    print("Invalid color")

#14. Write a Python program to check eligibility for a job based on age and experience:
#Age > 18 and Experience >= 2 years: Eligible
#Otherwise: Not Eligible

age = int(input("Enter your age: "))
experience = int(input("Enter your years of experience: "))

if age > 18 and experience >= 2:
    print("Eligible")
else:
    print("Not Eligible")

#15. Write a Python program to give advice based on the temperature:
#Temperature > 30°C: "It's hot, stay hydrated!"
#Temperature between 15-30°C: "Enjoy the weather!"
#Temperature < 15°C: "It's cold, wear warm clothes!"

temperature = float(input("Enter the temperature in °C: "))

if temperature > 30:
    print("It's hot, stay hydrated!")
elif 15 <= temperature <= 30:
    print("Enjoy the weather!")
else:
    print("It's cold, wear warm clothes!")

#16. Write a Python program that takes a menu option ("Pizza", "Burger", "Pasta") and prints its price:
#Pizza: $10
#Burger: $7
#Pasta: $8

items = input("Enter a menu item (Pizza, Burger, Pasta): ")

if items == "Pizza":
    print("Price: $10")
elif items == "Burger":
    print("Price: $7")
elif items == "Pasta":
    print("Price: $8")
else:
    print("Not availabe in menu option")


#17. Write a Python program to select players based on height:
#Height >= 6 feet: Selected
#Height < 6 feet: Not Selected

height = float(input("Enter height in feet: "))

if height >= 6:
    print("Selected")
else:
    print("Not Selected")

#18. Write a Python program to check if a person is eligible to watch a movie based on their age:
#Age >= 18: Allowed
#Age < 18: Not Allowed

Age=int(input("Age: "))
if Age>=18 :
    print("You are allowded to watch the movie")
else:
    print("You are not allowded to watch the movie")

#19. Write a Python program to check login credentials:
#Username: "admin", Password: "password123"
#If correct, print "Access Granted"; otherwise, print "Access Denied."

Username=input("Enter your Username: ")
Password=input("Enter your Password: ")

if Username==("admin") and Password==("password123"):
    print("Access Granted")
else :
    print("Access Denied")

#20. Write a Python program that takes a month number (1–12) and outputs the corresponding season:
#12, 1, 2: "Winter"
#3, 4, 5: "Spring"
#6, 7, 8: "Summer"
#9, 10, 11: "Autumn"

month=input("Enter your month number: ")
if month==('12','1','2'):
    print("Winter")
elif month in [3, 4, 5]:
    print("Spring")
elif month in [6, 7, 8]:
    print("Summer")
elif month in [9, 10, 11]:
    print("Autumn")
else:
    print("Invalid month number")
    