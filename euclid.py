a = input("a の値を入力: ")
b = input("b の値を入力: ")

#TODO

s = int(a)
m = int(b)

while m != 0:
    temp = s % m
    s = m
    m = temp
    
print(s)
    

