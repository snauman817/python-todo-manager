from manager import Manager

manage = Manager()

choice = input("> ")
while choice != 'quit':
    manage.interact(choice)
    choice = input("> ")
    print(" ")

manage.save()