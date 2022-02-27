month= str(input("Enter A Month: "))
#Statements
#31 Days
if month in ['January','january','March','march','May','may', 'July','july','August','august','October','october', 'December','december']:
    print("31")
#28 Days
if month in ['February', 'february']:
   print("28")
   print("29 If Leap Year")
#30 Days
if month in['April','april','June','june','September','september','November','november']:
    print("30")
