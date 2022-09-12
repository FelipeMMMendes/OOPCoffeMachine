from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#instancia os objetos
coffeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
menu = Menu()


#variavel flag para controlar a repeticao da maquina
machineOn = True

while machineOn == True:

    #pergunta para o usuario qual bebida ele vai querer
    drink = input((f"What would you like? {menu.get_items()}\n"))
    
    #se o usuario entrar com off, desliga a maquina
    if drink == 'off':
        machineOn = False

    #se o usuario entrar com report, mostra os status da maquina
    elif drink == 'report':
        coffeMaker.report()
        moneyMachine.report()

    else:    
        #associa a bebida ao que o usuario digitou
        drink = menu.find_drink(drink)    

        #checa se há recursos o suficiente para fazer a bebida
        if coffeMaker.is_resource_sufficient(drink) == False:
            print("Not enough ingredients available, why don't you try another drink? ")
            continue
        else:
            #chama uma funcao para contar a quantidade de dinheiro inserido
            if moneyMachine.make_payment(drink.cost):
                #faz a bebida que foi pedida
                coffeMaker.make_coffee(drink)



        



   