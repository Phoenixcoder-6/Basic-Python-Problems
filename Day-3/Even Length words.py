str=input("Enter the string:")

def even_length(str):
    str=str.split(" ")
    for words in str:
        lg= len(words)
        if (lg%2 == 0):
            print(words,"Even","(",len(words),")")

even_length(str)
