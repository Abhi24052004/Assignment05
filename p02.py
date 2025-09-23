l=[]
for i in range(1,11):
  l.append(i)
l1=[]
for i in range(1,6):
  l1.append(i)
print("Original List: ",l)
print("Extracted first five elements: ",l1)
l1.sort(reverse=True)
print("Reversed extracted elements: ",l1)
