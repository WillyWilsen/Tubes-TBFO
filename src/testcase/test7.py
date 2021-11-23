numbers = [1,2,3,4,5,6,7,8,9,10]

jumlah = 0
for i in range(len(numbers)):
    jumlah += numbers[i]

i = 0
jumlah1 = 0
while i < len(numbers):
    jumlah1 += numbers[i]
    i += 1 

print(jumlah)
print(jumlah1)