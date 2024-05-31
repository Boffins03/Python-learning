import math

def calculate_number_of_months():
    loan_principal = int(input("Enter the loan principal:\n"))
    monthly_payment = int(input("Enter the monthly payment:\n"))
    loan_interest = float(input("Enter the loan interest:\n")) / 100 / 12
    x = monthly_payment / (monthly_payment - loan_interest * loan_principal)
    num_months = math.ceil(math.log(x, 1 + loan_interest))
    years = num_months // 12
    months = num_months % 12
    if years == 0:
        print(f"It will take {months} months to repay the loan")
    elif months == 0:
        print(f"It will take {years} years to repay the loan")
    else:
        print(f"It will take {years} years and {months} months to repay the loan")

def calculate_annuity_payment():
    loan_principal = int(input("Enter the loan principal:\n"))
    num_periods = int(input("Enter the number of periods:\n"))
    loan_interest = float(input("Enter the loan interest:\n")) / 100 / 12
    annuity_payment = loan_principal * loan_interest / (1 - (1 + loan_interest) ** -num_periods)
    print(f"Your monthly payment = {math.ceil(annuity_payment)}")

def calculate_loan_principal():
    annuity_payment = float(input("Enter the annuity payment:\n"))
    num_periods = int(input("Enter the number of periods:\n"))
    loan_interest = float(input("Enter the loan interest:\n")) / 100 / 12
    loan_principal = annuity_payment / ((loan_interest * (1 + loan_interest) ** num_periods) / ((1 + loan_interest) ** num_periods - 1))
    print(f"Your loan principal = {math.ceil(loan_principal)}")

def main():
    print("What do you want to calculate?")
    calculation_type = input("""Type "n" for number of monthly payments,
Type "a" for annuity monthly payment amount,
Type "p" for loan principal:
""")
    if calculation_type == 'n':
        calculate_number_of_months()
    elif calculation_type == 'a':
        calculate_annuity_payment()
    elif calculation_type == 'p':
        calculate_loan_principal()
    else:
        print("Invalid input. Please select a valid option.")

if __name__ == "__main__":
    main()
