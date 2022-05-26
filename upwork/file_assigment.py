from time import sleep
import threading

file_dic = 'C:/Users/richa/OneDrive/Počítač/projects/programming/python/upwork/text.txt'
def last_line():
    threading.Timer(10.0, last_line).start()
    count = len(open(file_dic).readlines())
    with open(file_dic) as f:
        list = []
        for line in f:
            list.append(line)
        print(list[-1])
last_line()

'''while True:
    last_line()
    answer = str(input("Do you want to continue? yes/no\n"))
    if answer == "yes":
        pass
    elif answer == "no":
        break
    else:
        while True:
            bad_ans = str(input("Your answer was misspelled. Do you want to continue? yes/no\n"))
            if bad_ans == "yes":
                break
            elif bad_ans == "no":
                exit()
            else:
                pass
    sleep(10)'''
#from line 15 to 28 it's not nessesery but i want let user to choose wether he wants to continue or not
#also if users input is worng he is looped in while and have to write correctly yes or no
#if we comment line 13 and 6 and UNcomment 15-31 we are able to let user choose to continue or not