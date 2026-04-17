word = input("Введите слово из маленьких латинских букв: ")

vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0} #гласные
consonants = 0 #согласные

for idk in word:
    if idk in vowels:
        vowels[idk] += 1
    else:
        consonants += 1

total_vowels = sum(vowels.values())

print("Гласных букв: " + str(total_vowels))
print("Согласных букв: " + str(consonants))

print("Буква 'a': " + ("False" if vowels['a'] == 0 else str(vowels['a'])))
print("Буква 'e': " + ("False" if vowels['e'] == 0 else str(vowels['e'])))
print("Буква 'i': " + ("False" if vowels['i'] == 0 else str(vowels['i'])))
print("Буква 'o': " + ("False" if vowels['o'] == 0 else str(vowels['o'])))
print("Буква 'u': " + ("False" if vowels['u'] == 0 else str(vowels['u'])))