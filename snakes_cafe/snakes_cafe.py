print("*" * 38)
print("""**   Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **""")
print("*" * 38)

print(
  """
  Appetizers
  ----------
  Wings
  Cookies
  Spring Rolls

  Entrees
  ----------
  SalmonSteak
  Meat Tornado
  A Literal Garden

  Dessert
  ----------
  Ice Cream
  Cake
  Pie

  Drinks
  ----------
  Coffee
  Tea
  Unicorn Tears
  """
)

print("*" * 38)
print("** What would you like to order? **")
print("*" * 38)

order = input(">")

myOrder = {}
while order != "quit":
  if order not in myOrder:
    myOrder[order] = 0
  print(f"** {myOrder[order]} order of {order} have been added to your meal **")
  order = input(">")
