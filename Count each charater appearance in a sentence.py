text1 = "Hello World"
text = text1.replace(" ", "")
new_list =[]
for item in text:
    new_list.append(item)
print(new_list)
unique_list = []
for item1 in new_list:
    if item1 not in unique_list:
        unique_list.append(item1)
        val = new_list.count(item1)
        val = str(val)
        print(item1 + " = " + val)
    else:
        continue