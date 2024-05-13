num = 0
while True:
    if num == 100:
        break
    print()
    num = num + 1
print("===============")
input("press enter ")
print("===============")
print("loading")
import machine
import utime
LED  = machine.Pin(25, machine.Pin.OUT)
fire = machine.Pin(1, machine.Pin.OUT)
pizo = machine.Pin(2, machine.Pin.OUT)
sli  = machine.Pin(3, machine.Pin.OUT)
reset= machine.Pin(4, machine.Pin.OUT)
zone1= machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_DOWN)
zone2= machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_DOWN)
re_bu= machine.Pin(7, machine.Pin.IN, machine.Pin.PULL_DOWN)
pro  = machine.Pin(8, machine.Pin.IN, machine.Pin.PULL_DOWN)
drll = machine.Pin(9, machine.Pin.IN, machine.Pin.PULL_DOWN)
none = ""
fire.value(0)
pizo.value(0)
sli.value(0)
reset.value(0)
horn_dis = 0
zone1_dis= 0
zone2_dis= 0
stop_ = 0
done = 0
sliv = 0
zone1_s = ""
zone2_s = ""
zone1_n = ""
zone2_n = ""
pizo.value(1)
LED.value(1)
num = 1
utime.sleep(9)
print("loading complete")
print("===============")
#True is testing False is done
if False:
    print("WARNING THIS VERSION IS INCOMPLETE")
    print("press reset to go in the version")
    while True:
        if re_bu.value() == 1:
            break
        if pro.value() == 1:
            print("make suv and more")
            utime.sleep(.5)
#==============default==============#
#name
zone1_n = "Simplex Pull"
zone2_n = "NOTIFIER PULL"
#staus
zone1_s = "F"
zone2_s = "F"
#disable
horn_dis = 0
zone1_dis= 0
zone2_dis= 0
#================def================#
def ACK():
    pizo.value(0)
def sli_d():
    pizo.value(0)
    sli.value(1)
def reset_d():
    LED.value(1)
    fire.value(1)
    pizo.value(1)
    sli.value(1)
    reset.value(1)
    utime.sleep(1)
    fire.value(0)
    pizo.value(0)
    sli.value(0)
    reset.value(0)
    LED.value(0)
def fire_alarm(zone):
    print("FIRE ALARM ZONE " + str(zone))
    if horn_dis == 0:
        fire.value(1)
    LED.value(1)
    pizo.value(1)
    sliv = 0
    AM = input("[1]=man[2]=auto\n")
    if AM == "1":
        while True:
            ASR = input("[1]=ACK[2]=silence[3]=reset\n")
            if ASR == "1":
                ACK()
            if ASR == "2":
                sli_d()
            if ASR == "3":
                if zone1.value() == 1:
                    print("reset "+zone1_n)
                    pizo.value(1)
                elif zone2.value() == 1:
                    print("reset "+zone2_n)
                    pizo.value(1)
                else:
                    print("press reset")
                    while True:
                        if re_bu.value() == 1:
                            reset_d()
                            break
                    break
    else:
        print("[reset]=reset[pro]=ACK[drll]=silence")
        while True:
            if re_bu.value() == 1:
                if zone1.value() == 1:
                    print("reset "+zone1_n)
                    pizo.value(1)
                    utime.sleep(1)
                elif zone2.value() == 1:
                    print("reset "+zone2_n)
                    pizo.value(1)
                    utime.sleep(1)
                else:
                    print("press reset")
                    while True:
                        if re_bu.value() == 1:
                            reset_d()
                            sliv = 0
                            print("reset in system")
                            print("===============")
                            break
                    break
            if pro.value() == 1:
                ACK()
            if drll.value() == 1:
                sli_d()
                sliv = 1
            if zone1.value() == 1 and sliv == 1 and zone == 2:
                sli.value(0)
                pizo.value(1)
            if zone2.value() == 1 and sliv == 1 and zone == 1:
                sli.value(0)
                pizo.value(1)
def stop():
    fire.value(0)
    pizo.value(0)
    sli.value(0)
    reset.value(0)
def supervisory(zone):
    print("supervisory in zone "+str(zone))
    pizo.value(1)
    LED.value(1)
    print("press reset to reset")
    while True:
        if re_bu.value() == 1:
            break
    pizo.value(0)
