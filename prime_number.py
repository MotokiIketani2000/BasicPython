a = int(input("aの値を入力: "))
b = int(input("bの値を入力: "))

# TOD

def prime_number(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n)):
        if n % i == 0:
            return False
        
    return True

print(prime_number(a))
print(prime_number(b))
    

