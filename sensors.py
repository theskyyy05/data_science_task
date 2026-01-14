n = int(input("enter the number of readings: "))
readings = eval(input("enter the readings: "))

l2 = []
sum_list = []

for i in range(n - 2):
    group = []
    for j in range(i, i+3):
        group.append(readings[j])
    l2.append(group)

for grp in l2:
    s = 0
    for num in grp:
        s += num
    sum_list.append(s)

print("Groups of 3:", l2)
print("Sums:", sum_list)
print("Highest total signal:", max(sum_list))
