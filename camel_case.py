camel_case = input("camelCase: ")
snake_case = ""

for char in camel_case:
   if char.isupper():
     snake_case += "_" + char.lower()
else:
   snake_case += char

if snake_case.startswith("_"):
 snake_case = snake_case[1:]
 print("snake_case:", snake_case)