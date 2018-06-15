#!/usr/bin/env python

import unittest
from vending_machine import VendingMachine



class VendingMachineTests(unittest.TestCase):
    def setUp(self):
        self.machine = VendingMachine(0.5, 1.0, 0.65)
        pass

    def test_sold_out(self):
        self.assertEqual(self.machine.has_product("CHIPS"), None)

    def test_show_zero_fifty_as_total_chip(self):
        self.assertEqual(self.machine.get_chips_price(), 0.50)

    def test_show_one_as_total_cola(self):
        self.assertEqual(self.machine.get_cola_price(),1)

    def test_show_zero_sixty_five_as_total_candy(self):
        self.assertEqual(self.machine.get_candy_price(),0.65)

    def test_coin_accepted(self):
        self.assertTrue(self.machine.insert_coin("NICKELS"))
        self.assertTrue(self.machine.insert_coin("DIMES"))
        self.assertTrue(self.machine.insert_coin("QUARTERS"))

    def test_coin_non_accepted(self):
        self.assertFalse(self.machine.insert_coin("PENNIES"))

    def test_display_insert_coin_when_zero_amount(self):
        self.assertEqual(self.machine.display(), "INSERT COIN")

    def test_display_quarter_credit(self):
        self.machine.insert_coin("QUARTERS")
        self.assertEqual(self.machine.display(), 0.25)

    def test_display_penny_credit(self):
        self.machine.insert_coin("PENNIES")
        self.assertEqual(self.machine.display(), "INSERT COIN")

    def test_display_two_quarters(self):
        self.machine.insert_coin("QUARTERS")
        self.machine.insert_coin("QUARTERS")
        self.assertEqual(self.machine.display(), 0.50)

    def test_display_one_pennie_two_quarters(self):
        self.machine.insert_coin("QUARTERS")
        self.machine.insert_coin("QUARTERS")
        self.machine.insert_coin("PENNIES")
        self.assertEqual(self.machine.display(), 0.50)

    def test_display_one_quarter_and_one_dime(self):
        self.machine.insert_coin("QUARTERS")
        self.machine.insert_coin("DIMES")
        self.assertEqual(self.machine.display(), 0.35)

    def test_display_one_quarter_and_one_nickel(self):
        self.machine.insert_coin("QUARTERS")
        self.machine.insert_coin("NICKELS")
        self.assertEqual(self.machine.display(), 0.30)

#    def test_sell_product(self):
#        self.machine.select("QUARTERS")
#        self.machine.insert_coin("NICKELS")
#        self.assertEqual(self.machine.display(), 0.30)

if __name__ == '__main__':
    unittest.main()
