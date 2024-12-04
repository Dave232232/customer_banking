#input check function
#try function for months
def integer_test(months_input):
    try:
        int(months_input)
    except Exception:
        return True #returns true if error occurs
    return int(months_input) #returns months as integer if no error

def check(user_input, step):
    #initialize variables
    max_iterations=2
    iteration_count=1
    integer_error=integer_test(user_input)
    balance=user_input
    apr=user_input
    months=integer_error
  

    #check on balance
    while iteration_count<=max_iterations and user_input.isdigit()==False and step=="balance":
        balance=(input("Please enter a number for your account balance.  No units are necessary.\nFor example, a balance of $100 would be entered as 100. "))
        user_input=balance
        iteration_count=iteration_count+1
        if iteration_count>max_iterations and step=="balance":
            print("I am sorry, I need a number.  The program will exit now.")
            balance="exit"
   
    #check on APR
    while iteration_count<=max_iterations and user_input.isdigit()==False and step=="apr":
        apr=(input("Please enter a number for the APR on your account.\nFor example, an APR of 1% would be entered as 1. "))
        user_input=apr
        iteration_count=iteration_count+1
    if iteration_count>max_iterations and step=="apr":
        print("I am sorry, I need a number.  The program will exit now.")
        apr="exit"

    #check on months
    while iteration_count<=max_iterations and integer_error==True and step=="months":
        months=(input("Please enter an integer for the number on months.  Partial months are not allowed.\nFor example, 2 months should be entered as 2. "))
        integer_error=integer_test(months)
        iteration_count=iteration_count+1
    if iteration_count>max_iterations and step=="months":
        print("I am sorry, I need an integer.  The program will exit now.")
        months="exit"
    #else:
     #   print("++++++++++++++++++",integer_error, type(integer_error))
      #  months=integer_error
    
    return [balance,apr,months]
