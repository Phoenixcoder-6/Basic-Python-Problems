class check:
    def __init__(self,number):
        self.num=number
    
    def armstrong(self):
        num_str= str(self.num)
        length= len(num_str)
        total=0
        for i in num_str:
            total += int(i)**length
        
        return total== self.num
            
def main():
    a= check(153)
    
    if a.armstrong():
        print(f"{a.num} is an armstrong number..")
    else:
        print(f"{a.num} is not an armstrong number..")

if __name__=="__main__":
    main()
                