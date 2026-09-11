name = (input("John Loyd P. Mayao: "))
print("Hello," +name)

year = int(input("Enter a year: "))

result = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(result)