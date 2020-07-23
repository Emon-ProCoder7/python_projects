# Creating Menu System Class

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return "Name of The Menu: {},\nAvailable from: {}'o clock to {}'o clock".format(self.name, self.start_time, self.end_time)

  def calculate_bill(self, purchased_items):
    bill = 0
    for each in self.items:
      for food in purchased_items:
        if food == each:
          bill += self.items[food]
    return bill

# Menu Objects
brunch = Menu("brunch", {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, 11, 16)


early_bird = Menu("Early Bird", {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, 15, 18)


dinner = Menu("dinner",{
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, 17, 23)


kids = Menu("dinner",{
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, 11, 21)


# Testing Instance
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))










# Franchaise System

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus


  def __repr__(self):
    return "Address is: {}".format(self.address)


  def available_menus(self, time):
    for menu in self.menus:
      if (time >= menu.start_time) and (time <= menu.end_time):
        return "Available Items are: {}".format(list(menu.items))    


# Franchaise Objects
flagship_store = Franchise("1232 West End Road", (brunch, kids, dinner, early_bird))

new_installment = Franchise("12 East Mulberry Street", (brunch, kids, dinner, early_bird))


# Testing Franchaise Instance
print(new_installment.available_menus(17))








# Creating Business Class

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchise = franchises


# Business Instance
basta_fazoolin = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])


# Another Business

# Menu Object
arepa_menu = Menu("arepa menu", {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, 10, 20)

# Franchaise Object
arepas_place = Franchise("189 Fitzgerald Avenue", arepa_menu)

# Business Object
take_a_arepa = Business("Take a Arepa", [arepas_place])
