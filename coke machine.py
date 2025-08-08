amount_due = 50
while amount_due > 0:
 print(f"Amount due: {amount_due} cents")
 coin = int(input("Insert a coin: "))
if coin in [25, 10, 5]:
 amount_due-= coin
 if amount_due < 0:
  print(f"Change owed: {-amount_due} cents")
 else:
  print("Change owed: 0 cents")