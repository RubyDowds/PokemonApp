# new_item = input("Enter a to-do item: ")
#
# with open('todo.txt', 'r') as todo_file:
#     todo = todo_file.read()
#
# todo = todo + new_item + "\n"
#
#
# with open('todo.txt', 'w+') as todo_file:
#     todo = todo_file.write(todo)

import csv
with open('trees.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
heights = []
for row in spreadsheet:
    tree_height = row['height']
heights.append(tree_height)
shortest_height = min(heights)
print(shortest_height)






