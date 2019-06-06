bank_list=["Kotak ","HDFC","RBL","SBI","Bank Of Baroda"]

my_file=open("file_question3.txt","w")
#bank_list=["Kotak ","HDFC","RBL","SBI","Bank Of Baroda"]
i = 0
while(i < len(bank_list)):
	my_file.write(bank_list[i]+"\n")
	i = i + 1
my_file.close()


my_file=open("file_question3.txt","r")
my_data=my_file.read()
print my_data
my_file.close()


