#!/usr/bin/env python


class VendingMachine:
    def __init__(self, chip_price, cola_price, candy_price):
        self.data = ""
        self.chip_price = chip_price
        self.cola_price = cola_price
        self.candy_price = candy_price
        self.amount = 0

    def has_product(self, param):
        return None

    def get_chips_price(self):
        return self.chip_price

    def get_cola_price(self):
        return self.cola_price

    def get_candy_price(self):
        return self.candy_price

    def insert_coin(self, coin_type):
        if coin_type == "PENNIES":
            return False
        elif coin_type == "QUARTERS":
            self.amount += 0.25
        elif coin_type == "DIMES":
            self.amount += 0.10
        elif coin_type == "NICKELS":
            self.amount += 0.05
        return True

    def display(self):
        if self.amount > 0:
            return self.amount
        return "INSERT COIN"
