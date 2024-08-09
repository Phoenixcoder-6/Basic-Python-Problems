string = input("Enter the string: ")
words = string.split(" ")
k = int(input("Enter the minimum length of the word: "))

largerStrings = []
for word in words:
    if len(word) > k:
        largerStrings.append(word)

# Print the list of words longer than k
print("Words longer than", k, "characters:", largerStrings)
