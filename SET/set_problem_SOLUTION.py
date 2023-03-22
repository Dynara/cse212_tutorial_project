# SET SOLUTION
hobbit = {'Bilbo', 'Thorin', 'Smaug', 'Witch-king of Angmar', 'Elrond', 'Galadriel', 'Gandalf', 'Gollum', 'Thranduil', 'Legolas', 'Saruman'}
lord_or_the_rings = {'Aragorn', 'Arwen', 'Elrond', 'Bilbo', 'Boromir', 'Gollum', 'Frodo', 'Galadriel', 'Gandalf', 'Legolas', 'Saruman', 'Witch-king of Angmar'}

# Find what characters were in both hobbit and lord of the rings
print(hobbit.intersection(lord_or_the_rings))
#Output: {'Galadriel', 'Gandalf', 'Elrond', 'Bilbo', 'Witch-king of Angmar', 'Legolas', 'Gollum', 'Saruman'}

# Find out what characters were in either hobbit or lord of rings, not both
print(hobbit.symmetric_difference(lord_or_the_rings))
#Output: {'Boromir', 'Smaug', 'Arwen', 'Aragorn', 'Thranduil', 'Thorin', 'Frodo'}

# Add Bard to hobbit
hobbit.add('Bard')

# Remove Gollum from lord of the rings and add Smeagol
lord_or_the_rings.remove('Gollum')
lord_or_the_rings.add('Smeagol')

# Print characters that were in both hobbit and lord of the rings
print(hobbit.intersection(lord_or_the_rings))
#Output: {'Galadriel', 'Legolas', 'Bilbo', 'Gandalf', 'Elrond', 'Witch-king of Angmar', 'Saruman'}


