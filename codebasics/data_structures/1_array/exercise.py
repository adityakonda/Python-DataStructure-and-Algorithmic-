"""
1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
"""


def check_spent(expenses, amount):
    has_spent = False
    for exp in expenses:
        if exp == amount:
            has_spent = True
            break
    return has_spent


def item_returned(expenses: list, month, amount):
    expenses[month - 1] = expenses[month - 1] - amount

    # expenses.insert(month - 1, expenses[month - 1] - amount)
    return expenses


def odd_number(number):
    odd_numbers = []

    for i in range(1, number):
        if i % 2 != 0:
            odd_numbers.append(i)
    return odd_numbers


if __name__ == '__main__':
    expenses = {"JAN": 2200, "FEB": 2350, "MAR": 2600, "APR": 2600, "MAY": 2190}
    expenses_list = [2200, 2350, 2600, 2130, 2190]

    first_quater_expenses = 0
    for i in range(3):
        first_quater_expenses += expenses_list[i]
    # Assignment 1
    print("dollar spent extra compared to Jan is : ", expenses_list[1] - expenses_list[0])
    print("total expense in first quarter: ", first_quater_expenses)
    print("sppent exactly 2000 in any month : ", check_spent(expenses_list, 2130))
    expenses_list.append(1980)
    print("adding june month expenses: ", expenses_list)
    print("item returned in April      ", item_returned(expenses_list, 4, 200))

    # Assignment 3
    print("odd_numbers: ", odd_number(100))
