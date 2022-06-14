from models.apiRequest import API
import sys

dateApi = API()

check = True

while check == True:
    try:
        startDate = input("Enter a start date YYYY-MM-DD: ")
        endDate = input("Enter a end date YYYY-MM-DD: ")
        dateApi.getDateRange(startDate,endDate)
    except:
        print("\nPlease enter a date in the correct format\n")
    
    run = True
    while run == True:
        test = input("exit? YES or NO: ")
        if test.lower() == "yes":
            check = False
            run = False
            break
        elif test.lower() == "no":
            check = True
            run = False
        else:
            print("Please enter YES or NO")

        
    
