""" Sorting Friends into Sets """

# set of all friends
friends = set(['Mark', 'Rae', 'Verne', 'Richard',
               'Aaron', 'David', 'Bruce', 'Garry',
               'Bill', 'Connie', 'Larry', 'Jim',
               'Landon', 'Dillon', 'Frank', 'Tom',
               'Kyle', 'Katy', 'Olivia', 'Brandon'])

# set of people who live in my zip code
zipcode = set(['Jerry', 'Elaine', 'Cindy', 'Verne',
                'Rudolph', 'Bill', 'Olivia', 'Jim',
                'Lindsay', 'Rae', 'Mark', 'Kramer',
                'Landon', 'Newman', 'George'])

# set of people who play Munchkin
munchkins = set(['Steve', 'Jackson', 'Frank', 'Bill',
                 'Mark', 'Landon', 'Rae'])

# set of Olivia's friends
olivia = set(['Jim', 'Amanda', 'Verne', 'Nestor'])

# intersect() function returns common elements between sets (IN)
# difference() function removes common elements between sets (NOT IN)

local = friends.intersection(zipcode) # find close friends
invite = local.difference(munchkins)    # remove local friends playing Munchkin
                                                # the argument is the set to remove from
                                                # the first set (order matters)
symdiff_invite = invite.symmetric_difference(olivia) # OR NOT AND
# set of elements in both A OR B except those that are common in both
# could this be done another way? e.g. union + intersection - difference?

print(symdiff_invite)
