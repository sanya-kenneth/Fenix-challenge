def compute_days_of_lighting(rate1, day1_in, rate2, day2_in, rate3,
                                day3_in, customer_payment, balance=0):
    """
    Function computes days of lighting for a customer.

    Args:
        rate1 (int): rate for Loan1
        day1_in (int): days for Loan1 to start
        rate2 (int): rate for Loan2
        day2_in (int): days for Loan2 to start
        rate3 (int): rate for Loan3
        day3_in (int): days for Loan3 to start
        customer_payment (int): Amount paid by the customer
        balance (int): Customer's balance

    Returns
        dictionary containing the number of days of lighting and
        the customer's balance
    """
    days_of_power = 0
    input_value_list = [rate1, day1_in, rate2, day2_in, rate3, day3_in, customer_payment]
    for digit in input_value_list:
        # validate user input values
        if not isinstance(digit, int):
            return "Error.Invalid input!! All inputs must be valid numbers."
    loan_days = [(day1_in, rate1), (day2_in, rate2), (day3_in, rate3)]
    # Sort loans
    loan_days.sort()
    # daily rate for loans
    daily_rate = 0
    # days of lighting for each loan
    day1_days = 0
    day2_days = 0
    day3_days = 0
    day1_2_days = 0
    day1_3_days = 0
    day2_3_days = 0
    day2_1_3_days = 0
    # day input for each loan
    day1 = loan_days[0][0]
    day2 = loan_days[1][0]
    day3 = loan_days[2][0]
    day1_2 = day1 + day2
    # rate input for each loan
    day1_rate = loan_days[0][1]
    day2_rate = loan_days[1][1]
    day3_rate = loan_days[2][1]
    # total days of lighting the customer is entitled to
    total_days_of_power = 0
    # customer's balance
    balance = balance
    # total amount customer has paid
    customer_payment = customer_payment + balance
    while daily_rate < customer_payment:
        while day1 == day2:
            daily_rate = day1_rate + day2_rate
            day1_2_days = day1_2_days + 1
            day1_2 = day1_2 + 1
            customer_payment -= daily_rate
            if day1_2 > day3 or daily_rate > customer_payment:
                break
        total_days_of_power = total_days_of_power + day1_2_days
        # compute days for the first loan
        while day1 < day2 and daily_rate < customer_payment:
            daily_rate = day1_rate
            day1_days = day1_days + 1
            day1 = day1 + 1
            customer_payment -= daily_rate
            if day1 >= day2:
                break
        total_days_of_power = total_days_of_power + day1_days
        # compute days for the second loan
        while day2 < day3 and daily_rate < customer_payment:
            daily_rate = day2_rate + day1_rate
            day2_days = day2_days + 1
            day2 = day2 + 1
            customer_payment -= daily_rate
            if day2 >= day3:
                break
        total_days_of_power = total_days_of_power + day2_days
        # compute days for the third loan 
        while day3 and daily_rate < customer_payment:
            daily_rate = day3_rate + day2_rate + day1_rate
            day3_days = day3_days + 1
            day3 = day3 + 1
            customer_payment -= daily_rate
            if daily_rate > customer_payment:
                break
        total_days_of_power = total_days_of_power + day3_days
    return {"days_of_power": total_days_of_power, "customer_balance": customer_payment}
