def string_finding(arr,stri):
    arr_str=''.join(arr)

    if stri in arr_str:
        print(f"The series '{stri}' found in given array string.")
    else:
        print(f"The series '{stri}' not found in that given array.")


arr= list(input("Enter the characters for the array (no spaces): "))
stri = input("Enter the series to find: ")
string_finding(arr, stri)





    
