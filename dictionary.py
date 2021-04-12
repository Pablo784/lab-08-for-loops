myData = {"effective top tube length": 515, "seat tube length": 500, "seat tube angle": 74.4, "head tube angle": 70.5, "stack": 513, "reach": 367, "standover height": 755}
myKeys = []
myValues = []
for k, v in myData.items():
    print("key:"  + str(k) + ", value:" + str(v))
    myKeys.append(k)
    myValues.append(v)

print("ALL KEYS:" +str(myKeys))
print("ALL VALUES:" +str(myValues))

# I edited this filed since the professor decided to go over the file in class
# on April 12th, 2021
