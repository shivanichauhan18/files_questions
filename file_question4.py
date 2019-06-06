shimlaFile=open("shimla1.txt","w")
delhiFile=open("delhi1.txt","w")
othersFile=open("others1.txt","w")
name_list=["rishabh","imtiyaz","nilima","rati","ayishah","raghu","naseer","karthikeyan","salma","pankaj","brijesh","govind","puneet","siddhi","suman","rajeev","mohinde","rajendra","priyanka","neela","sashi","sarika","deepti","harshad","trishna","pradeep","sekhar","nand","anoop","balwinder"]
place_list=["meerut","delhi","cochin","shimla","delhi","shimla","kanpur","delhi","jaipur","delhi","delhi"
,"delhi","shimla","delhi","jaipur","shimla","delhi","jaipur","shimla","delhi"
,"jaipur","delhi","shimla","delhi"," raipur","jaipur","delhi","delhi","delhi","tokyo"]


i=0
while i<len(name_list):
	if "delhi" == place_list[i]:
		delhiFile.write(name_list[i]+ "-" +place_list[i]+"\n")
	elif "shimla" == place_list[i]:
		shimlaFile.write(name_list[i] + "-" + place_list[i]+"\n")
	else:
		othersFile.write(name_list[i] + "-" + place_list[i]+"\n")
	i=i+1
delhiFile.close()
shimlaFile.close()
othersFile.close()




my_data=open("shimla1.txt","r")
my_data1=my_data.read()
print my_data1
my_data.close()



my_data=open("delhi1.txt","r")
my_data1=my_data.read()
print my_data1
my_data.close()

my_data=open("others1.txt","r")
my_data1=my_data.read()
print my_data1
my_data.close()