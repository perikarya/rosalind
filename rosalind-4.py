f = open("rosalind_fib.txt", "r") 

a, b = f.readline().strip().split(" ")

def recur(n, k):
    if n < 2:
        return n
    else:
        return recur(n-1, k) + (recur(n-2, k) * k)

print(recur(int(a), int(b)))
