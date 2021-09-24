#code=utf8
#wps pin maker
#-------------------------------------#
"""
    Olcay Software Youtube
    ücretsiz egitim videoları
 ------------------------------------
    herkes için ulaşılabilir eğitim
               YOUTUBE
"""
#-------------------------------------#

import random
from threading import Thread
import datetime
from time import sleep

Banner = """ 
                         PPPPPP  iii
ww      ww pp pp    sss  PP   PP     nn nnn
ww      ww ppp  pp s     PPPPPP  iii nnn  nn
 ww ww ww  pppppp   sss  PP      iii nn   nn
  ww  ww   pp          s PP      iii nn   nn
           pp       sss
"""
print(Banner)
ii=""" 
-----------------------------------------------
          WELCOME TO WPS PİN MAKER
   *CREATE WPS PİN LİSTS FOR WİFİ BRUTEFORCE*
             -ENTER FOR START-
            -(E/e)XİT FOR EXİT-
----------------------------------------------
"""
print(ii)
print(">>default(5000)")
line = input("[+]>>HOW MUCH DO YOU WANT TO LİNE: ")
list_name = input("[*]>>PİN LİST NAME: ")
basla = input("[+]>>>ENTER TO START: ...")
x = 0

def pin_Maker():

    try:
        if basla == "":
    
            if line == "":

                for pin in range(5000):

                    random_pin = '{}{}{}{}{}{}{}{}'.format(*__import__('random').sample(range(0,9),8))
                    doctype = "{}.txt".format(list_name)
                    save = open(doctype,"a")
                    save.write("{}\n".format(random_pin))
                    print(random_pin)
            
                save.close()
                


            elif line != "":
                print(line)
                sleep(1)
                int_line = int(line)
                global x
                while True:

                    random_pin = '{}{}{}{}{}{}{}{}'.format(*__import__('random').sample(range(0,9),8))
                    doctype = "{}.txt".format(list_name)
                    save = open(doctype,"a")
                    save.write("{}\n".format(random_pin))
                    print(random_pin)
                    x+=1
                    if x == int_line:

                        break
                    else:
                        pass
            
                save.close()


            print(Banner)
            with open("{}.txt".format(list_name), "r") as c:
                line_i = c.read().count("\n")
                line_i_w = "PİN LİST LİNE: {}".format(str(line_i))
                print(line_i_w)
            print("[CREATE SUCCESFULY GOODBYE :-) ] ")
            input("ENTER TO EXİT  OR  CTRL+C")

        elif basla == "e" or basla == "E" or basla == "exit" or basla == "Exit":

            print("[ GOODBYE :-) I WİLL WAİT YOU ]")

    except:

        print("[ OHH SORRY WPS PİN CREATOR İS FAİL PLEASE RESTART TOOL :-( ]")


def exit():


    print("[ GOODBYE :-) I WİLL WAİT YOU ]")



    
if line == "e" or line == "E":

    exit()

elif line !="e" or line !="E":

    create = Thread(target=pin_Maker)
    create.start()
 