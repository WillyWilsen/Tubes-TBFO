x = ["apple", "banana", "cherry"]

y = x

a = x is y 
print(a)

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

x = 10
if not x > 10:
    print("not returned True")
else:
    print("not returned False")