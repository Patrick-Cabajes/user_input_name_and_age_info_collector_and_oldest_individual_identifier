#declare personalinfovault as an empty array
personalinfovault = {}

#while True:
    #ask user to input name (i.e Pat)
digit = False
while True:
    name = input("Please input your name: ")

    #add conditions such as it contains only letters, initial letter is capitalized while others are in lower case
    #if not:
        #print "Error: Please input a valid name and follow the format"
    if not name.istitle():
        print("All characters should be in lowercase except the initial letter")

    for char in name:
        if name.isdigit():
                digit = True
                break
    if digit == True:
        print("Please put letters only")
        
    if len(name) <2:
        print("Please provide a longer name")


#while True:
    #ask user to input age 
    #add conditions such as age >= 0
    #if not:
        #print "Error: Please input a valid age"

    #add the user input name and user input age to the dictionary

    #Ask user if he/she would like to input another entry
    #if the response is no
        #print the name and age of the oldest individual 

#declare oldest age as 0
#declare oldest name as a blank string
    #for each entry in personalinfovaul set
        #entry.age > oldest age
        #oldest age > entry.age
        #oldest name > entry.name