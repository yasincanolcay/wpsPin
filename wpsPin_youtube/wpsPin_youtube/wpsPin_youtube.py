#code=utf8

import random
from random import randint
from threading import Thread

banner = """ 
                                   ███████████   ███            
                                  ░░███░░░░░███ ░░░             
 █████ ███ █████ ████████   █████  ░███    ░███ ████  ████████  
░░███ ░███░░███ ░░███░░███ ███░░   ░██████████ ░░███ ░░███░░███ 
 ░███ ░███ ░███  ░███ ░███░░█████  ░███░░░░░░   ░███  ░███ ░███ 
 ░░███████████   ░███ ░███ ░░░░███ ░███         ░███  ░███ ░███ 
  ░░████░████    ░███████  ██████  █████        █████ ████ █████
   ░░░░ ░░░░     ░███░░░  ░░░░░░  ░░░░░        ░░░░░ ░░░░ ░░░░░ 
                 ░███                                           
                 █████                                          
                ░░░░░                                           
"""

print(banner)

i = """ 
------------------------------------------------------------------
                   WELCOME TO WPS PİN MAKER
             CREATE WPS PİN FOR WİFİ BRUTEFORCE
                      ENTER FOR START
                    [e/E]XİT FOR EXİT
------------------------------------------------------------------
"""
print(i)
print("[Deafult>>5000]")
ask_line = input("[+]>>>HOW MUCH LİNE : ")
ask_file = input("[+]PİN LİST NAME : ")
ask_start = input("[*]ENTER FOR START....")

x = 0
def pin_maker():


    try:

        if ask_start == "":

            if ask_line == "":


                for p in range(5000):

                    pin = '{}{}{}{}{}{}{}{}\n'.format(*__import__('random').sample(range(0,9),8))
                    d = "{}.txt".format(ask_file)
                    dosya = open(d,"a")
                    dosya.write(pin)
                    print(pin)

                dosya.close()


            else:

                while True:

                    pin = '{}{}{}{}{}{}{}{}\n'.format(*__import__('random').sample(range(0,9),8))
                    d = "{}.txt".format(ask_file)
                    dosya = open(d,"a")
                    dosya.write(pin)
                    print(pin)
                    global x
                    x+=1


                    if x == int(ask_line):


                        break

                    else:
                        continue


                dosya.close()
            
            
            print(banner)
            with open("{}.txt".format(ask_file), "r") as c:
                line_i = c.read().count("\n")
                line_i_w = "PİN LİST LİNE: {}".format(str(line_i))
                print(line_i_w)
            print("[CREATE SUCCESFULY GOODBYE :-) ] ")
            input("ENTER TO EXİT  OR  CTRL+C")

        elif ask_start == "e" or ask_start == "E" or ask_start == "exit" or ask_start == "Exit":


            print("[EXİT SUCCESFULLY, I WILL WAİT YOU :-) ]")

    except:

        print("[ OHH SORRY WPS PİN MAKER FAİL,PLEASE TRY RESTART :-( ]")



def exit():

    print("[EXİT SUCCESFULLY, I WILL WAİT YOU :-) ]")



if ask_line == "e" or ask_line == "E" or ask_line == "exit" or ask_line == "Exit":

    exit()

else:

    t1 = Thread(target=pin_maker)
    t1.start()


