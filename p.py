number_list=[[1,2.3],
			[2,1,3],
			[3,2,1]]
i=0
j=0
new_list=[]
sum=0
while i<len(number_list):
	new_list.append(number_list[i][j])
	sum=sum+new_list[i]
	j=j+1
	i=i+1
print sum				