import re
def extract_urls(text):
    # Regular expression pattern for URLs
    url_pattern = r'(https?://\S+|www\.\S+)'
    
    # Find all matches in the input string
    urls = re.findall(url_pattern, text)
    
    return urls

# Example input
string = input("Enter a string: ")

# Extract URLs from the string
urls = extract_urls(string)

# Print the extracted URLs
if urls:
    print("Extracted URLs:")
    for url in urls:
        print(url)
else:
    print("No URLs found in the string.")