a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TOD

a = int(a)
b = int(b)

if a <= 1:
    print(f"{a}は素数ではありません。")
else:
    is_prime_a = True
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            is_prime_a = False
            break
    print(f"{a}は素数です。" if is_prime_a else f"{a}は素数ではありません。")


if b <= 1:
    print(f"{b}は素数ではありません。")
else:
    is_prime_b = True
    for i in range(2, int(b**0.5) + 1):
        if b % i == 0:
            is_prime_b = False
            break
    print(f"{b}は素数です。" if is_prime_b else f"{b}は素数ではありません。")