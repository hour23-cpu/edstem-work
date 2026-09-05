'''
Structure Chart:
main
│
├── get_input()
│   ├── Get weight of the shipping
│   └── Get the zone
│
├── calculate_shipping_quote(weight, zone)
│   ├── Calculate number of 0.5 kg units which multiply by 2
│   ├── Calculate shipping cost
│   └── Apply zone multiplier from the input of users
│├──Print out the amount that should pay
    └── Display final shipping'''
import math
base_fee = 5
each_part_cost = 2 #0.5kg=2$ 
Zone_A = 1
Zone_B = 1.2
Zone_C = 1.5
def get_weight():
    weight= float(input("Enter the weight of the box in kg: "))
    weight = math.ceil(weight/0.5) * 0.5
    return weight
def zone_cost(zone):

    if zone == "A":
        cost = Zone_A
        return Zone_A
    elif zone == "B":
        cost = Zone_B
        return Zone_B
    elif zone == "C":
        cost = Zone_C
        return Zone_C
    else:
        print("Invalid zone. Please enter A, B, or C.")
        return None
def calculate_shipping_cost(weight, zone):
    if zone_cost(zone) is not None:
        shipping_cost = base_fee + ((weight * each_part_cost) * zone_cost(zone))
        return shipping_cost
    else:
        return None
def main():
    weight = get_weight()
    zone = input("Enter the shipping zone (A, B, or C): ")
    shipping_cost = calculate_shipping_cost(weight, zone)
    if shipping_cost is not None:
        print(f"The shipping cost for a {weight} kg box to zone {zone} is: ${shipping_cost:.2f}")

main()