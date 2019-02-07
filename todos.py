import item
import manager

manage = manager.Manager()

choice = input("> ")
while choice != 'quit':
    manage.interact(choice)
    choice = input("> ")
    print(" ")