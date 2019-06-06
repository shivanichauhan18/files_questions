my_file3 = open("test_file.txt", "w")
my_file3.write("Yahan main kuch likha")
my_file3.write("\nYaha maine kuch aur bhi likha.\n shivani - biotech field \n anjali paitil- bca se\n")
my_file3.write("anjali sen-microbiology se hai\n")
my_file3.write("bulbul-cs")
my_file3.close()
#my_file3.write("i write something")


my_file=open("test_file.txt","r")
new_data=my_file.read()
print new_data
my_file.close()