word = input("enter the sentence.")
listmaker = word.split()
print(listmaker)

reverselist = []
for n in range(len(listmaker)-1,0,-1):
    reverselist.append(listmaker[n])
print(reverselist)

revese_word = ""
for w in reverselist:
    revese_word += w
    print("end=")
print(revese_word)