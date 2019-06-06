my_file=open("people1_exercise.txt","r")
my_data=my_file.read()
i=0
count=0
while i<len(my_data):
    if my_data[i]=="\n":
        count=count+1
    i=i+1
print count
print len(my_data)
my_file.close()