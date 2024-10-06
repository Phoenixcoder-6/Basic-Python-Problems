stack=[10,20,30]
print("Stack elements:")
print(stack)

#PUSH Operation
stack.append(40)
stack.append(50)
print("Stack elements after push operation...")
print(stack)

#POP Operation
print(stack.pop(), " is removed/popped...")
print(stack)

#TOP Operation
print("Stack TOP:", stack[-1])

if stack ==[]:
    print("Stack Underflow..")
else:
    print("Stack is not empty..")