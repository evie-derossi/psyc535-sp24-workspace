"""Tell length of each inner list and averace score of each inner list."""

partic_ratings : list[list[int]] = [[4,5], [1,2,3], [1], [7,3,8,2,4]]
length_list = []
avg = 0
avg_list =[]


for l in partic_ratings:
    length_list.append(len(l))
    for num in l:
        avg += num
    avg /= len(l)
    avg_list.append(avg)
    avg = 0
print(length_list)
print(avg_list)