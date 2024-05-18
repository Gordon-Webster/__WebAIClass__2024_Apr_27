fruits:list[str] = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# print(type(fruits))
for item in fruits:
    if 'b' not in item:
        print(item)