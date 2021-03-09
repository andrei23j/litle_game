def create_name():
    """ Validation of user-entered data,  creating and confirm name.
    The function itself will ask you to enter a name and she checking the correctness of the characters.
    """
    # Creating a list with the symbols of the Latin alphabet.
    com_list = ""
    j = 0
    name = ""
    for i in range(97, 122, 1):
        com_list += com_list + str(chr(i))
    while j != 1:
        name = input("\nPlease enter you name. You name: ")
        name_1 = name.lower()
        if len(name) not in range(3, 10 + 1) or len(name) == 0:
            print("\nThe name cannot be shorter than 3 characters.")
            print("\nThe name must not be longer than 10 characters.")
        else:
            for i in name_1:
                if i not in com_list:
                    print("\nThe name can only consist of letters of the Latin alphabet.")
                    break
                else:
                    j = 1
    return name


def enter_money():
    """
    This function allows the user to enter the number of banknotes.
    banknotes - (int) - number of banknotes.
    """
    # Operation 1. Checking the exception and owning in range.
    banknotes = ""
    while banknotes not in range(0, 10 + 1, 1):
        banknotes = input("\nEnter the number of banknotes in your wallet.\nBanknotes: = ")
        try:
            banknotes = int(banknotes)
        except ValueError:
            print("\nPlease enter the integer number.")
        else:
            if banknotes < 0:
                print("\nThere can be no less than 0 banknotes. You don’t owe anyone money yet.")
            elif banknotes > 10:
                print("\nYou don't live so richly. Maximum 10 banknotes.")
            else:
                return banknotes


def enter_value(total):
    """
    This function allows the user to enter the number of banknotes.
    total - (int) - quantity of money.
    """
    # Operation 1. Checking the exception and owning in range.
    value = ""
    while value not in range(1, total + 1, 1):
        value = input("\nPlease enter value.\nValue = ")
        try:
            value = int(value)
        except ValueError:
            print("\nPlease enter the integer number.")
        else:
            if value < 1:
                print("\nYou cannot give 0 banknotes.")
            elif value > total:
                print("\nThe value cannot be greater than:", total)
            else:
                return value


def total_money(**dict_money):
    """
    This function processes the amount that the dude wants to give.
    **kwargs - (dict) - A dictionary with money in the form (value of banknote: quantity).
    """
    total = 0
    for key in dict_money:
        nominal = int(str(key)[:-4])
        total = total + nominal * dict_money[key]
    return total


def wallet_possibility(quantity, **wallet):
    """
    This function checks the availability of money and the remaining denominations of bills.
    It returns the dictionary with denominations anyway.
    If not possible, the function will return "Not OK".
    quantity - (int)  - The amount of money you want to use.
    **wallet - (dict) - A dictionary with money in the form (value of banknote: quantity).
    """
    additional_wallet = {}
    possible = 0
    for key in wallet:
        if int(str(key)[:-4]) > quantity:
            break
        else:
            nominal = int(str(key)[:-4])
            possible = possible + nominal * wallet[key]
            additional_wallet[key] = wallet[key]
    if possible < quantity:
        print("\nYou can convey only:", possible, "Rub.")
        for key in additional_wallet:
            print("There are", key, "banknotes", additional_wallet[key], "pieces left.")
        return "Not Ok"
    else:
        pass
    return wallet


def drop_money(quantity, **wallet):
    """
    The function returns a dictionary with denominations of denominations for deduction.
    If not possible, the function will return "Not OK".
    quantity - (int)  - The amount of money you want to use.
    **wallet - (dict) - A dictionary with money in the form (value of banknote: quantity).
    """
    output_sum = 0
    output_wallet = {}
    additional_wallet = wallet
    additional_wallet_1 = {}
    additional_wallet_2 = {}
    max_key = ""
    for key in wallet:
        output_wallet[key] = 0
    while quantity != 0:
        value = 0
        min_key = "100 Rub"

        for key in additional_wallet:
            if additional_wallet[key] != 0:
                additional_wallet_1[key] = additional_wallet[key]
            else:
                pass

        for key in additional_wallet_1:
            if int(str(key)[:-4]) > quantity:
                break
            else:
                if additional_wallet_1[key] == value:
                    additional_wallet_2[key] = additional_wallet_1[key]
                    value = additional_wallet_1[key]
                    max_key = key
                elif additional_wallet_1[key] > value:
                    additional_wallet_2.clear()
                    additional_wallet_2[key] = additional_wallet_1[key]
                    value = additional_wallet_1[key]
                    max_key = key
                else:
                    pass

        for key in additional_wallet_1:
            if int(str(key)[:-4]) > quantity:
                break
            else:
                if additional_wallet_1[key] == value:
                    additional_wallet_2[key] = additional_wallet_1[key]
                    value = additional_wallet_1[key]
                elif additional_wallet_1[key] < value:
                    additional_wallet_2.clear()
                    additional_wallet_2[key] = additional_wallet_1[key]
                    value = additional_wallet_1[key]
                else:
                    pass

        for key in additional_wallet_1:
            if (int(str(min_key)[:-4])) < (int(str(key)[:-4])):
                pass
            else:
                min_key = key

        if quantity % (int(str(min_key)[:-4])) != 0:
            print("\nThe requested amount must be a multiple of:", min_key)
            return "Not Ok"
        else:
            pass

        if value <= 2:
            for key in additional_wallet_1:
                if int(str(key)[:-4]) > quantity:
                    break
                else:
                    max_key = key
            output_wallet[max_key] = output_wallet[max_key] + 1
            additional_wallet[max_key] = additional_wallet[max_key] - 1
            output_sum = output_sum + int(str(max_key)[:-4])
            quantity = quantity - int(str(max_key)[:-4])
            additional_wallet_1.clear()
        else:
            output_wallet[max_key] = output_wallet[max_key] + 1
            additional_wallet[max_key] = additional_wallet[max_key] - 1
            output_sum = output_sum + int(str(max_key)[:-4])
            quantity = quantity - int(str(max_key)[:-4])
            additional_wallet_1.clear()
    return output_wallet


def upgrade_dict(dict_1, dict_2):
    """
    This function subtracts the values of the second dictionary from the first and returns a new dictionary.
    dict_1, dict_2 - (dict) - Two dictionaries with the same keys and the same size.
    """
    dict_3 = {}
    for key in dict_1:
        dict_3[key] = dict_1[key] - dict_2[key]
    return dict_3
