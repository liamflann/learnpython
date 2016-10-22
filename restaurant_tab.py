# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 17:49:10 2016

@author: Liam
"""

def supper():
        print('''This program will calculate the amount of money left over on a giftcard after eating at a restaurant with an 8% tax''')
        print"Tell us about person one's meal."        
        gift_card = float(raw_input("Gift card amount: "))        
        appetizer1 = float(raw_input("Appetizer: "))
        entree1 = float(raw_input("Entree: "))
        drinks1 = float(raw_input('Drinks: '))
        dessert1 = float(raw_input('Dessert: '))
        print"Tell us about person two's meal."        
        appetizer2 = float(raw_input('Appetizer: '))
        entree2 = float(raw_input('Entree: '))
        drinks2 = float(raw_input('Drinks: '))
        dessert2 = float(raw_input('Dessert: '))
        total = appetizer1+appetizer2+entree1+entree2+drinks1+drinks2+dessert1+dessert2
        tax = total*.08
        print'Your pre tax total is: $', total
        print'Your tax is: $', tax
        new_total = total + tax
        print'Your new total is: $', new_total
        remaining = gift_card-new_total
        print'You have $', remaining, ' remaining on your card.'
