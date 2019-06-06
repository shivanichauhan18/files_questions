delhi_file=open("delhi.txt","w")
shimla_file=open("shimla.txt","w")
others_file=open("others.txt","w")
name=["rishabh","imtiyaz","nilima","rati","ayishah","raghu","naseer","karthikeyan","salma","pankaj","brijesh","govind","puneet","sidhhi","suman","rajeev","mohinder","rajendra","priyanka","neela","sashi","sarika","deepti","harshad","trishna","pradeep","sekhar","nand","anoop","balwinder"]
place=["meerut","delhi","cochin","shimla","delhi","shimla","kanpur","delhi","jaipur","delhi","delhi","delhi","shimla","delhi","jaipur","shimla","delhi","jaipur","shimla","delhi","shimla","delhi","raipur","jaipur","delhi","delhi","tokyo"]
i=0
while i<len(place):
	if place[i]=="delhi":
		delhi_file.write(name[i]+"-"+place[i]+"\n")
	elif place[i]=="shimla":
		shimla_file.write(name[i]+"-"+place[i]+"\n")
	else:
		others_file.write(name[i]+"-"+place[i]+"\n")
	i=i+1
delhi_file.close()
shimla_file.close()
others_file.close()
