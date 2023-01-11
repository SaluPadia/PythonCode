text = "Hello World"
word = " "
result = " "
for i in (text + " "):
    if i == " ":
        if word:
            result = result + " " + word
            word = " "
    else:
        word = i+ word
print(result)