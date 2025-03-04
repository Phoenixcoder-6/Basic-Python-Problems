""" 
#Using string slicing
def rev_string(string):
    string= string[::-1]
    return string

string="abcd"
res= rev_string(string)
print(res) 

"""
#Using loop

def rev_string(string):
    rev=""
    for i in string:
        rev= i+ rev
    return rev
    
string="abcd"
res= rev_string(string)
print(res) 
    
