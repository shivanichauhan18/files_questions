my_file2=open("people2.txt","w")
my_file2.write("abhisek-gurgao\n")
my_file2.write("ranveer-Delhi")
my_file2.write("\nshivani-mp ")
my_file2.write("sonam-mp \n")
my_file2.write("anjali-mp \n")
my_file2.write("bulbul-mumbai \n")
my_file2.close()


my_file2=open("people2.txt","r")
my_data=my_file2.read()
print my_data
my_file2.close()
