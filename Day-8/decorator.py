def car(start,stop):
    if (start>0):
        print("car started..")
    else:
        print("car stopped..")


def smart_car(func):
    def inner(start,stop):
        if (start>=4 and start<=10):
            print("No need bbreaks")
        else:
            print("Break needed..")
    return inner

car= smart_car(car)

car(40,8)
