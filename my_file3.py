my_question=open("people2_question.txt","w")
my_question.write("rishabh-meerut\nimtiyaz-cochin\nnilima-delhi\nrati-shimla\nayishah-delhi\nnaseer-kanpur\nraghu-shimla\nkartikeyan-delhi\nsalma-jaipur\npankaj-delhi\nbrijesh-delhi\ngovind-delhi\npunnet-shimla\nsiddi-delhi\nsuman-jaipur\nrajeev-shimla\nmohindar-delhi\nrajendra-shimla\npriyanka-shimla\nneelma-delhi\nsashi-jaipur\nsarika-delhi\ndeepti-shimla\nharshad-delhi\ntrishna-raipur\npradeep-jaipur\nsekhar-delhi\nnand-delhi\nanoop-delhi\nbalwindar-tokyo")
my_question.close()

my_file=open("people2_question.txt","r")
my_data=my_file.read()
print my_data
my_file.close()