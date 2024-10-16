def is_gnomic(k):
    if k < 1 or k % 2 == 0:
        return False
    
    n = (k - 1) // 2
    return 2*n+1+n*n==(n+1)**2


# for i in range(1, 130):
#     if is_gnomic(i):
#         print(i)

result = 0

with open("gnomiczne.txt") as file:
    binary = file.read().strip().split("\n")

for num in binary:
    if num[-1] == '1':
        result += 1

print(result)