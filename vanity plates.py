def starts_with_two_letters(s):
 return len(s) >= 2 and s[0].isalpha() and s[1].isalpha() 

def numbers_at_end(s):
 
 if not any(char.isdigit() for char in s):
   return True
first_digit_index = next(i for i, char in enumerate(s) if char.isdigit())
return s[first_digit_index:].isdigit()


def no_zero_start(s):
 
 if any(char.isdigit() for char in s):
    first_digit = next(char for char in s if char.isdigit())
 return first_digit != '0'
 return True

 def length_valid(s):
  return 2 <= len(s) <= 6

 def is_valid(s):
  return (starts_with_two_letters(s) and
 numbers_at_end(s) and
 no_zero_start(s) and
 length_valid(s))

 def main():
  plate = input("Plate: ")
 if is_valid(plate):
  print("Valid")
 else:
  print("Invalid")
if __name__ == "__main__":
 main()