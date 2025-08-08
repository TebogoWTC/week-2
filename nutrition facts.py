
fruits_calories = {
 "apple": 130,
 "avocado california": 50,
 "banana": 110,
 "cantaloupe": 50,
 "grapefruit": 60,
 "grapes": 90,
 "honeydew melon": 50,
 "kiwifruit": 90,
 "lemon": 15,
 "lime": 20,
 "nectarine": 60,
 "orange": 80,
 "peach": 60,
 "pear": 100,
 "pineapple": 50,
"plums": 70,
 "strawberries": 50,
 "sweet cherries": 100,
 "tangerine": 50,
 "watermelon": 80
 }
def main():
 fruit = input("Enter a fruit: ").strip().lower()
 if fruit in fruits_calories:
  print(f"One portion of {fruit} has {fruits_calories[fruit]} calories.")
 else:pass
if __name__ == "__main__":
 main()