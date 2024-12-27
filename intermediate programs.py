import random
def displayclue(word,x):
    clue=""
    for i in range(0,len(word)):
        if i<x:
            clue=clue+word[i]
        else:
            clue+"_"
        clue=clue+" "
    print("Name of the country: "+clue.upper())
countries=countries = ["Australia","Brazil","Canada","Denmark","Egypt","France","Ghana","Haiti","India","Japan","Kenya","Lebanon","Madagascar","Nepal","Oman","Poland","Qatar","Rwanda","Singapore","Turkey","Uganda","Venezuela","Yemen","Zambia"]
country=random.choice(countries)
for i in range(1,len(country)+1):
    displayclue(country,i)
    guess=input("your guess?").title()
    if guess==country:
        print("Good guess!")
        break
else:
    print("Worng guess")
