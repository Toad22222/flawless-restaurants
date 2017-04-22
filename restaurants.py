#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 15:37:58 2017

@author: rebeccabrunsberg
"""

from collections import defaultdict
import csv

class Restaurant(object):
    
    
    def __init__(self, name, loc, time, price, dist, cuisine):
        self.name = name
        self.loc=loc
        self.time=time
        self.price=price
        self.dist=dist
        self.cuisine=cuisine
        self.fieldnames = ['name', 'loc', 'time', \
        'price', 'dist','cuisine']
        
    def __str__(self):
        return self.name
   
def readFile(filename, rlist):
    restaurants= open(filename, 'r')  
    for line in restaurants:
        data=line.split(',')
        this_rest = Restaurant(data[0], data[1], data[2], data[3], \
                               data[4], data[5])
        rlist.append(this_rest)

def enterNew(filename, rlist):
    response='y'
    r =Restaurant(1,1,1,1,1,1)
    fields=r.fieldnames
    with open(filename, 'a') as rest:
        
        while (response=='y'):
            name=input("Please enter the name: ")
            loc=input("location? ")
            time=input("average time to eat there? (in minutes) ")
            price=input("average price for 1: ")
            dist=input("distance from your home (in miles) ")
            cuisine=input("cuisine? separate by spaces ")
            rlist.append(Restaurant(name, loc, time, price, dist, cuisine))
    
            writer = csv.DictWriter(rest,fieldnames=fields)
            writer.writerow({fields[0]:name, fields[1]:loc, fields[2]:time, \
                            fields[3]:price, fields[4]:dist, fields[5]:cuisine})
            response=input("Would you like to add more restaurants y/n ")
    
def main():
    use = input("What would you like to do?)
    rlist = []
    #db="rest.csv"
    with open('rest.csv', 'r') as db:
        reader=csv.DictReader(db)
        for row in reader:
            rlist.append(Restaurant(row['name'], row['loc'], \
                                    row['time'], row['price'], \
                                    row['dist'], row['cuisine']))
    #readFile(db, rlist)
    print("Here is a list of your current restaurants")
    for restaurant in rlist:
        print(str(restaurant))
    response = input("Would you like to add more restaurants y/n ")
    if (response == 'y'):
        enterNew('rest.csv', rlist)
        response=input("Would you like to add more restaurants y/n ")
    print("Here is a list of your current restaurants")
    for restaurant in rlist:
        print(str(restaurant))
    
        
        
if __name__ == "__main__":
    main()
    