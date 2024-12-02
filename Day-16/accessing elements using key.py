def find(dictionary, key):
    if not key:  # Check if the input is empty
        return "Invalid input!!"
    # Search for the key in the dictionary
    return dictionary.get(key, "Key not found.")

# Input the number of elements for the dictionary
n = int(input("Enter the number of elements in the dictionary: "))
sample_dict = {}

# Create the dictionary
for _ in range(n):
    k = input("Enter key: ")
    v = input("Enter value: ")
    sample_dict[k] = v

print("\nDictionary created:", sample_dict)

# Search for a key
search_key = input("\nEnter a key to search: ")
result = find(sample_dict, search_key)
print(f"Result: {result}")
