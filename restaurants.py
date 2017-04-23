#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
import csv

attributes = ['name', 'loc', 'time', 'price', 'dist', 'cuisine']
pref_dict = {'name': [], 'loc': [], 'time': [], 'price': [],
             'dist': [], 'cuisine': []}

#added comment here to see what happens

class Restaurant(object):
    def __init__(self, name, loc, time, price, dist, cuisine):
        self.name = str(name)
        self.loc = str(loc)
        self.time = str(time)
        self.price = str(price)
        self.dist = str(dist)
        self.cuisine = str(cuisine)

    def __str__(self):
        return self.name


def readFile(filename, rlist):
    with open('rest.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            this_rest = Restaurant(
                row['name'], row['loc'], row['time'],
                row['price'], row['dist'], row['cuisine'])
            rlist.append(this_rest)


def enterNew(filename, rlist):
   response='y'
   with open(filename, 'a') as rest:
       while response=='y':
           name = input("Please enter the name: ")
           loc = input("location? ")
           time = input("average time to eat there? (in minutes) ")
           price = input("average price for 1: ")
           dist = input("distance from your home (in miles) ")
           cuisine = input("cuisine? separate by spaces ")
           rlist.append(Restaurant(name, loc, time, price, dist, cuisine))
           writer = csv.DictWriter(rest,fieldnames=attributes)
           writer.writerow({attributes[0]:name, attributes[1]:loc, attributes[2]:time, \
                            attributes[3]:price, attributes[4]:dist, attributes[5]:cuisine})
           response=input("Would you like to enter more restaurants? y/n ")


def main():
    a = input("What would you like to do? \na) get suggestions\n\
b) see all restaurants\n\
c) add restaurants\n\
d) quit\n\
please enter a, b, c or d: ")
    rlist = []
    #db="rest.csv"
    with open('rest.csv', 'r') as db:
        reader=csv.DictReader(db)
        for row in reader:
            rlist.append(Restaurant(row['name'], row['loc'], \
                                    row['time'], row['price'], \
                                    row['dist'], row['cuisine']))
                   
    while (True):
        if a is 'a':
            menu_text = '''What do you have a preference for?
            1) name
            2) location
            3) times
            4) price
            5) distance
            6) cuisine
            Enter a number: '''
            add_pref = True
        
            while add_pref:
                pref_num = int(input(menu_text)) - 1
                print("")
                print("preferences: " + str(pref_dict))
                print("")
                try:
                    pref_int = int(pref_num)
                    ask_pref(pref_int)
                except ValueError:
                    print('Sorry, please enter that again.')
                except IndexError:
                    print('Sorry, please enter that again.')
                done_add_pref = input('Done adding preferences? (Y/N): ' )
                if done_add_pref.upper() == 'Y':
                    add_pref = False
        
            print("")
            print("preferences: " + str(pref_dict))
            print("")
        
            get_suggestions()
            #print('done with main :D')
        elif a is 'c':
            #use = input("What would you like to do?")
            
            #readFile(db, rlist)
            print("Here is a list of your current restaurants")
            for restaurant in rlist:
                print(str(restaurant))
            response = input("Would you like to add more restaurants y/n ")
            if (response == 'y'):
                enterNew('rest.csv', rlist)
                #response=input("Would you like to add more restaurants y/n ")
            print("Here is a list of your current restaurants")
            for restaurant in rlist:
                print(str(restaurant))
        elif a is 'b':
            print("These are all your restaurants")
            for r in rlist:
                print(r)
        else:
            break
        a=input("What would you like to do? \na) get suggestions\n\
b) see all restaurants\n\
c) add restaurants\n\
d) quit\n\
please enter a, b, c or d: ")

def ask_pref(pref_int):
    pref_text = input("Enter your preference for " + attributes[pref_int] + ": ")
    attribute = attributes[pref_int]
    pref_dict[attribute].append(pref_text)


def find_matches(rlist, threshold):
    count = 0
    match_list = []
    for restaurant in rlist:
        match = 0
        if restaurant.name in pref_dict['name']:
            match_list.append(restaurant)
        #    match += 1
        elif restaurant.loc in pref_dict['loc']:
            match_list.append(restaurant)
        #    match += 1
        if restaurant.time in pref_dict['time']:
            match_list.append(restaurant)
         #   match += 1
        if restaurant.dist in pref_dict['dist']:
            match_list.append(restaurant)
          #  match += 1
        if restaurant.cuisine in pref_dict['cuisine']:
            match_list.append(restaurant)
         #   match += 1
        #if match >= threshold:
        #    print(str(restaurant))
         #   count += 1
    for res in match_list:
        print(res)
    if match_list ==[]:
        print("No matches found")
        #print(match_list)


def get_suggestions():
    threshold = len(pref_dict)
    rlist = []
    readFile("rest.csv", rlist)
    print("Here are your restaurant recommendations")
    find_matches(rlist, threshold)
    response = input("Would you like more restaurant recommendations? y/n ")
    while response == 'y':
        threshold -= 1
        find_matches(rlist, threshold)
        response = input("Would you like more restaurant recommendations? y/n ")


if __name__ == "__main__":
    main()

