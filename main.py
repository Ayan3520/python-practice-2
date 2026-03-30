customer_name = input("Enter customer name: ")

subtotal = 0.0
count = 0

while True:
    item_name = input("Enter item name (or 'done' to finish): ")
    
    if item_name.lower() == 'done':
        break
        
    price = float(input("Enter price: "))
    subtotal += price
    count += 1

print("Customer : {customer_name.upper()}")
print("Items : {count}")
print("Subtotal : {subtotal} KZT")

hour = int(input("Enter current hour (0-23): "))
discount_rate = 0.0
label = ""

if 6 <= hour < 12:
    label = "Morning discount"
    discount_rate = 0.10  
elif 12 <= hour < 17:
    label = "No discount"
    discount_rate = 0.0 
elif 17 <= hour < 22:
    label = "Evening discount"
    discount_rate = 0.05  
else:
    print("Closed")
    exit()

discount_amount = subtotal * discount_rate
discounted_price = subtotal - discount_amount
tip = discounted_price * 0.10 
final_total = discounted_price + tip

print(f"Time period: {label}")
print(f"Discount: {discount_amount} KZT")
print(f"Tip (10%): {tip} KZT")
print(f"Total: {final_total} KZT")

print(f"Name uppercase: {customer_name.upper()}")
print(f"Name lowercase: {customer_name.lower()}")
print(f"Name length: {len(customer_name)}")

if customer_name[0].upper() == 'A' or customer_name[0].upper() == 'S':
    print("VIP customer")
else:
    print("Regular customer")
