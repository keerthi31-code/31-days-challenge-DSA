'''
Big-O, Big-Omega, Big-Theta
as the input becomes bigger, how much more work will the algorithm do

for i in range(n):
print(i)

n=10--loop runs 10 tyms
n=100 -- loop runs 100 tyms
n=1000 loop runs 1000 times

we use spcl mathematical notations to describe this growth
big O
big Omega-- Ω
big theta -- Θ

big -O 
tells upper bound -- at most
Ex: journey to college takes at most 60 miutes
it could take 30mins, 40mins, 50mins, 60mins
but it wont take more than 60mins
Atmost 60mins Big O
 algorithm takes at most n steps
 so -- O(n)


 3. Big Omega --- Ω
 Atleast
big omega tells us the lower bound
ex: journey takes aleast 20mins
it could take 20 mins, 30 mins, 40 mins, 60mins 
but it cannot take less than 20 mins
so algorithm takes at least n steps

so -- Ω(n)
 4. Big Theta --- Θ
the growth is tightly bounded
the upper bound and lower bound are the same
so Ω(n) ≤ work ≤ O(n)-- if both sides are n 
Θ(n)


easy trick
O     → At most
Ω     → At least
Θ     → Both







'''
print('keerthi')