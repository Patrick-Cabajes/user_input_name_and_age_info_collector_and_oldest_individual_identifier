#declare personalinfovault as an empty array
personalinfovault = {}

while True:
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
            if age < 0 or age > 150:
                print("Error: Please provide a valid age between 0 and 150")

            else:
                break
    
        #Store the user's information to the dictionary
        personalinfovault[name]= age

        #Ask user if he/she would like to input another entry
        retry = input("Would you like to input another entry? (yes/no): ")
        break
        
    if retry == "yes":
        print("Request Accepted: Please input a new entry")
        
    #if the response is no
        #print the name and age of the oldest individual
    elif retry == "no":
        print(f"The oldest individual is {name}, he/she is {age} years old.")
        break

#determines the oldest individual
oldest_age = 0
oldest_name = ("")

for name, age in personalinfovault.items():
    if age > oldest_age:
        oldest_age = age
        oldest_name = name