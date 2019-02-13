# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     if item == "spam":
#         # print("item ignoring is " + item)
#         continue
#         # break
#     print("Buy " + item)
# 2. another scenario
meal = ["egg", "bacon", "spam", "sausages"]
# nasty_food_item = ''
for item in meal:
    if item == "spam":
        nasty_food_item = item
        break
else:
    nasty_food_item = ''
    print("I'll have a plate of that, then , please")

if nasty_food_item == 'spam':
    print("Can't I have anything without spam in it")