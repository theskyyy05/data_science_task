

n=int(input("enter the no of readings "))
readings=eval(input("enter the readings of values"))
k=int(input("enter the times of reading"))
l1=[]
l2=[]
i=0

for i in range(2):
  i=0
  while i<=2:
    l1.append(readings[i]) 
    list(l1)
    i=i+1
  i=i+1
l2.append(l1)
sum=0
print(l2)

for i in l2:
  for j in i:
    sum=sum+j

list_of_sum=list(sum)
print(f'the highest toral signal is{max(list_of_sum)} ')



