# tv.py

class Television(object):

    """ a virtual television """

    # Constructor:
    def __init__(self, channel, volume, is_on):
        self.__channel = channel
        self.volume = volume
        self.is_on = is_on
        
    # String Method:
    def __str__(self):
        if self.is_on == True:
            reply = "The television is on.\n"
            reply += "Channel: " + str(self.__channel) + "\n"
            reply += "Volume: " + str(self.volume)
        else:
            reply = "The television is off."
        return reply

    # Power method, switches on and off
    def toggle_power(self):
        if self.is_on == True:
            self.is_on = False
        else:
            self.is_on = True

    # Returns channel:
    def get_channel(self):
        print self.__channel

    # Changes channel:
    def set_channel(self,new_channel):
        if new_channel >= 0 and new_channel <= 499:
            self.__channel = new_channel
        else:
            print "Could not change channels, channel was not between 0 and 499"

    # Increases volume, if not at 10:
    def raise_volume(self):
        if self.volume < 10:
            self.volume += 1
        else:
            print "Could not raise volume, volume is already at maximum (10)."

    # Decreases volume if not at 0:
    def lower_volume(self):
        if self.volume >= 1:
            self.volume -= 1
        else:
            print "Could not lower volume, volume is already at minimum (0)."

    # Property of television, since channel is private:
    @property
    def channel(self):
        return self.__channel

# Starting the menu:
def main():
    # Created a new television object:
    tv = Television(3,5,True)
    choice = None
    # Menu loop:
    while choice != "0":
        print str(tv) + \
              """
    Television Menu
    0 - Exit
    1 - Toggle Power
    2 - Change Channel
    3 - Raise Volume
    4 - Lower Volume
    """
        choice = raw_input("Choice: ")
        print
        if choice == "0":
            print "Goodbye."
        elif choice == "1":
            tv.toggle_power()
        elif choice == "2":
            new = int(raw_input("What channel do you want to switch to? "))
            tv.set_channel(new)
        elif choice == "3":
            tv.raise_volume()
        elif choice == "4":
            tv.lower_volume()
        else:
            print "\nSorry, but",choice,"is not a valid choice."

# Calling the function:
main()
        
