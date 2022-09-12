#4.1
# clothes = [
#     "shorts",
#     "shoes ",
#     "tshirt "
# ]
# if clothes[0] == "shorts":
#     clothes[0] = "warm coat"
#
# print(clothes)

#4.2
# scores = [3, 6, 9, 10, 50, 75, 125, 150, 200]
#
# print("Number of scores: {}".format(len(scores)))
# print("Highest score: {}".format(max(scores)))
# print("Lowest score: {}".format(min(scores)))

#4.6
# fruits = [
#     {'name': 'apple', 'colour': 'red', 'price': 0.12},
#     {'name': 'banana', 'colour': 'yellow', 'price': 0.2},
#     {'name': 'pear', 'colour': 'green', 'price': 0.19},
# ]
#
# for fruit in fruits:
#     print(fruit['name'], fruit['colour'], fruit['price'])

#4.7
import random
first_names = ["ruby", "annie", "lucy"]
last_names = ["dowds", "kennedy", "cook"]

random_name = random.choice(first_names) + random.choice(last_names)
print(random_name)