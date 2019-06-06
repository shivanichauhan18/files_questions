my_file=open("people2_question.txt","r")
my_Data=my_file.readlines()
print my_Data
i=0
excute_value=""
count=0
while i<len(my_Data):
	count=count+1
	excute_value=excute_value+my_Data[i]
	i=i+1
print count
print excute_value
my_file.close()
