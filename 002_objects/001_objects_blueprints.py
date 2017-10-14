""" The Blueprints for Jeans """

class jeans:

    def __init__(self, waist, length, color):
        # init method is a constructor method called when a new object is created
        # it is being overridden here with a custom constructor method that
        # allows for more args

        # self is a reference to the object being acted upon and allows for accessing
        # and modifying that object from within the method (class function = method)
        self.waist = waist
        self.length = length
        self.color = color
        self.wearing = False

    def put_on(self):
        print('Putting on {}x{} {} jeans'.format(self.waist, self.length, self.color))
        self.wearing = True


    def take_off(self):
        print('Taking off {}x{} {} jeans'.format(self.waist, self.length, self.color))
        self.wearing = False

my_jeans = jeans(31, 32, 'blue')

print(type(my_jeans))
print('-' * 120)
print(dir(my_jeans))
print('-' * 120)
print(my_jeans.wearing)
print('-' * 120)
my_jeans.put_on()
print('-' * 120)
print(my_jeans.wearing)
