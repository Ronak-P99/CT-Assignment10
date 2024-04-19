'''
1. Python Sets Adventure
Objective:
The aim of this assignment is to deepen your understanding and application of Python sets in various scenarios, 
ranging from basic operations to advanced manipulations and best practices. 
You will correct given codes, use sets in everyday contexts, and tackle challenges that require creative thinking and problem-solving.

Task 1: Flight Route Comparison
Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. 
You have two sets of flight destinations, one for each airline. Write a Python program to find out:

Destinations that both airlines fly to.
Destinations unique to your airline.
Whether there are any destinations that neither airline shares.
Example Code:

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
'''

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

mutual_destinations = our_routes.intersection(competitor_routes)
print(f"\nThe similar destinations are: {mutual_destinations} ")

our_destinations_only = our_routes.difference(competitor_routes)
print(f"\nThe routes that we take that our competitor don't: {our_destinations_only} ")

joint_destinations = our_routes.union(competitor_routes)
if 'ORD' in joint_destinations:
    print("\nWe have found ORD aiport in one of the routes\n")
else:
    print("\nORD not found!\n")
