my_question=open("people2_question.txt","w")
my_question.write("rishabh-meerut\n","imtiyaz-cochin\n","nilima-delhi\n","rati-shimla\n","ayishah-delhi\n","naseer-kanpur\n","raghu-shimla\n","kartikeyan-delhi\n","salma-jaipur\n","pankaj-delhi\n","brijesh-delhi\n",
"govind-delhi\n","punnet-shimla\n","siddi-delhi\n","suman-jaipur\n","rajeev-shimla\n","mohindar-delhi\n","rajendra-shimla\n","priyanka-shimla\n","neelma-delhi\n","sashi-jaipur\n","sarika-delhi\n","deepti-shimla\n","harshad-delhi\n","trishna-raipur\n","pradeep-jaipur\n","sekhar-delhi\n","nand-delhi\n","anoop-delhi\n","balwindar-tokyo"
my_question.close()






my_question=open("people2_question.txt","r")
my_data=my_question.readline()
print my_data
my_question.close()