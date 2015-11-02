# Zombie-rabbits

I forgot to copy the instructions for this one, so I'll have to recreate the 
word problem for it. This time, Dr. Boolean wants to infect some rabbits with 
a zombie virus. The rabbits are in pens, and the pens are set up in an 
m-by-n grid, and each pen has exactly one rabbit in it. Dr. Boolean will 
concoct a virus that has a certain strength, and each rabbit will have a 
certain amount of resistance against the virus. The strength of the virus will 
be denoted by the variable strength, and will be a positive integer from 1 to 
5000(? I think--can't remember the exact number). The resistance to the virus 
of each rabbit will be represented by a positive integer, also from 1 to 
5000(?). 

You will be given an array of length m, where each entry is an array of 
length n. The entry in position (i, j) will be the positive integer that is 
the resistence level of the rabbit in the pen with position (i, j). Dr. Boolean 
will then infect one rabbit--patient z. We are able to know which rabbit is 
patient z, and we will denote the coordinates of patient z by (x, y). If the 
strength of the virus is greater than or equal to the resistance of the rabbit, 
then patient z becomes a zombie rabbit. Than, patient z can infect the rabbits 
adjacent to it--left, right, up, or down, but not diagonally. If the strength 
of the virus is greater than or equal to the strength of those rabbits, then 
those rabbits become zombies. Then those rabbits and infect rabbits adjacent 
to them, and so on. 

You need to come up with a function answer(population, x, y, strength), where 
population is the array containing the resistances of the rabbits, (x, y) are 
the coordinates for patient z, and strength is the strength of the virus. The 
function needs to return an array with the same dimensions as population, with 
the (i, j)-th entry is -1 if that rabbit became infected, and is equal to the 
rabbit's resistance if it did not.
