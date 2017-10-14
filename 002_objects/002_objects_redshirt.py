""" Two Names, One Shirt """

class shirt:

    def __init__(self):
        self.clean = True

    def make_dirty(self):
        self.clean = False

    def make_clean(self):
        self.clean = True


red = shirt()
crimson = red

print('Red shirt: {}'.format(id(red)))
print('Crimson shirt: {}'.format(id(crimson)))

print('Red clean: {}'.format(red.clean))
print('Crimson clean: {}'.format(crimson.clean))

print('Spilling juice on red shirt')
red.make_dirty()

print('Red clean: {}'.format(red.clean))
print('Crimson clean: {}'.format(crimson.clean))

print('Washing crimson')
crimson.make_clean()

print('Red clean: {}'.format(red.clean))
print('Crimson clean: {}'.format(crimson.clean))

print('Red shirt is crimson shirt: {}'.format(red is crimson))

print('Creating a new crimson shirt')
crimson = shirt()

print('Red shirt is crimson shirt: {}'.format(red is crimson))

print('Red shirt: {}'.format(id(red)))
print('Crimson shirt: {}'.format(id(crimson)))

print('Red clean: {}'.format(red.clean))
print('Crimson clean: {}'.format(crimson.clean))

print('Spilling juice on red shirt')
red.make_dirty()

print('Red clean: {}'.format(red.clean))
print('Crimson clean: {}'.format(crimson.clean))

print('Washing crimson')
crimson.make_clean()

print('Red clean: {}'.format(red.clean))
print('Crimson clean: {}'.format(crimson.clean))

print('Red shirt is crimson shirt: {}'.format(red is crimson))
