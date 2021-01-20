def choice():
    choice='bad choice'
    while choice.isdigit()==False:
        choice=input('give me a number, only: ')
        if choice.isdigit()==False:
            print('foo you didnt give me a number')
    return int(choice)
#choice()

from IPython.display import clear_output
clear_output()
def multipleChoice():
    choice='no dice'
    acceptableRange=range(0,10)
    withinRange=False

    while choice.isdigit()==False or withinRange==False:
        choice=input('dame un numero del 0 al 9 ')
        if choice.isdigit()==False:
            print('no seas pancho, dame un numero')
        if choice.isdigit()==True:
            if int(choice) in acceptableRange:
                withinRange=True
            pass 
    print(f'tu numero fue {choice}')
    return int(choice)

multipleChoice()
