number_list=[[1,2,3],
			[2,1,3],
			[3,2,1]]
i=0
total_number=0
while i<len(number_list):
	j=0
	while i<len(number_list[i]):
		total_number=number_list[i][j]+total_number
		j=j+1
	i=i+1
print total_number				