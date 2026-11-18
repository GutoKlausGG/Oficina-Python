nums = [12, 45, 7, 30, 2, 19]

maior = nums[0]
menor = nums[0]

for num in nums:
    if num > maior:
        maior = num

    if num < menor:
        menor = num

print("Maior número:", maior)
print("Menor número:", menor)

print("Conferindo com max():", max(nums))
print("Conferindo com min():", min(nums))