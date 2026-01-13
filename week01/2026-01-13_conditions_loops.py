#1
def count_even_odd(nums):
    even_count = 0
    odd_count = 0
    for i in nums:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

n = int(input())
nums = list(map(int, input().split()))
print(*count_even_odd(nums))

#2
def print_gugudan(a,b):
    for i in range(a,b+1):
        for j in range(1,10):
            print(f"{i} X {j} = {i*j}")
    if i != b:
        print()
a,b = map(int, input().split())
print_gugudan(a,b)


#3
def check_password(pw):
    if len(pw) < 8: return False
    has_alpha = any(c.isalpha() for c in pw)
    has_digit = any(c.isdigit() for c in pw)
    return has_alpha and has_digit
pw = input()
if check_password(pw):
    print("OK")
else:
    print("NO")