#1
def split_even_odd(nums):
    evens = []
    odds = []
    for i in nums:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    return evens, odds

nums = list(map(int, input().split()))
evens, odds = split_even_odd(nums)
print("evens:",evens)
print("odds:",odds)
print(f"even_count: {len(evens)}, odd_count: {len(odds)}, ")
print(f"even_sum: {sum(evens)}, odd_sum: {sum(odds)}")

#Comprehension Code
'''
    for x in nums:
        (evens if x % 2 == 0 else odds).append(x)
    return evens, odds
'''

#2
def save_item_list(n):
    item_list = {}
    for i in range(n):
        name, price = input().split()
        item_list[name] = int(price)
    return item_list
#before
'''
def cal_stuff(cart):
'''
#after
def cal_stuff(cart, item_list):
    unknown_item = []
    total_price = 0
    for item in cart:
        if item not in item_list:
            unknown_item.append(item)
        else:
            total_price += item_list[item]
    return unknown_item, total_price

n = int(input())
item_list = save_item_list(n)

m = int(input())
cart = []
for i in range(m):
    cart.append(input())
unknown_item, total_price = cal_stuff(cart, item_list)

print("Unknown item: ",end='')
for i in range(len(unknown_item)):
    print(unknown_item[i], end='')
print()
print("total: ",total_price)





