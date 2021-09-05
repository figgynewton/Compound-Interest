Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> principal = float(input("Enter the amount of principal amount to be deposited: " ))
Enter the amount of principal amount to be deposited: 23.46
>>> rate = float(input("Enter annual interest rate paid by the account: " ))
Enter annual interest rate paid by the account: 5
>>> num = int(input("Enter the number of times per year that the interest is compunded: " ))
Enter the number of times per year that the interest is compunded: 3
>>> years = float(input("Enter the number of years the account will be left to earn interest: " ))
Enter the number of years the account will be left to earn interest: 45
>>> amount = principal*(1+(rate/100)/num)**(num*years)
>>> print("The amount of money that will be in your account after ", years, "years:", round(amount,2))
The amount of money that will be in your account after  45.0 years: 218.49
>>> 
