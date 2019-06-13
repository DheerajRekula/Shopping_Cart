# shopping_cart.py


products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#print(products)


# prompt the checkout clerk to input the identifier of each shopping cart item, one at a time. 
# When the clerk enters DONE, process payment
# If product id is not found, ask the user to add a correct entry

###########################
# CODE

def to_usd(dollar_amt):
    return "${0:,.2f}".format(dollar_amt)

def calc_tax(product_total):
    tax_percent = 8.73                     # TODO: This is in main script. Can i put it in a different script?
    tax_amt = product_total * tax_percent/100
    return tax_amt

def calc_total_bill_amt(product_total, tax_percent = 8.73):    #TODO:This is in main script. Can i put in in a different script?
    return product_total + (product_total * tax_percent)
    
    
# STEP 1: TAKE INPUTS AND PRINT THEM
selected_products = []
total_price = 0
while True:
    input_id = input("Please input a product identifier:")  

#TODO: What if the user enters DOne or DONE
#TODO: What if the user enters someother text string
#TODO: WHat if the user enters a number that is not available in the list
    if input_id == "Done":
        break
    else:
        selected_products.append(input_id)

print("-------------------------------------------------")
print("SELECTED PRODUCTS")
for selected_product in selected_products:
    product_match = [p for p in products if str(p["id"]) in str(selected_product)]
    total_price = total_price + product_match[0]['price']
    #product_price = "${0:,.2f}".format(product_match[0]['price'])
    product_price = to_usd(product_match[0]['price'])

    #print(product_match[0]['price'])
    print(f"... {product_match[0]['name']} ({product_price})")

print("-------------------------------------------------")
#STEP 2: PRINT SUBTOTAL AND GRAND TOTAL
#print(f"SUBTOTAL = {total_price}")
product_tot_amt = to_usd(total_price)
product_tot_tax = to_usd(calc_tax(total_price))
product_grand_tot = to_usd(calc_total_bill_amt(total_price))
#print(f"SUBTOTAL = {to_usd(total_price)}")
print(f"SUBTOTAL = {product_tot_amt}")
print(f"TAX = {product_tot_tax}")
print(f"TOTAL = {product_grand_tot}")
print("-------------------------------------------------")
print("Thanks, SEE YOU AGAIN SOON!")
print("-------------------------------------------------")


#selected_product = [p for p in products if str(p["id"]) == str(input_id)]
#print(type(selected_product))

#print(f"...{selected_product[0]['name']} ({product_price})")
#selected_list.append(input_id)
#print(selected_list)
#selected_product = [p for p in products if str(p["id"]) == str(input_id)]
#print()

# USED THE SELECTED PRODUCTS TO FILTER VALUES FROM THE PRODUCTS LIST


'''
# list of product ids
product_id = [i["id"] for i in products]
#print(product_id)
cust_product = []

while True:
    print(product_id)
    p_id = input("Enter the product id:")

    
    if p_id in product_id:
        cust_product.append(p_id)
    elif p_id == "Done":
        exit()
    else:
        print("You have entered an incorrect product code. Enter Again")


'''