reset_d()
print("reset in system")
print("===============")
#=====================main loop===================#
while True:
    if zone1.value() == 1:
        if zone1_s == "F":
            if zone1_dis == 0:
                print(zone1_n)
                fire_alarm(1)
                print("reset in system")
                print("===============")
        elif zone1_s == "S":
            print(zone1_n)
            supervisory(1)
    if zone2.value() == 1:
        if zone2_s == "F":
            if zone2_dis == 0:
                print(zone2_n)
                fire_alarm(2)
                print("reset in system")
                print("===============")
        elif zone2_s == "S":
            print(zone2_n)
            supervisory(2)
    if re_bu.value() == 1:
        reset_d()
        print("reset in system")
        print("===============")
    if drll.value() == 1:
        fire_alarm("DRLL")
        print("reset in system")
        print("===============")
    if pro.value() == 1:
        #=====================progarmming===========================#
        pizo.value(1)
        utime.sleep(1)
        pizo.value(0)
        WTD = input("[1]=fire_test[2]=rly_test[3]=program[4]=off[5]=delete_history[6]=EMERGENCY_RESET[7]=fire_alarm[8]=supervisory\n")
        #fire test
        if WTD == "1":
            fire_test = input("[1]=with_pizo[2]=no_pizo\n")
            if fire_test == "1":
                print("press reset to start test")
                while True:
                    if re_bu.value() == 1:
                        if horn_dis == 0:
                            fire.value(1)
                        pizo.value(1)
                        utime.sleep(3.8)
                        sli.value(1)
                        pizo.value(0)
                        reset()
                        break
            if fire_test == "2":
                print("press reset to start test")
                while True:
                    if re_bu.value() == 1:
                        if horn_dis == 0:
                            fire.value(1)
                        utime.sleep(3.8)
                        sli.value(1)
                        fire.value(0)
                        pizo.value(0)
                        sli.value(0)
                        reset.value(0)
                        break
        #rly test
        if WTD == "2":
            print("press reset to start test")
            while True:
                if re_bu.value() == 1:
                    fire.value(1)
                    pizo.value(1)
                    sli.value(1)
                    reset.value(1)
                    done = 1
                    utime.sleep(1)
                else:
                    fire.value(0)
                    pizo.value(0)
                    sli.value(0)
                    reset.value(0)
                    if done == 1:
                        done = 0
                        break
        #programming
        if WTD == "3":
            print("press reset to enter programming")
            while True:
                if re_bu.value() == 1:
                    break
            dis = input("[1]=Zone_1[2]=Zone_2[3]=horn[4]=all_on[5]=read[6]=all_fire[7]=walk_test\n")
            #ZONE 1
            if dis == "1":
                print("[1]=On[2]=Off[3]=mode[4]=rename")
                YN = input()
                if YN == "1":
                    zone1_dis = 0
                elif YN == "2":
                    zone1_dis = 1
                elif YN == "3":
                    stat = input("[1]=Fire_alarm[2]=supervisory\n")
                    if stat == "1":
                        zone1_s = "F"
                    elif stat == "2":
                        zone1_s = "S"
                elif YN == "4":
                    zone1_n = input("name\n")
            #ZONE 2
            if dis == "2":
                print("[1]=On[2]=Off[3]=mode[4]=rename")
                YN = input()
                if YN == "1":
                    zone2_dis = 0
                elif YN == "2":
                    zone2_dis = 1
                elif YN == "3":
                    stat = input("[1]=Fire_alarm[2]=supervisory\n")
                    if stat == "1":
                        zone2_s = "F"
                    elif stat == "2":
                        zone2_s = "S"
                elif YN == "4":
                    zone2_n = input("name\n")
            #horn
            if dis == "3":
                print("[1]=On[2]=Off")
                YN = input()
                if YN == "1":
                    horn_dis = 0
                else:
                    horn_dis = 1
            #all on
            if dis == "4":
                horn_dis = 0
                zone1_dis= 0
                zone2_dis= 0
            #read
            if dis == "5":
                pass
            #all fire
            if dis == "6":
                zone1_s = "F"
                zone2_s = "F"
            #walk test
            if dis == "7":
                print("press reset to exit walk test")
                while True:
                    if zone1.value() == 1:
                        print("test "+str(zone1_n))
                        fire.value(1)
                        pizo.value(1)
                        utime.sleep(1.5)
                        reset_d()
                    if zone2.value() == 1:
                        print("test "+str(zone2_n))
                        fire.value(1)
                        pizo.value(1)
                        utime.sleep(1.5)
                        reset_d()
                    if re_bu.value() == 1:
                        reset_d()
                        print("===============")
                        break
        #stop
        if WTD == "4":
            none = input("write 159 to break or press enter to do nonething\n")
            if none == "159":
                break
        #delete history
        if WTD == "5":
            while True:
                print()
                stop_ = stop_ + 1
                if stop_ == 500:
                    break
        #E-stop
        if WTD == "6":
            stop()
        #fire alarm
        if WTD == "7":
            fire_alarm("none")
        #supervisory
        if WTD == "8":
            supervisory(0)
        print("zone1 is disable "+str(zone1_dis))
        print("zone2 is disable "+str(zone2_dis))
        print("horn is disable "+str(horn_dis))
        print("zone1 mode "+str(zone1_s))
        print("zone2 mode "+str(zone2_s))
        print("zone1 name "+str(zone1_n))
        print("zone2 name "+str(zone2_n))
        print("===============")
