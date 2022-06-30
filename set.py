# a={1,2,3,4}
# b=3,4,5,None
# a.add(b)
# print(a)

# a={1,2,3,4};b={3,3,4,5};c={'helllo','python'};d={4,5,66,77}
# print(a.intersection(b))
# print(a.intersection(b))
# print(b.intersection(d))



# a={1,2,3,4};b={3,3,4,5};c={'helllo','python'};d={4,5,66,77}
# print(a.union(b))
# print(a.intersection(b))
# print(a.union(d))

# a={1,2,3,4};b={3,3,4,5};c={'helllo','python'};d={4,5,66,77}
# b.update(c)
# print(b)
 
# b={4,6,False,None}    #{false,none}
# a.difference(b)
# print(a-b)
# b.difference(a) 
# print(b-a)



# a={1,2,3,55}
# a.discard(77)
# print(a)

# a={1,2,3,55}
# a.pop()  #in set there is not specified index position
# print(a)


# a={1,2,3,4}
# b={5,6,7}                       #disjoint :   two sets have null intraction reports the dis joint
# c={4,5,6}
# print('Are a and b isdisjoint',a.isdisjoint(b))
# # print('Are a and c isdisjoint',a.isdisjoint(c))







# a={1,2,3,4,}
# b={1,2,3,4,5}
# c={1,3,5,}               #report where another contain this set
# print(a.issubset(b))
# print(b.issubset(a))
# print(c.issubset(b))


# a={1,2,3,4,5}
# b={3,4,2,6,7}
# a.difference_update(b)      # those both diffference and difference update both are show indivisual sets
# print(a)
# b.difference_update(a)
# print(b)

# a={1,2,3,4,5}
# b={3,4,2,6,7}
# a.symmetric_difference_update(b)      # it shows remainig both intersecion value in a sets
# print(a)

# a={1,2,3,4,5}
# b={3,4,2,6,7}
# a.intersection_update(b)                  #intersection ponts will be specified
# print(a)



# a={1,2,3,4,5}
# b={3,4,2,6,7}
# print(a.intersection(b))

# a={1,2,3,4,5}
# a.remove(4)
# print(a)

