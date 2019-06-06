myFile=open("people1_exercise.txt","r")
my_Data=myFile.readlines()
i=0
count_line=0
while i<len(my_Data):
	count_line=count_line+1
	i=i+1
print count_line
myFile.close()