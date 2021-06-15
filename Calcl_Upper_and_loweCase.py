text = input("enter a sentence to get the number of upper case and lower case in it")
d = {"upper case": 0, "lower case": 0}
for cases in text:
    if cases.isupper():
        d["upper case"] += 1
    elif cases.islower():
        d["lower case"] += 1
    else:
        pass
print("the sentence", text, )
print("number of upper case", d["upper case"])
print("number of lower case", d["lower case"])
