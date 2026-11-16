
stack = []

def push():
    element = input("Enter the element to push: ")
    stack.append(element)
    print(element, "is pushed into the stack")

def pop():
    if not stack:
        print("Stack is empty. Cannot pop!")
    else:
        print(stack.pop(), "is popped from the stack")

def peek():
    if not stack:
        print("Stack is empty")
    else:
        print("Top element is:", stack[-1])

def display():
    if not stack:
        print("Stack is empty")
    else:
        print("Stack elements:", stack)

def findSize():
    if not stack:
        print("Stack is empty")
    else:
        print("Size of the stack is:", len(stack))

def stackOps():
    while True:
        print("\n----- STACK OPERATIONS -----")
        print("1. Append at the end")
        print("2. Remove from the end")
        print("3. Display Top Element")
        print("4. Display whole stack")
        print("5. Find Size")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            push()
        elif choice == 2:
            pop()
        elif choice == 3:
            peek()
        elif choice == 4:
            display()
        elif choice == 5:
                findSize()
        elif choice == 6:
            print("Exiting Stack Program")
            break
        else:
            print("Invalid choice!")


stackOps()
