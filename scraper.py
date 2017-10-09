
from selenium import webdriver
from bs4 import BeautifulSoup

#object to store flight info
class flight:
    price = ''
    departure_time = ''
    arrival_time = ''
    airline = ''
    origin = ''
    destination = ''
    def __init__(self,price,times,airline,locations):
        self.price = price
        self.departure_time=times[0]
        self.arrival_time = times[1]
        self.airline = airline
        self.origin = locations[0]
        self.destination = locations[1]


# parses each container in list of flights found
def containerParse(root):
    return flight(findPrice(root),findTime(root),findAirline(root),findLocation(root))


# finds price
def findPrice(root):
    price1 = root.find_elements_by_xpath('.//span[@class="dollars price-emphasis"]')[0].text
    price2 = root.find_elements_by_xpath('.//span[@class="cents secondary price-emphasis"]')[0].text
    return price1+price2


# finds flight time
def findTime(root):
    departure_time = root.find_elements_by_xpath('.//span[@class="departure-time departure-0-emphasis"]')[0].text
    arrival_time = root.find_elements_by_xpath('.//span[@class="arrival-time arrival-0-emphasis"]')[0].text
    return [departure_time,arrival_time]

# finds airline
def findAirline(root):
    airline = root.find_elements_by_xpath('.//div[@class="secondary truncate"]')[0].text
    return airline


# finds origin and destination
def findLocation(root):
    locations = root.find_elements_by_xpath('.//div[@class="secondary"]')[0].text
    return locations.split(" - ")


# prints details of all flights found
def printFlights(flights):
    for flight in flights:
        print("price: "+flight.price+" | Departure Time: "+flight.departure_time+" | Arrival Time: "+flight.arrival_time + " | Airline: "+flight.airline+" | "+flight.origin+" - "+flight.destination+'\n')

def main():
	driver = webdriver.Chrome()
	driver.get("https://www.expedia.com/Flights-Search?flight-type=on&starDate=10%2F15%2F2017&_xpid=11905%7C1&mode=search&trip=oneway&leg1=from%3ASan+Francisco%2C+CA+%28SFO-San+Francisco+Intl.%29%2Cto%3ALAX%2Cdeparture%3A10%2F15%2F2017TANYT&passengers=children%3A0%2Cadults%3A1%2Cseniors%3A0%2Cinfantinlap%3AY")
	results = driver.find_elements_by_xpath('//li[@class="flight-module segment offer-listing"]')
	flights = []
	for result in results:
	    flights += [containerParse(result)]
	printFlights(flights)
	driver.close()

if __name__ == "__main__": main()



