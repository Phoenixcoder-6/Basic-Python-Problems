str= input("Enter any string:")
def count_length(str):
    str=str.split(" ")
    for word in str:
        print(word,"(",len(word),")")
count_length(str)