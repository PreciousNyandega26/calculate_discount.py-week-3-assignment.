def calculate_discount(price, discount_percent):
    "A function that calculates the final price after applying a discount."
    
    if discount_percent >=20:
       discount_amount = (discount_percent / 100)* price
       final_price = price - discount_amount
       return final_price
    else: 
       return price
    
#PROMPT THE USER TO ENTER THE ORIGINAL PRICE OF AN ITEM AND DISCOUNT PERCENTAGE
def calculate_discount(price, discount_percent):
   original_price = (input("Enter theoriginal price of the item:")) 
   discount_percent =(input("Enter the discount percentage:"))
   #CALL THE FUNCTION AND PRINT THE FINAL PRICE AND ORIGINAL PRICE
   if discount_percent >=20:
     final_price = calculate_discount(original_price, discount_percent)
     print("The final price after discount is:", final_price)
   else:
        print("The original price is:", original_price)






