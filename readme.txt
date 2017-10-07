Construct the URL of the search results from Expedia- Here is one for the available flights listed from New York to Miami –https://www.expedia.com/Flights-Search?trip=oneway&leg1=from:New%20York,%20NY%20(NYC-All%20Airports),to:Miami,%20Florida,departure:04/01/2017TANYT&passengers=children:0,adults:1,seniors:0,infantinlap:Y&mode=search

Download HTML of the search result page using Python Requests.

Parse the page using LXML – LXML lets you navigate the HTML Tree Structure using Xpaths. We have predefined the XPaths for the details we need in the code.

Save the data to a JSON file. You can later modify this to write to a database.