""" A Stack of Bills to Pay """

# create a list to use as the stack
stack = list()

# add some bills to the stack
stack.append('bill1')
stack.append('bill2')

# remove the top bill to pay it
print(stack.pop())

# add two more bills to the stack
stack.append('bill3')
stack.append('bill4')

# remove bills from top to bottom
print(stack.pop())
print(stack.pop())
# print(stack.pop())

try:
    # del bill
    bill2 = stack.pop() # causes Indexerror exception
except Exception as e:
    print('Stack is empty: {}'.format(e))
else:
    print(bill2)

try:
    # del bill
    bill1 = stack.pop() # causes Indexerror exception
except Exception as e:
    print('Stack is empty: {}'.format(e))
else:
    print(bill1)
