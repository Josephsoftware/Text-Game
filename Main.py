#A fully function text based game with 6 objectives and mulitple endings, using multiple dimentional dictionaries and functions.
#
# Dictionary links a rooms to each other.
import time
import os
rooms = {
        'Control Room': {'South' : 'Laboratory', 'East' : 'Dry Cask Storage', 'West' : 'Armory', 'North' : 'Work Shop'},
        'Armory': {'East' : 'Control Room'},
        'Work Shop': {'East' : 'Med Bay', 'South' : 'Control Room'},
        'Laboratory': {'North' : 'Control Room', 'East' : 'Centrifuge'},
        'Dry Cask Storage': {'West' : 'Control Room', 'North' : 'Reactor Room'},
        'Med Bay': {'West' : 'Work Shop'},
        'Centrifuge': {'West' : 'Laboratory'},
        'Reactor Room': {}

}


items = {
        'Armory': {'Hazmat Suit': 0 },
        'Work Shop': {'Hammer': 0 },
        'Laboratory': {'LN2': 0},
        'Dry Cask Storage': {'Storage Container': 0},
        'Med Bay': {'Iodine Pills' : 0},
        'Centrifuge': {'Fuel Rod': 0}

}



#Initilization of functions

def control_room():
    move = rooms['Control Room'][user_input]
    print('You entered: ' + rooms['Control Room'][user_input])
    return move

def armory():
    print('You entered: ' + rooms['Armory'][user_input])
    move = rooms['Armory'][user_input]
    return move

def work_shop():
    print('You entered: ' + rooms['Work Shop'][user_input])
    move = rooms['Work Shop'][user_input]
    return move

def laboratory():
    print('You entered: ' + rooms['Laboratory'][user_input])
    move = rooms['Laboratory'][user_input]
    return move

def dry_cask_storage():
    print('You entered: ' + rooms['Dry Cask Storage'][user_input])
    move = rooms['Dry Cask Storage'][user_input]
    return move

def med_bay():
    print('You entered: ' + rooms['Med Bay'][user_input])
    move = rooms['Med Bay'][user_input]
    return move

def centrifuge():
    print('You entered: ' + rooms['Centrifuge'][user_input])
    move = rooms['Centrifuge'][user_input]
    return move




def help():
    print('***********************************\n'
          'Collect the 6 items to win the game, or the reactor will detonate'
          '\nGo to the reactor room once you have all 6 items\n'
          '***********************************\n')
    print('***********************************\n'
          'Move Commands: North, South, West, East '
          '\nItem Commands: To pick up item type "Item Name" in the correct room, Inventory '
          '\nAux Commands: Map, help, Quit\n'
          '***********************************\n')

def inventory():
    print(list(items.values()))
def map():
    print(list(rooms[location].items()))



i=0
while i <10:

    time.sleep(0.07)
    print('loading','|')
    time.sleep(0.07)
    print('\rloading','\\')
    time.sleep(0.07)
    print('\rloading','--')
    time.sleep(0.07)
    print('\rloading','/')
    time.sleep(0.07)
    print('loading','|')
    time.sleep(0.07)
    print('\rloading','\\')
    time.sleep(0.07)
    print('\rloading','--')
    time.sleep(0.07)
    print('\rloading','/')
    time.sleep(0.07)
    i+=1
    os.system('cls')



room = str()
user_input = str()
location = 'Control Room'
print('\n \n \n'
      '***********************************\n'
      'Inventory must be called by the command listed below \n'
      'Use the map to help navigate\n'
      'Type Quit to end the game\n'
      '***********************************\n')





help()




