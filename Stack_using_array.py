size = 3
array = [0] * size
top = -1

def push(value):
    global top, size
    if top >= size-1:
        print("Stack is overflow")
    else:
        top += 1
        array[top] = value

def pop():
    global top
    if top == -1:
        print("Stack is underflow")
    else:
        array[top] = 0
        top -= 1
        return array[top+1]

def peek():
    if top == -1:
        print("Stack empty")
    else:
        print(array[top])

push(5)
push(7)
push(10)
print(array[0:top+1])
push(100)
pop()
print(array[0:top+1])
peek()