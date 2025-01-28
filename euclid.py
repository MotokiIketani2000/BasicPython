a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
def euculid(a,b):
    if a / b ==0:
        return a
        
    return euculid(b, a / b)

print(euculid(int(a),int(b)))