while user_input != 'Quit':

    while rooms[location] == rooms['Control Room']:
        user_input = input('--------------------------------- \n Enter your move: \n')
        if user_input in list(rooms['Control Room']):
            location = control_room()
        elif user_input == 'help':
            help()
        elif user_input == 'Quit':
            break
        elif user_input == 'Inventory':
            inventory()
        elif user_input == 'Map':
            map()
        else:
            print('Invalid Input')


    while rooms[location] == rooms['Armory']:
        user_input = input('--------------------------------- \n Enter your move: \n')
        if user_input in list(rooms['Armory']):
            location = armory()
        elif user_input in ('North', 'South', 'East', 'West') and user_input not in list(rooms['Armory']):
            print('You Cannot go that way!')
        elif user_input in items[location] and items[location][user_input] == 0:
            items[location].update({user_input : 1})
            print('You equipped the',list(items[location])[0])
        elif user_input in items[location] and items[location][user_input] == 1:
            print('You already have the', list(items[location])[0])
        elif user_input == 'help':
            help()
        elif user_input == 'Quit':
            break
        elif user_input == 'Inventory':
            inventory()
        elif user_input == 'Map':
            map()
        else:
            print('Invalid Input')



    while rooms[location] == rooms['Work Shop']:
        user_input = input('--------------------------------- \n Enter your move: \n')
        if user_input in list(rooms['Work Shop']):
            location = work_shop()
        elif user_input in ('North', 'South', 'East', 'West') and user_input not in list(rooms['Work Shop']):
            print('You Cannot go that way!')
        elif user_input in items[location] and items[location][user_input] == 0:
            items[location].update({user_input : 1})
            print('You equipped the',list(items[location])[0])
        elif user_input in items[location] and items[location][user_input] == 1:
            print('You already have the', list(items[location])[0])
        elif user_input == 'help':
            help()
        elif user_input == 'Quit':
            break
        elif user_input == 'Inventory':
            inventory()
        elif user_input == 'Map':
            map()
        else:
            print('Invalid Input')



    while rooms[location] == rooms['Laboratory']:
        user_input = input('--------------------------------- \n Enter your move: \n')
        if user_input in list(rooms['Laboratory']):
            location = laboratory()
        elif user_input in ('North', 'South', 'East', 'West') and user_input not in list(rooms['Laboratory']):
            print('You Cannot go that way!')
        elif user_input in items[location] and items[location][user_input] == 0:
            items[location].update({user_input : 1})
            print('You equipped the',list(items[location])[0])
        elif user_input in items[location] and items[location][user_input] == 1:
            print('You already have the', list(items[location])[0])
        elif user_input == 'help':
            help()
        elif user_input == 'Quit':
            break
        elif user_input == 'Inventory':
            inventory()
        elif user_input == 'Map':
            map()
        else:
            print('Invalid Input')



    while rooms[location] == rooms['Dry Cask Storage']:
        user_input = input('--------------------------------- \n Enter your move: \n')
        if user_input in list(rooms['Dry Cask Storage']):
            location = dry_cask_storage()
        elif user_input in ('North', 'South', 'East', 'West') and user_input not in list(rooms['Dry Cask Storage']):
            print('You Cannot go that way!')
        elif user_input in items[location] and items[location][user_input] == 0:
            items[location].update({user_input : 1})
            print('You equipped the',list(items[location])[0])
        elif user_input in items[location] and items[location][user_input] == 1:
            print('You already have the', list(items[location])[0])
        elif user_input == 'help':
            help()
        elif user_input == 'Quit':
            break
        elif user_input == 'Inventory':
            inventory()
        elif user_input == 'Map':
            map()
        else:
            print('Invalid Input')



    while rooms[location] == rooms['Med Bay']:
        user_input = input('--------------------------------- \n Enter your move: \n')
        if user_input in list(rooms['Med Bay']):
            location = med_bay()
        elif user_input in ('North', 'South', 'East', 'West') and user_input not in list(rooms['Med Bay']):
            print('You Cannot go that way!')
        elif user_input in items[location] and items[location][user_input] == 0:
            items[location].update({user_input : 1})
            print('You equipped the',list(items[location])[0])
        elif user_input in items[location] and items[location][user_input] == 1:
            print('You already have the', list(items[location])[0])

        elif user_input == 'help':
            help()
        elif user_input == 'Quit':
            break
        elif user_input == 'Inventory':
            inventory()
        elif user_input == 'Map':
            map()
        else:
            print('Invalid Input')



    while rooms[location] == rooms['Centrifuge']:
        user_input = input('--------------------------------- \n Enter your move: \n')
        if user_input in list(rooms['Centrifuge']):
            location = centrifuge()
        elif user_input in ('North', 'South', 'East', 'West') and user_input not in list(rooms['Centrifuge']):
            print('You Cannot go that way!')
        elif user_input in items[location] and items[location][user_input] == 0:
            items[location].update({user_input : 1})
            print('You equipped the',list(items[location])[0])
        elif user_input in items[location] and items[location][user_input] == 1:
            print('You already have the', list(items[location])[0])
        elif user_input == 'help':
            help()
        elif user_input == 'Quit':
            break
        elif user_input == 'Inventory':
            inventory()
        elif user_input == 'Map':
            map()
        else:
            print('Invalid Input')


    if rooms[location] == rooms['Reactor Room']:
        if items['Armory']['Hazmat Suit'] == 0:
            print('You are burnt alive by radiation!\n'
                  'Game Over!')
            time.sleep(5)
            break
        if items['Laboratory']['LN2'] == 0:
            print('It is too late to go back for the LN2\n'
                  'Game Over!')
            time.sleep(5)
            break
        if items['Centrifuge']['Fuel Rod'] == 0:
            print('It is too late to go back for the Fuel Rod\n'
                  'Game Over!')
            time.sleep(5)
            break
        if items['Work Shop']['Hammer'] == 0:
            print('It is too late to go back for the Hammer\n'
                  'Game Over!')
            time.sleep(5)
            break
        if items['Med Bay']['Iodine Pills'] == 0:
            print('You poisoned by radiation\n'
                  'Game Over!')
            time.sleep(5)
            break
        if items['Dry Cask Storage']['Storage Container'] == 0:
            print('It is too late to go back for the Storage Container\n'
                  'Game Over!')
            time.sleep(5)
            break
        else:
            os.system('cls')
            time.sleep(5)
            print('Using the hammer you open the door and change the fuel rod.')
            time.sleep(5)
            os.system('cls')
            print('A noise comes from the Control room')
            time.sleep(1.4)
            print('.')
            time.sleep(1.4)
            print('.')
            time.sleep(2)
            print('.')
            time.sleep(2)
            os.system('cls')
            print('A call from Earth is flashing on the communication console')
            time.sleep(8)
            os.system('cls')
            print('You answer the phone')
            time.sleep(8)
            os.system('cls')
            i = 0
            while i < 15:
                time.sleep(1)
                print('loading','*')
                time.sleep(1)
                os.system('cls')
                print('\rloading','**')
                time.sleep(1)
                os.system('cls')
                print('\rloading', '***')
                time.sleep(1)
                os.system('cls')
                print('\rloading', '****')
                time.sleep(1)
                os.system('cls')
                print('loading', '*****')
                i += 1
                os.system('cls')
            print('Hi we have been trying to reach you about your cars extended warranty for sometime now, this will '
                  'be our last attempt to try and reach you')
            time.sleep(10)
            print('You Win')
            time.sleep(10)

            break
