""" A Functional Breakfast """

cheese = 'cheddar' # global var

def mix_and_cook():
    print('Mixing the ingredients')
    print('Greasing the frying pan')
    print('Pouring the mixture into a frying pan')
    print('Cooking the first side')
    print('Flipping it!')
    print('Cooking the other side')

def make_omelette(ingredient):
    # cheese = 'swiss' # local var with the same name as the global var cheese
    # the local variable is always used first
    # local, then global
    global cheese # create or access a global var
    cheese = 'swiss' # change the global var
    mix_and_cook()
    omelette = 'a {} omelette'.format(cheese)
    return omelette

def make_pancake():
    mix_and_cook()
    pancake = 'a {} pancake'.format(cheese)
    return pancake

def fancy_omelette(*ingredients):
    mix_and_cook()
    omelette = 'a fancy omelette with {} ingredients'.format(len(ingredients))
    return omelette

print(make_omelette('bacon')) # returns a swiss panckae
print(make_pancake()) # also returns swiss pancake!
