def linear(arr,target):
    for index,element in enumerate(arr):
        if element == target:
            return index
        else:
            pass

if __name__=='__main__':
    arr=[4,2,3,7,8,9,34]
    t=67
    print("The element present at:" , linear(arr,t))