# Importing additional libraries.
import additional_dll


class Dude:
    def __init__(self):
        """
        Creating an inhabitant of the system.
        name - (str)  - it is name of dude.
        wallet - (dict) - it is dict with money of dude.
        """
        self.name = self.create_name()
        self.wallet = self.create_wallet()
        self.total_money = self.possible_money(**self.wallet)

    @staticmethod
    def create_wallet():
        """
        This function initializes the dude's first money data.
        """
        dude_wallet = \
            {
                "5 Rub": "",
                "10 Rub": "",
                "20 Rub": "",
                "50 Rub": "",
                "100 Rub": "",
            }
        for key in dude_wallet:
            print("\nHow many banknotes with a face value of", key, "are in your wallet?")
            dude_wallet[key] = additional_dll.enter_money()
            print(key, ":", dude_wallet[key])
        return dude_wallet

    @staticmethod
    def create_name():
        """
        This function initializes the dude's name.
        """
        name = additional_dll.create_name()
        print("\nIt's a good name. Your name is:", name)
        return name

    @staticmethod
    def possible_money(**wallet):
        """
        This function calculates the dude's available amount of money.
        **wallet - (dict) - A dictionary with affordable money.
        """
        money = additional_dll.total_money(**wallet)
        return money

    def give_money(self):
        """
        This function subtracts a given amount of money from the dude's wallet.
        """
        a = "Not Ok"
        while a != "Ok":
            money = additional_dll.enter_value(self.total_money)
            possibility_dict = additional_dll.wallet_possibility(money, **self.wallet)
            giv_money = additional_dll.drop_money(money, **possibility_dict)
            if giv_money == "Not Ok":
                continue
            else:
                new_wallet = additional_dll.upgrade_dict(self.wallet, giv_money)
                a = "Ok"
                self.wallet = new_wallet
                self.total_money = self.possible_money(**self.wallet)
