from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.
print(products)


# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.
customer_preferences = []

response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    # Add the customer preference to the list
    customer_preferences.append(preference)
    response = input("Do you want to add another preference? (Y/N): ").upper()
  

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.

customer_tags = set(customer_preferences)

# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []
for product in products:
    converted_product = product.copy()
    converted_product["tags"] = set(product[tags])
    converted_products.append(converted_product)



# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
   product_tags = {}
   customer_tags = {}
   int = product_tags & customer_tags
    pass




# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
   matches = []

   for product in products:
    match_count = count_matches(product["tags"], customer_tags)
    matches.append({'name': product['name'], 'matches': match_count})

    matches.sort(key=lamda x: x["matches"],reverse=True
    return matches)
    pass



# TODO: Step 7 - Call your function and print the results
recommended = recommend_products(converted_products, customer_tags)

print("\nRecommended products:")
for product in recommended:
    print(f"{product['name']} - {product['matches']} matching tags")



# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
#    - We use loops to collect the customer’s preferences and to check each product’s tags.
#    - Converting tags to sets removes duplicates and makes it easy to compare them quickly.
#    - By finding the overlap between customer preferences and product tags, we can see how well each product matches.
#    - Sorting the products by number of matches puts the most relevant items at the top.
# 2. How might this code change if you had 1000+ products?
#    - Sets keep comparisons fast, even with hundreds or thousands of products.
#    - For very large collections, using a database or an indexed system could make matching quicker.