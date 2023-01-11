text = "Hello World"
new_list = text.split(" ")
rev_list = []
for item in new_list:
    print(item[::-1], end = " ")