""" Adding and Removing Friends from Sets """

# revised set of friends to invite
invite = set(['Nestor', 'Amanda', 'Olivia'])

print('Verne invited? {}'.format('Verne' in invite))

invite.add('Verne')

print('Now is Verne invited? {}'.format('Verne' in invite))

invite.add('Olivia') # Don't see to worry about duplicates

invite.remove('Nestor')
# invite.remove('Nestor') # will throw exception as Nestor does not exist in list

print(invite.pop()) # remove a random element from the set and return it to the user
