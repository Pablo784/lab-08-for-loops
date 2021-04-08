party_or_not = input("Let's party! How long until the party? (Give me a number.)")
party_or_not = int(party_or_not, 10)
if (party_or_not < 1):
    print("PARTY NOW!!!")
else:
    for i in range (party_or_not, 0, - 1):
        print(i)
        if (i == 1):
            print("PARTY TIME!")
