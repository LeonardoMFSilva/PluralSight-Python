acronyms = ['LOL', 'IDK', 'SMH', 'TBH', 'BFN']

word = "BFN"

acronyms.remove("BFN")
print(acronyms)


if word in acronyms:
   print(word + " is in the list")
else:
    acronyms.append(word)
    print(word + " was not is in the list but, was added to the list: ")
    print(acronyms)

for acronym in acronyms:
    print(acronym)