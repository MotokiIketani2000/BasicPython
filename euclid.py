a = input("a の値を入力: ")
b = input("b の値を入力: ")

#TODO

s = int(a)
m = int(b)

def gcd_euclid(s, m):
    
    while m != 0:
        s, m = m, s % m
        
    return abs(s)


def independent(s, m):
    return gcd_euclid(s, m) == 1

print(gcd_euclid(s,m))
print(independent(s,m))


