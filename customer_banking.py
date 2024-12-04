# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account
from input_check_function import check

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    
    #get balance for savings account
    user_balance=(input("\nWhat is your current savings account balance? "))
    #check for proper input on balance
    input_check=check(user_balance, "balance")[0]
    if input_check=="exit":
        exit()
    else:
        user_balance=input_check
    
    #get interest rate for savings account
    user_interest_rate=(input("\nWhat is the APR of your savings account? "))
    #check for proper input on interest rate
    input_check=check(user_interest_rate, "apr")[1]
    if input_check=="exit":
        exit()
    else:
        user_interest_rate=input_check

    #get months
    user_months=(input("\nHow many months of interest should be calculated? "))
    #check for proper input on on months
    input_check=check(user_months, "months")[2]
    if input_check=="exit":
        exit()
    else:
        user_months=input_check
    
    # Call the create_savings_account function and pass the variables from the user.
    #updated_savings_balance, interest_earned = create_savings_account#(savings_balance, savings_interest, savings_maturity)
    interest_earned=create_savings_account(float(user_balance),float(user_interest_rate),int(user_months))[0]
    updated_balance=create_savings_account(float(user_balance),float(user_interest_rate),int(user_months))[1]

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"\nYou have earned ${interest_earned:,.2f} on your savings acount and your updated balance is ${updated_balance:,.2f}\n")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    
    #get balance for CD
    user_balance=(input("\nWhat is your current CD account balance? "))
    #check for proper input on balance
    input_check=check(user_balance, "balance")[0]
    if input_check=="exit":
        exit()
    else:
        user_balance=input_check

    #get APR for CD
    user_interest_rate=(input("\nWhat is the APR of your CD account? "))
    #check for proper input on interest rate
    input_check=check(user_interest_rate, "apr")[1]
    if input_check=="exit":
        exit()
    else:
        user_interest_rate=input_check

    #get months for CD
    user_months=(input("\nHow many months of interest should be calculated? "))
    #check for proper input on on months
    input_check=check(user_months, "months")[2]
    if input_check=="exit":
        exit()
    else:
        user_months=input_check

    # Call the create_cd_account function and pass the variables from the user.
    #updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)
    interest_earned=create_cd_account(float(user_balance),float(user_interest_rate),int(user_months))[0]
    updated_balance=create_cd_account(float(user_balance),float(user_interest_rate),int(user_months))[1]

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"\nYou have earned ${interest_earned:,.2f} on your CD acount and your updated balance is ${updated_balance:,.2f}\n")

if __name__ == "__main__":
    # Call the main function.
    main()