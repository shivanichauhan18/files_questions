list1=[1,2,[3,4],[5,6]]
i=0
while i<len(list1):
	j=0
	sum=0
	while j<len(list1[i]):
		sum=sum+list1[i][j]
		j=j+1
	i=i+1
print sum

def sum1(lst):
    total = 0
    for element in lst:
        if (type(element) == type([])):
            total = total + sum1(element)
        else:
            total = total + element
    return total
print( "Sum is:",sum1([1,2,[3,4][5,6]]))