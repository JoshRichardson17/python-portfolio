import random

#creates a car object
class Car(object):
    
    def __init__(self, make, driver, player):
        #constructor
        self.drive = 0
        self.make = make
        self.driver = driver
        self.player = player

    def __str__(self):
        #defines miles traveled according to make
        if self.make.lower() == "ferrari":
            miles_traveled = random.randrange(10, 91)

        elif self.make.lower() == "porsche":
            miles_traveled = random.randrange(30, 71)

        else:
            miles_traveled = 50
        
        #defines miles traveled according to driver
        if self.driver.lower() == "tony stewart":
            self.drive += miles_traveled + 10

        else:
            if self.make.lower() == "ferrari":
                self.drive += max(random.randrange(10, 91), random.randrange(10, 91))
            if self.make.lower() == "porsche":
                self.drive += max(random.randrange(30, 71), random.randrange(30, 71))
            if self.make.lower() == "bmw":
                self.drive += 50
                
        #returns the miles traveled for the appropriate player
        if self.player == 1:
            return "Player 1 has driven " + str(self.drive) + " miles."
        else:
            return "Player 2 has driven " + str(self.drive) + " miles."

#main
print "Welcome to the race!\n" + "-"*40
print "Each player, please select your car and driver."
print "Cars are BMW, Porsche, and Ferrari"
print "Drivers are Mario Andretti and Tony Stewart"

#gets player 1's make from the user
while True:
    p1car = raw_input("Player 1, please enter your car: ")
    if p1car.lower() not in ("bmw", "ferrari", "porsche"):
        print "Sorry, that's not a valid car option."
        continue
    else:
        break
#gets player 1's driver from the user
while True:
    p1driver = raw_input("Player 1, please enter your driver: ")
    if p1driver.lower() not in ("mario andretti", "tony stewart"):
        print "Sorry, that's not a valid driver option."
        continue
    else:
        break    

#gets player 2's make from the user
while True:
    p2car = raw_input("Player 2, please enter your car: ")
    if p2car.lower() not in ("bmw", "ferrari", "porsche"):
        print "Sorry, that's not a valid car option."
        continue
    else:
        break

#gets player 2's driver from the user    
while True:
    p2driver = raw_input("Player 2, please enter your driver: ")
    if p2driver.lower() not in ("mario andretti", "tony stewart"):
        print "Sorry, that's not a valid driver option."
        continue
    else:
        break

#creates the cars
player1 = Car(p1car, p1driver, 1)
player2 = Car(p2car, p2driver, 2)

#lap counter
lapcount = 0

#runs the race and returns the winner
while True:
    lapcount += 1
    print "Lap: " + str(lapcount)
    print player1
    print player2
    if player1.drive or player2.drive >= 500:
        if player1.drive and player2.drive >= 500:
            if player1.drive == max(player1.drive, player2.drive):
                print "Congratulations! Player 1 with " + player1.driver.title() + " driving a " + player1.make + ", you are the winner!"
            if player2.drive == max(player1.drive, player2.drive):
                print "Congratulations! Player 2 with " + player2.driver.title() + " driving a " + player2.make + ", you are the winner!"
            break            
        elif player1.drive >= 500:
            print "Congratulations! Player 1 with " + player1.driver.title() + " driving a " + player1.make + ", you are the winner!"
            break
        elif player2.drive >= 500:
            print "Congratulations! Player 2 with " + player2.driver.title() + " driving a " + player2.make + ", you are the winner!"
            break








