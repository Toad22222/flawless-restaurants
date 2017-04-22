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


def enterNew(rlist):
   response='y'
   name = input("Please enter the name: ")
   loc = input("location? ")
   time = input("average time to eat there? (in minutes) ")
   price = input("average price for 1: ")
   dist = input("distance from your home (in miles) ")
   cuisine = input("cuisine? separate by spaces ")
   rlist.append(Restaurant(name, loc, time, price, dist, cuisine))


def main():
   use =input(“What would you like to do?\n a) get suggestions \
, b)
   menu_text = '''What do you have a preference for?
   1) name
   2) location
   3) time
   4) price
   5) distance
   6) cuisine
   Enter a number: '''
   add_pref = True

   while add_pref:
       pref_num = input(menu_text)
       print("")
       print("preferences: " + str(pref_dict))
       print("")
       try:
           pref_int = int(pref_num) - 1
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
   print('done with main :D')


def ask_pref(pref_int):
   pref_text = input("Enter your preference for " + attributes[pref_int] + ": ")
   attribute = attributes[pref_int]
   pref_dict[attribute].append(pref_text)


def find_matches(rlist, threshold):
   count = 0
   for restaurant in rlist:
       match = 0
       if restaurant.name in pref_dict['name']:
           match += 1
       if restaurant.loc in pref_dict['loc']:
           match += 1
       if restaurant.time in pref_dict['time']:
           match += 1
       if restaurant.dist in pref_dict['dist']:
           match += 1
       if restaurant.cuisine in pref_dict['cuisine']:
           match += 1
       if match >= threshold:
           print(str(restaurant))
           count += 1
   if count == 0:
       print("No matches found")


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


