# reverse only vowels in a string
# Hint: use 2 pointers

vowels = "aeiou"
str = "hello"

lst = []

for i in str:
    if i in vowels:
        lst.append(i)
        
for i in str:
    if i in lst:
        str.replace(i,lst[i+1])
        
print(str)