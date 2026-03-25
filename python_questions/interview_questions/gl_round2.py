# 🔹 Quick Summary
# All three (d, e, f) end up having the same data:

# same keys → a, b, c
# same values → 1, 2, 3 (some are float like 1.0, but that’s fine)

# In Python:

# order in dictionaries doesn’t matter
# 1 == 1.0 is considered equal

# So even though they were created differently, Python sees them as the same.

# Final result:

# True

# Short takeaway:
# Dictionaries are equal if keys and values match, order doesn’t matter, and int/float values are treated equal if same.


# all are creating dictionary only
d, e, f = {},dict(),dict(())

# d = {'a': 1.0, 'b': 2.0, 'c': 3.0} 
d['a'] = 1.0; 
d['b'] = 2.0; 
d['c'] = 3.0

# e = {'b': 2.0, 'c': 3.0, 'a': 1.0}
e = dict([('b',2/1), 
     ('c',3/1),
     ('a', 1/1)])


f = dict(zip(['c','a','b'], 
          [3, 1, 2]))
print(d==e and e==f and d==f)

# so final answer will be True