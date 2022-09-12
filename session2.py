# friends = input("how many friends? ")
# pizzas = int(friends) *0.5
#
# print("you need {} pizzas for {} friends".format(pizzas, friends))

#for loops

# shopping_list = ["Oranges", "milk", "water"]
#
# for item in shopping_list:
#     print(item)
#
# for number in range(8):
#     print(number)
#
# for character in "Banana":
#     print(character)

##while loop
store_capacity = 5

while store_capacity > 0:
    print("Please come in. Spaces available: "+ str(store_capacity))
    store_capacity = store_capacity - 1

print("\nPlease wait for someone to exit the store")
