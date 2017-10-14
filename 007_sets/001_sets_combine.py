""" Creating and Combining Sets of Friends """

# sets are unranked/unordered
# items in sets are unique (cannot have two 'Bills')

# merge sets with the union operater

college = set(['Bill', 'Katy', 'Verne', 'Dillon',
               'Bruce', 'Olivia', 'Richard', 'Jim'])

coworker = set(['Aaron', 'Bill', 'Brandon', 'David',
                'Frank', 'Connie', 'Kyle', 'Olivia'])

family = set(['Garry', 'Landon', 'Larry', 'Mark',
              'Olivia', 'Katy', 'Rae', 'Tom'])

print('Number of college friends is {}'.format(len(college)))

# union sets together to combine them
# if an item appears in two sets that are combined, they will only appear once
# in the final set as items are unique

friends = college.union(coworker, family)

print('All friends: {}'.format(friends))
