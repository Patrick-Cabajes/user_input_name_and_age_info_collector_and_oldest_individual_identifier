#declare personalinfovault as an empty array
personalinfovault = {}

#while True:
    #ask user to input name (i.e Pat)
while True:
    while True:
        name = input("Please input your name: ")

        #add conditions such as it contains only letters, initial letter is capitalized while others are in lower case
        #if not:
            #print "Error: Please input a valid name and follow the format"
        if not name.isalpha():
            print("Error: Please input letter only")
    
        elif not name.istitle():
            print("Error: All characters should be in lowercase except the initial letter")
     
        elif len(name) <2:
            print("Error: Please provide a longer name")
        
        else:
            break

    #while True:
        #ask user to input age
    while True:
        age = int(input("How old are you?: "))

        #add conditions such as age >= 0
        #if not:
            #print "Error: Please input a valid age"
        if age < 0 and age > 150:
            print("Please provide a valid age")

        else:
            break

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