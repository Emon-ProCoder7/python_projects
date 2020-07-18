def ground_shipping(weight):
  flat_charge = 20
  if (weight <= 2):
    price = weight * 1.50
    return price + flat_charge
  elif (weight > 2) and (weight <= 6):
    price = weight * 3.00
    return price + flat_charge
  elif (weight > 6) and (weight <= 10):
    price = weight * 4.00
    return price + flat_charge
  elif (weight > 10):
    price = weight * 4.75
    return price + flat_charge

premium_ground_shipping = 125.00

def drone_shipping(weight):
  if (weight <= 2):
    price = weight * 4.50
    return price
  elif (weight > 2) and (weight <= 6):
    price = weight * 9.00
    return price
  elif (weight > 6) and (weight <= 10):
    price = weight * 12.00
    return price
  elif (weight > 10):
    price = weight * 14.75
    return price

# Recommendation function
def cheapest_shipping(weight):
  if (drone_shipping(weight) < premium_ground_shipping) and (drone_shipping(weight) < ground_shipping(weight)):
    price = drone_shipping(weight)
    return "Dear, your Cheapest Shipping - Drone Shippping & price: " + str(price) + "$"
  elif (drone_shipping(weight) > premium_ground_shipping) and (premium_ground_shipping < ground_shipping(weight)):
    price = premium_ground_shipping
    return "Dear, your Cheapest Shipping - Premium Ground Shipping & price: " + str(price) + "$"
  elif (drone_shipping(weight) > ground_shipping(weight)) and (premium_ground_shipping > ground_shipping(weight)):
    price = ground_shipping(weight)
    return "Dear, your Cheapest Shipping - Ground Shipping price: " + str(price) + "$"


#Code testing
print(cheapest_shipping(4.8))

print(cheapest_shipping(41.5))
