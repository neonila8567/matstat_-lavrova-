import numpy as np
np.random.rand(5)
print(np.random.rand(5))
A= np.random.rand(5)
B=[4, 432, 7, 90, 2]
add=[a+b for a, b in zip(A, B)]
sub=[a-b for a, b in zip(A, B)]
mul=[a*b for a, b in zip(A, B)]
div=[a/b for a, b in zip(A, B)]
print("A + B =", add)
print("AB=", sub)
print("A B =", mul)
print("A / B =", div)
C=A+B
min_= min(C)
max_= max(C)
sum_= sum(C)
print(min_)
print(max_)
print(sum_)
product = 1
for x in C:
    product *= x
print ("Добуток:", product)