len = int(input("Введите количество строк в списке: "))

arr =[0]*len

for i in range(0,len):
    arr[i] = input("Введите строку: ")

arr_2 = [i*3 for i in arr]

print(arr_2)

