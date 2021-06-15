str = input("enter a sentence")

d = {}
for word in str.replace(" ",''):
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
for keys,values in d.items():
    print(keys,":",values)
