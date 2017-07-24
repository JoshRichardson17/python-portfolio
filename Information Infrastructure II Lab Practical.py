#creates properties
class Property(object):

    property_list = []

    #prints all current properties
    @staticmethod
    def print_all():
        print "Current Properties are:"
        for property in Property.property_list:
            print property

    #prints the most expensive property
    @staticmethod
    def most_expensive():
        print "The Most Expensive Property is:"
        print max(Property.property_list)

    #prints properties that have increased in value
    @staticmethod
    def good_investments():
        print "The Properties that are worth more now are:"
        for property in Property.property_list:
            if property.current_value > property.purchase_price:
                print property, "\n"
                
    #initializer
    def __init__(self, address, purchase_price):
        self.address = address
        self.purchase_price = purchase_price
        self.current_value = purchase_price
        self.occupied = False
        Property.property_list.append(self)

    #prints information about the Property
    def __str__(self):
        reply = "Property: " + self.address + "\n"
        reply += "Purchase Price: $" + str(self.purchase_price) + "\n"
        reply += "Current Value: $" + str(self.current_value) + "\n"
        reply += "Occupied: " + str(self.occupied) + "\n"
        return reply

    #allows properties to be compared based on current value
    def __cmp__(self, other):
        if self.current_value > other.current_value:
            return 1
        if self.current_value == other.current_value:
            return 0
        if self.current_value < other.current_value:
            return -1

    #sets occupied to the opposite of current value
    def swap(self):
        print "Swapping " + self.address + "'s Occupied Status.\n"
        if self.occupied == False:
            self.occupied = True
        elif self.occupied == True:
            self.occupied = False

#subclass of Property
class CommercialProperty(Property):

    #intializer
    def __init__(self, address, purchase_price, percentage):
        super(CommercialProperty, self).__init__(address, purchase_price)
        self.percentage = percentage

    #prints information about the CommercialProperty
    def __str__(self):
        reply = "Commercial Property: " + self.address + "\n"
        reply += "Purchase Price: $" + str(self.purchase_price) + "\n"
        reply += "Current Value: $" + str(self.current_value) + "\n"
        reply += "Occupied: " + str(self.occupied) + "\n"
        reply += "Interest Rate: " + str(self.percentage) + "%\n"
        return reply

    #updates the current value based on current value and interest rate           
    def annual_update(self):
        if self.current_value >= 200000.0:
            self.current_value += ((self.percentage/100.0)*self.current_value)
        else:
            self.current_value -= 10000
            
    

#Test Code for Part 3
store = CommercialProperty("4362 Main Street", 197502.45, 3)

print "Welcome to the I210 Real Estate Tracker!"
print "(This version was coded by Josh Richardson",
print ", with username 'richjosh')\n"
print "-"*60

print store

print "This Property loses value the first year:"
store.annual_update()
print store

store.swap()

print "The value then increases by $20000:"
store.current_value += 20000
print store

print "After 10 years:"

for i in range(10):
    store.annual_update()

print store
