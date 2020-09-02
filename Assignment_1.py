list= [14, 12, 11, 15, 13]
i = 0
while i < len(list):
    j = i +1
    while j < len(list):
        if list[i] > list[j]:
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
        j += 1
    i +=1
print(list)
