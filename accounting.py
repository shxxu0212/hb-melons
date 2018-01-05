MELON_COST = 1.00


def melon_payment_calculator(file_name):
    """Calculate cost of melons and see who underpaid."""

    payment_data = open(file_name) # open file 

    # iterate over lines in file
    for line in payment_data: 
        # for each line, split by |
        order = line.split('|')

        # get the first name after splitting full name (idx 1) by " "
        customer_first_name = order[1].split(" ")[0] 

        # get of melons sold and payment ammount
        customer_melons = float(order[2])
        customer_paid = float(order[3])

        # calculate expected price
        customer_expected = customer_melons * MELON_COST

        # check if customer over or under paid
        if customer_expected < customer_paid:
            # .2f gives 2 decimal spaces
            print "{} paid ${:.2f}, expected ${:.2f}. Overpaid!".format( 
                customer_first_name, customer_paid, customer_expected)

        elif customer_expected > customer_paid:
            print "{} paid ${:.2f}, expected ${:.2f}. Underpaid!".format(
                customer_first_name, customer_paid, customer_expected)

    # close the file
    payment_data.close()

# call the function 
melon_payment_calculator("customer-orders.txt")
