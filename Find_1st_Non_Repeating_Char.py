# find the first non-repeating character in a string

str = "aabbcddeff"
# str = input("Enter a string: ")

for i in str:
    if str.count(i)<2:
        print(i)
        break