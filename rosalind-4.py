''' rabbits and recurrence relations: given positive integers n ≤ 40 and k ≤ 5, returns the total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs, where the number of rabbit pairs alive after the nth month is defined by defined by the recurrence relation Fn = Fn1 + Fn2 (with F1 = F2 = 1 to initiate the sequence)
'''

f = open("rosalind_fib.txt", "r") 

a, b = f.readline().strip().split(" ")

def recur(n, k):
    if n < 2:
        return n
    else:
        return recur(n-1, k) + (recur(n-2, k) * k)

print(recur(int(a), int(b)))
