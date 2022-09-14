shopping_list=["milk","pasta","eggs","spam","rice","pizza"]
# for item in shopping_list:
#     if item!="spam":
#         print("Buy "+ item)

for item in shopping_list:
    if item=="spam":
        continue #It will skip the full block code of for loop and will continue with the next iteration
    print("Buy "+item)
print()
for a in shopping_list:
    if a!="spam":
        print("buy "+ a)