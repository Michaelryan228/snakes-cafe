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

my_order = {}
while order != "quit":
  if order not in my_order:
    my_order[order] = 0
  my_order[order] += 1
  print(f"** {my_order[order]} order of {order} have been added to your meal **")
  order = input(">")
