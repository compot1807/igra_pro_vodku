import pgzrun
import time
import sys
import random
import math
from turtle import *
import os
import gamepad
import re



BULLET_SPEED = 10

def shoot_bullet():
    if bullet_fired:
        if ashoot==1:
            bullet.x -= BULLET_SPEED
        elif ashoot==2:
            bullet.x += BULLET_SPEED
        elif ashoot==3:
            bullet.y += BULLET_SPEED
        elif ashoot==4:
            bullet.y -= BULLET_SPEED




TITLE = " "
WIDTH = 1200
HEIGHT = 780

luntik_hp = 240000#96000

luntic = Actor("luntic.png")
luntic.x = 600
luntic.y = 400

luntic_copy = Actor("luntic.png")
luntic_copy.x = 600
luntic_copy.y = 400

def update_copy():
    if luntic_copy.colliderect(pin) or luntic_copy.colliderect(nyanya):
        if random.randint(1,tpch) == 1:
            if random.randint(1,4) == 1:
##                sounds.inecraft_portal.play()
                luntic_copy.x += 200
            elif random.randint(1,4) == 2:
##                sounds.inecraft_portal.play()
                luntic_copy.x -= 200
            elif random.randint(1,4) == 3:
##                sounds.inecraft_portal.play()
                luntic_copy.y += 200
            elif random.randint(1,4) == 4:
##                sounds.inecraft_portal.play()
                luntic_copy.y -= 200
    if not luntic_copy.colliderect(crosh) and not luntic_copy.colliderect(egik) and not luntic_copy.colliderect(pin) and not luntic_copy.colliderect(nyanya):
        if random.randint(1,4) == 1:
            luntic_copy.x += lunsd
        elif random.randint(1,4) == 2:
            luntic_copy.x -= lunsd
        elif random.randint(1,4) == 3:
            luntic_copy.y += lunsd
        elif random.randint(1,4) == 4:
            luntic_copy.y -= lunsd
    if luntic_copy.colliderect(crosh) or luntic_copy.colliderect(egik) or luntic_copy.colliderect(pin) or luntic_copy.colliderect(nyanya):
        if random.randint(1,4) == 1:
            luntic_copy.x += lunsd
        elif random.randint(1,4) == 2:
            luntic_copy.x -= lunsd
        elif random.randint(1,4) == 3:
            luntic_copy.y += lunsd
        elif random.randint(1,4) == 4:
            luntic_copy.y -= lunsd
    if luntic_copy.x < 0:
        luntic_copy.x = 600
##        sounds.inecraft_portal.play()
    elif luntic_copy.x > WIDTH:
        luntic_copy.x = 600
##        sounds.inecraft_portal.play()
    elif luntic_copy.y < 0:
        luntic_copy.y = 400
##        sounds.inecraft_portal.play()
    elif luntic_copy.y > HEIGHT:
        luntic_copy.y = 400


egik = Actor("egik.png")
egik.x = 300
egik.y = 400
ehp = 3000

pin = Actor("pin.png")
pin.x = 100
pin.y = 400
pihp=1400


nyanya = Actor("nyanya.png")
nyanya.x = 100
nyanya.y = 200
nhp=4000

crosh = Actor("crosh3.png")
crosh.x = 300
crosh.y = 200
chp=2600

weapons = ["gun","sword","katana"]
weapon = "gun"


sword = Actor("sword_final")
sword.x = crosh.x
sword.y = crosh.y
sangle = 0
sangle_b = 1

gun = Actor("gun")
gun.x = crosh.x
gun.y = crosh.y

UP = 180
U_L = 225
DOWN = 0
D_L = 315
LEFT = 270
U_R = 135
RIGHT = 90
D_R = 45

sova = Actor("sova.png")
sova.x = 500
sova.y = 600
shp=2000

voron = Actor("sova.png")
voron.y = 600
voron.x = 800





r_list=[]


class rocket2_1(Actor):
    def __init__(self,ang2):
        super().__init__("rocket")
        self.ang2 = ang2
        self.hp = 2
    def ubdrock2(self):
        if self.ang2 == 1:
            self.y+=rocket_speed
            self.angle=DOWN
        if self.ang2 == 2:
            self.x+=rocket_speed
            self.angle=RIGHT
        if self.ang2 == 3:
            self.x-=rocket_speed
            self.angle=LEFT
        if self.ang2 == 4:
            self.y-=rocket_speed
            self.angle=UP


r_list3 = []

def ubdrock2r():
    global chp,nhp,ehp,pihp,sum_blocked_dmg
    for r in r_list3:
        r.ubdrock2()
        if r.colliderect(crosh): #and r.ang==1:
            chp -=20
            sum_blocked_dmg+=20
            r_list3.remove(r)
        elif r.colliderect(pin):# and r.ang==3:
            pihp -=20
            sum_blocked_dmg+=20
            r_list3.remove(r)
        elif r.colliderect(egik):# and r.ang==2:
            ehp -=20
            sum_blocked_dmg+=20
            r_list3.remove(r)
        elif r.colliderect(nyanya):# and r.ang==4:
            nhp -=20
            sum_blocked_dmg+=20
            r_list3.remove(r)
        if r.ang2 == 1 and r.y ==HEIGHT:
            r_list3.remove(r)
        if r.ang2 == 2 and r.x ==WIDTH:
            r_list3.remove(r)
        if r.ang2 == 3 and r.x ==0:
            r_list3.remove(r)
        if r.ang2 == 4 and r.y ==0:
            r_list3.remove(r)





def create_rocket():
    if len(r_list)<13 and len(r_list3) <13:
        if fase2:
            angnr = random.randint(1,4)
            r = rocket2_1(angnr)
            if angnr==1:
                r.x = random.randint(20,1180)
                r.y = 0
            if angnr==2:
                r.y = random.randint(20,760)
                r.x = 0
            if angnr==3:
                r.y = random.randint(20,760)
                r.x = WIDTH
            if angnr==4:
                r.x = random.randint(20,760)
                r.y = HEIGHT
            r_list3.append(r)
        else:
            r = Actor("rocket.png")
            r.x = random.randint(20,1180)
            r.y = 0
            r_list.append(r)


bullet = Actor("bulletblue")
bullet.x = -10
bullet.y = -10
bullet_fired = False
ashoot=1

cosa = Actor("cosa.png")
cosa_broshena = False


message_n = 0
message_in_ugol = "С силой этой косы я стал богом! И несколько существ не помешают мне!"

def message1():
    global message_in_ugol
    message_in_ugol = ""

def message2():
    global message_in_ugol
    message_in_ugol = "Я использовал только часть сил!"

def message3():
    global message_in_ugol
    message_in_ugol = "Это ещё не конец!"

def draw():
    global luntik_hp,game_end
    if not fase2:
        screen.blit("background.jpg", (0,0))
    else:
        screen.blit("background2.png",(0,0))
    for r in r_list2:
        r.draw()
    for z in r_list:
        z.draw()
    for r in r_list3:
        r.draw()
    if ehp > 0:
        egik.draw()
        screen.draw.text("INFANTRYMAN HEALTH:" + str(ehp), (970,100))
    else:
        screen.draw.text("INFANTRYMAN HEALTH: 0" , (970,100),color="red")
    if pihp > 0:
        pin.draw()
        screen.draw.text("Fhtk HEALTH: " + str(pihp), (750,140), fontname="some")
    else:
         screen.draw.text("Fhtk :( HEALTH: 0" , (750,140),color="red",fontname="some")
    if nhp > 0:
        nyanya.draw()
        screen.draw.text("KNIGHT HEALTH:" + str(nhp), (1000,60))
    else:
         screen.draw.text("KNIGHT HEALTH: 0" , (1000,60),color="red")
    if chp > 0:
        crosh.draw()
        screen.draw.text("YOUgan HEALTH:" + str(chp), (1000,180))
    else:
         screen.draw.text("YOUgan HELTH: 0" , (1000,180),color="red")
    if shp > 0:
        sova.draw()
        screen.draw.text("MEDICINA HEALTH:" + str(shp), (1000,220))
    else:
         screen.draw.text("MEDICINA HEALTH: 0" , (1000,220),color="red")

    frect = Rect((195, 15), (610, 30))
    screen.draw.filled_rect(frect, "gray")
    rect = Rect((200, 20), (round(luntik_hp/2400.00,1)*6, 20))
    screen.draw.filled_rect(rect, "red")
    if luntik_hp > 96000:
        screen.draw.text("HEZIM HEALTH:" + str(round(luntik_hp/2400.00,1)) + "%", (400,22.5),color="black")
    else:
        screen.draw.text("HEZIM: FASE 2:   " + str(round(luntik_hp/2400.00,1)) + "%", (400,22.5),color="black")
    screen.draw.text(message_in_ugol,(100,700),color="red")
    bullet.draw()
    luntic.draw()
    bullet.draw()
    if chp > 0:
        if weapon == "sword":
            sword.draw()
        elif weapon == "gun":
            gun.draw()
    if is_hilled:
        luntic_copy.draw()
##    voron.draw()
##    laser.draw()
    if cosa_broshena == True:
        cosa.draw()
    if luntik_hp <= 0:
        if not game_end:
            endgame()
            game_end = True
        screen.fill("blue")
        screen.draw.text(f"GAME OVER!\n   You win! ",  (350, 150))
        screen.draw.text(f"The damage is done:" + str(sum_damage),  (300, 200))
        screen.draw.text(f"Total damage done:" + str(super_sum_damage),  (300, 250))

        screen.draw.text(f"Health restored:" + str(sum_heal),  (300, 300))
        screen.draw.text(f"All health has been restored:" + str(super_sum_heal),  (300, 350))

        screen.draw.text(f"Damage received::" + str(sum_blocked_dmg),  (300, 400))
        screen.draw.text(f"Total damage received:" + str(super_sum_blocked_dmg),  (300, 450))

        music.stop()
    if chp <=0 and nhp <= 0 and ehp <= 0 and pihp <= 0:
        if not game_end:
            endgame()
            game_end = True
        screen.fill("blue")
        screen.draw.text(f"GAME OVER! You lose! ",  (350, 150))



        music.stop()

game_end = False
super_sum_damage=0
super_sum_heal=0
super_sum_blocked_dmg=0


def endgame():
    global super_sum_blocked_dmg,super_sum_damage,super_sum_heal
    with open(os.environ["appdata"] + "\\igraprocosu\\stat.txt","w+") as stat:
        pass
    with open(os.environ["appdata"] + "\\igraprocosu\\stat.txt","r+") as stat:
        sttext = stat.read()
        text_stat = re.split("\n",sttext)
        try:
            ear_dmg=int(text_stat[0])
            ear_heal=int(text_stat[1])
            ear_block=int(text_stat[2])
        except:
            ear_dmg=0
            ear_heal=0
            ear_block=0
    with open(os.environ["appdata"] + "\\igraprocosu\\stat.txt","w+") as stat:
        super_sum_damage = ear_dmg + sum_damage
        super_sum_heal = ear_heal + sum_heal
        super_sum_blocked_dmg = ear_block + sum_blocked_dmg
        stat.write(str(super_sum_damage) + "\n" + str(super_sum_heal) + "\n" + str(super_sum_blocked_dmg) + "\n")




rocket_speed = 0.3
fase2 = False


lunsd = 10
atch = 70
ldmg = 10

tpch = 100

def mus2():
    music.stop()
    music.play("soundtrack2")
##    clock.schedule(mus3,30)

def mus3():
    music.stop()
    music.play("mus_f_part2.ogg")
    clock.schedule(mus2,27)

zashita = 0
cosachance = 900

def fase2_enter():
    global fase2,luntic,lunsd,rocket_speed,atch,ldmg,tpch,zashita,cosachance
    fase2 = True
    music.stop()
    sounds.mus_f_newlaugh_low.play()
    clock.schedule(mus2,4)
    luntic=Actor("luntic2.png")
    rocket_speed = 1
    lunsd = 15
    atch = 65
    ldmg = 12
    tpch = 75
    cosachance = 400
    zashita = -10
r_list2 = []

class rocket2(Actor):
    def __init__(self,ang):
        super().__init__("rocket2")
        self.ang=ang
        self.hp=2
    def update_rocket(self):
        if self.ang == 1:
            if chp <= 0:
                self.ang+=1
            self.angle = self.angle_to(crosh)
            if self.x < crosh.x:
                self.x += 0.8
            if self.y < crosh.y:
                self.y += 0.8
            if self.x > crosh.x:
                self.x -= 0.8
            if self.y > crosh.y:
                self.y -= 0.8
        elif self.ang == 2:
            if ehp <= 0:
                self.ang+=1
            self.angle = self.angle_to(egik)
            if self.x < egik.x:
                self.x += 0.8
            if self.y < egik.y:
                self.y += 0.8
            if self.x > egik.x:
                self.x -= 0.8
            if self.y > egik.y:
                self.y -= 0.8
        elif self.ang == 3:
            if pihp <= 0:
                self.ang+=1
            self.angle = self.angle_to(pin)
            if self.x < pin.x:
                self.x += 0.8
            if self.y < pin.y:
                self.y += 0.8
            if self.x > pin.x:
                self.x -= 0.8
            if self.y > pin.y:
                self.y -= 0.8
        elif self.ang == 4:
            if nhp <= 0:
                self.ang=1
            self.angle = self.angle_to(nyanya)
            if self.x < nyanya.x:
                self.x += 0.8
            if self.y < nyanya.y:
                self.y += 0.8
            if self.x > nyanya.x:
                self.x -= 0.8
            if self.y > nyanya.y:
                self.y -= 0.8

def createrock2sup():
    ran = random.randint(1,4)
    r = rocket2(ran)
    r.x = luntic.x
    r.y = luntic.y
    r_list2.append(r)
    clock.schedule(lambda x: r_list2.remove(r),5)


def create_rocket2():
    if fase2:
        if len(r_list2) < 5:
            ran = random.randint(1,4)
            r = rocket2(ran)
            r.x = random.randint(0,WIDTH)
            r.y = random.randint(0,HEIGHT)
            r_list2.append(r)
            clock.schedule(lambda x: r_list2.remove(r),5)
    else:
        return




def voron_update_f1():
    global shp,chp,pihp,ehp,nhp
    if voron.x < 0:
##        sounds.inecraft_portal.play()
        voron.x = 600
    if voron.x > WIDTH:
##        sounds.inecraft_portal.play()
        voron.x = 600
    if voron.y < 0:
##        sounds.inecraft_portal.play()
        voron.y = 400
    if voron.y > HEIGHT:
##        sounds.inecraft_portal.play()
        voron.y = 400
    if random.randint(1,4)==1:
        voron.x +=15
    elif random.randint(1,4)==2:
        voron.x -=15
    elif random.randint(1,4)==3:
        voron.y +=15
    elif random.randint(1,4)==4:
        voron.y -=15

    if random.randint(1,100)==1:
        u = random.randint(1,6)
        if u == 1:
            chp+=20
        elif u == 2:
            ehp+=20
        elif u == 3:
            nhp+=20
        elif u == 4:
            pihp+=20
        elif u == 5 or u==6:
            shp += 10

def voron_update_f2():
    global cosa_broshena

is_hilled = False


countercos = 0
cosaang = 0
cosspx = 0
cosspy = 0

def brosit():
    global cosa_broshena,countercos,cosaang,cosspx,cosspy
    cosa_broshena = True
    if not fase2:
        luntic.image = "lunticbez.png"
    else:
        luntic.image = "lunticbez2.png"
    cosa.x = luntic.x
    cosa.y = luntic.y
    cosaang = random.randint(1,8)
    countercos = 100
    if cosaang == 1:
        cosspx = 0
        cosspy = 10
    if cosaang == 2:
        cosspx = 0
        cosspy = -10
    if cosaang == 3:
        cosspx = 10
        cosspy = 0
    if cosaang == 4:
        cosspx = -10
        cosspy = 0


    if cosaang == 5:
        cosspx = -10
        cosspy = -10
    if cosaang == 6:
        cosspx = 10
        cosspy = -10
    if cosaang == 7:
        cosspx = 10
        cosspy = 10
    if cosaang == 8:
        cosspx = -10
        cosspy = 10

cosspl = 0

def vzatcosu():
    global cosa_broshena,cosspl,cosspx,cosspy
    if cosa_broshena != False:
        cosa_broshena = False
        if not fase2:
            luntic.image = "luntic.png"
        else:
            luntic.image = "luntic2.png"
        cosspx = 0
        cosspy = 0
        cosspl = 0


joy = gamepad.XboxController()

def on_key_up(key,mod):
    global weapon
    if key == keys.F:
        if weapon == "gun":
            weapon = "sword"
        elif weapon == "sword":
            weapon = "gun"
##    print(key)


sum_damage = 0
sum_heal = 0
sum_blocked_dmg = 0



def update_luntic():
    global ehp,shp,pihp,chp,nhp,sum_blocked_dmg,sum_damage,sum_heal
    if not luntic.colliderect(crosh) and not luntic.colliderect(egik) and not luntic.colliderect(pin) and not luntic.colliderect(nyanya):
        if random.randint(1,4) == 1:
            luntic.x += lunsd
        elif random.randint(1,4) == 2:
            luntic.x -= lunsd
        elif random.randint(1,4) == 3:
            luntic.y += lunsd
        elif random.randint(1,4) == 4:
            luntic.y -= lunsd
    if luntic.colliderect(crosh) or luntic.colliderect(egik) or luntic.colliderect(pin) or luntic.colliderect(nyanya):
        if random.randint(1,4) == 1:
            luntic.x += lunsd
        elif random.randint(1,4) == 2:
            luntic.x -= lunsd
        elif random.randint(1,4) == 3:
            luntic.y += lunsd
        elif random.randint(1,4) == 4:
            luntic.y -= lunsd
    if luntic.x < 0:
        luntic.x = 600
##        sounds.inecraft_portal.play()
    elif luntic.x > WIDTH:
        luntic.x = 600
##        sounds.inecraft_portal.play()
    elif luntic.y < 0:
        luntic.y = 400
##        sounds.inecraft_portal.play()
    elif luntic.y > HEIGHT:
        luntic.y = 400
##        sounds.inecraft_portal.play()
    if luntic.colliderect(crosh):
        if random.randint(1,atch) == 1:
            chp -= ldmg
            sum_blocked_dmg+=ldmg
    if luntic.colliderect(egik):
        if random.randint(1,atch) == 1:
            ehp -= ldmg
            sum_blocked_dmg+=ldmg
    if luntic.colliderect(nyanya):
        if random.randint(1,atch) == 1:
            nhp -= ldmg
            sum_blocked_dmg+=ldmg
    if luntic.colliderect(pin):
        if random.randint(1,atch) == 1:
            pihp -= ldmg
            sum_blocked_dmg+=ldmg
    if luntic.colliderect(sova):
        if random.randint(1,atch) == 1:
            shp -= ldmg
            sum_blocked_dmg+=ldmg


def update():
    global luntik_hp,chp,nhp,ehp,pihp,shp,bullet_fired,ashoot,luntic,rocket_speed,fase2,is_hilled,message_n,cosspx,cosspy,countercos,cosa_broshena,cosspl,sangle,sangle_b,weapon,sum_damage,sum_blocked_dmg,sum_heal
##    clock.schedule(shoot_bullet, 5)
    if not game_end:
        shoot_bullet()
        create_rocket()
        create_rocket2()
        ubdrock2r()
        cosa.angle += 1
        update_copy()

        joy_control = joy.read()

        if chp > 0:
            if weapon == "sword":
                sword.x = crosh.x
                sword.y = crosh.y
            elif weapon == "gun":
                gun.x = crosh.x
                gun.y = crosh.y

    ##    if keyboard.f or joy_control[3]:
    ##        if weapon == "gun":
    ##            weapon = "sword"
    ##        elif weapon == "sword":
    ##            weapon = "gun"

        if cosa_broshena and cosa.colliderect(crosh):
            chp-=1
            sum_blocked_dmg+=1
        if cosa_broshena and cosa.colliderect(egik):
            ehp-=1
            sum_blocked_dmg+=1
        if cosa_broshena and cosa.colliderect(nyanya):
            nhp-=1
            sum_blocked_dmg+=1
        if cosa_broshena and cosa.colliderect(pin):
            pihp-=1
            sum_blocked_dmg+=1
        if cosa_broshena and cosa.colliderect(sova):
            shp-=1
            sum_blocked_dmg+=1






        if countercos > 0:
            if cosaang == 1:
                cosa.y += cosspy
                cosspy -= 0.1
                countercos -= 1
            if cosaang == 2:
                cosa.y += cosspy
                cosspy += 0.1
                countercos -= 1

            if cosaang == 3:
                cosa.x += cosspx
                cosspx -= 0.1
                countercos -= 1
            if cosaang == 4:
                cosa.x += cosspx
                cosspx += 0.1
                countercos -= 1



            if cosaang == 5:
                cosa.x += cosspx
                cosspx += 0.1
                cosa.y += cosspy
                cosspy += 0.1
                countercos -= 1
            if cosaang == 6:
                cosa.x += cosspx
                cosspx -= 0.1
                cosa.y += cosspy
                cosspy += 0.1
                countercos -= 1
            if cosaang == 7:
                cosa.x += cosspx
                cosspx -= 0.1
                cosa.y += cosspy
                cosspy -= 0.1
                countercos -= 1
            if cosaang == 8:
                cosa.x += cosspx
                cosspx += 0.1
                cosa.y += cosspy
                cosspy -= 0.1
                countercos -= 1
        elif countercos >= 0 and cosa_broshena:
            if cosa.x < luntic.x:
                cosa.x+=cosspl
            if cosa.x > luntic.x:
                cosa.x-=cosspl
            if cosa.y < luntic.y:
                cosa.y+=cosspl
            if cosa.y > luntic.y:
                cosa.y-=cosspl
            cosspl += 0.1
            if cosa.colliderect(luntic):
                clock.schedule(vzatcosu,0.8)
        elif cosa_broshena==False:
            if not fase2:
                luntic.image = "luntic.png"
            else:
                luntic.image = "luntic2.png"




        if cosa_broshena == False and random.randint(1,cosachance) == 1:
            brosit()

        if message_n == 0:
            message_n = 1
            clock.schedule(message1,7)
        if message_n == 1 and fase2:
            message_n = 2
            message2()
            clock.schedule(message1,7)
        if not is_hilled and luntik_hp <= 2400:
            is_hilled = True
            luntik_hp = 72000
            message3()
            clock.schedule(message1,7)
        if fase2:
            voron_update_f2()
        else:
            voron_update_f1()
        for r in r_list2:
            r.update_rocket()
            if r.colliderect(crosh): #and r.ang==1:
                chp -=50
                sum_blocked_dmg+=50
                r_list2.remove(r)
            elif r.colliderect(pin):# and r.ang==3:
                pihp -=50
                sum_blocked_dmg+=50
                r_list2.remove(r)
            elif r.colliderect(egik):# and r.ang==2:
                ehp -=50
                sum_blocked_dmg+=50
                r_list2.remove(r)
            elif r.colliderect(nyanya):# and r.ang==4:
                nhp -=50
                sum_blocked_dmg+=50
                r_list2.remove(r)
        if fase2 and random.randint(1,500)==1:
            luntic.x = random.randint(0,WIDTH)
            luntic.y = random.randint(0,HEIGHT)
        if luntik_hp < 96000 and fase2 != True:
            fase2_enter()
        for z in r_list:
            z.y += rocket_speed
            if z.colliderect(crosh) and chp > 0:
                chp -=20
                sum_blocked_dmg+=20
                r_list.remove(z)
            elif z.colliderect(pin) and pihp > 0:
                pihp -=20
                sum_blocked_dmg+=20
                r_list.remove(z)
            elif z.colliderect(nyanya) and nhp > 0:
                nhp -=20
                sum_blocked_dmg+=20
                r_list.remove(z)
            elif z.colliderect(egik) and ehp > 0:
                ehp -=20
                sum_blocked_dmg+=20
                r_list.remove(z)
    ##        elif z.colliderect(sova) and shp > 0:
    ##            shp -=20
    ##            r_list.remove(z)
            if z.y > HEIGHT:
                r_list.remove(z)


        if (keyboard.right or joy_control[0] > 0):
            crosh.angle=RIGHT
        if (keyboard.left or joy_control[0] < 0):
            crosh.angle=LEFT
        if (keyboard.up or joy_control[1] > 0):
            crosh.angle=UP
        if (keyboard.down or  joy_control[1] < 0):
            crosh.angle=DOWN

        if (keyboard.right or joy_control[0] > 0) and not crosh.x >= WIDTH:
            crosh.x+=2
        if (keyboard.left or joy_control[0] < 0) and not crosh.x <= 0:
            crosh.x-=2
        if (keyboard.up or joy_control[1] > 0) and not crosh.y <= 0:
            crosh.y-=2
        if (keyboard.down or  joy_control[1] < 0) and not crosh.y >= HEIGHT:
            crosh.y+=2

        if chp >0:
            if (keyboard.space or joy_control[2]) and weapon == "gun":
                if not bullet_fired:
                    bullet_fired = True
                    if crosh.angle == LEFT:
                        bullet.x = crosh.x-30
                        bullet.y = crosh.y
                        bullet.angle = LEFT
                        ashoot=1

                    elif crosh.angle == RIGHT:
                        bullet.x = crosh.x+30
                        bullet.y = crosh.y
                        bullet.angle = RIGHT
                        ashoot=2

                    elif crosh.angle == DOWN:
                        bullet.x = crosh.x
                        bullet.y = crosh.y + 30
                        bullet.angle = DOWN
                        ashoot=3

                    elif crosh.angle == UP:
                        bullet.x = crosh.x
                        bullet.y = crosh.y - 30
                        bullet.angle = UP
                        ashoot=4
            elif (keyboard.space or joy_control[2]) and weapon == "sword":
                if sangle_b:
                    sangle += 3
                    if sangle >= 80:
                        sangle_b = 0
                else:
                    sangle -= 3
                    if sangle <= -80:
                        sangle_b = 1
                if sword.colliderect(luntic):
                    luntik_hp -= 20
            sword.angle = crosh.angle + sangle
            gun.angle = crosh.angle
    ##        if crosh.colliderect(luntic) and keyboard.space:
    ##            luntik_hp -=3
        if bullet.x >= WIDTH or bullet.x <=0 or bullet.y >=HEIGHT or bullet.y <=0:
                bullet_fired = False
                bullet.x = -10
                bullet.y = -10
        if bullet.colliderect(luntic):
            luntik_hp -= 15 - zashita
            sum_damage += 15 - zashita
            bullet_fired = False
            bullet.x = -10
            bullet.y = -10
        for r in r_list2:
            if bullet.colliderect(r):
                r.hp -=1
                bullet_fired=False
                bullet.x = -10
                bullet.y = -10
                if r.hp == 1:
                    r.image = "rocket2_2"
                if r.hp == 0:
                    r_list2.remove(r)
        for r in r_list3:
            if bullet.colliderect(r):
                r.hp -=1
                bullet_fired=False
                bullet.x = -10
                bullet.y = -10
                if r.hp == 1:
                    r.image = "rocket1_2"
                if r.hp == 0:
                    r_list3.remove(r)

        rnalx = int()
        realx = int()
        rpalx = int()

        rnaly = int()
        realy = int()
        rpaly = int()

        rnacx = int()
        reacx = int()
        rpacx = int()

        rnacy = int()
        reacy = int()
        rpacy = int()

        if nyanya.x > luntic.x:
            rnalx = nyanya.x - luntic.x
        if nyanya.x < luntic.x:
            rnalx = luntic.x -nyanya.x
        if nyanya.x == luntic.x:
            rnalx = 0
        if nyanya.y > luntic.y:
            rnaly = nyanya.y - luntic.y
        if nyanya.y < luntic.y:
            rnaly = luntic.y -nyanya.y
        if nyanya.y == luntic.y:
            rnaly = 0

        if nyanya.x > luntic_copy.x:
            rnacx = nyanya.x - luntic_copy.x
        if nyanya.x < luntic_copy.x:
            rnacx = luntic_copy.x -nyanya.x
        if nyanya.x == luntic_copy.x:
            rnacx = 0
        if nyanya.y > luntic_copy.y:
            rnacy = nyanya.y - luntic_copy.y
        if nyanya.y < luntic_copy.y:
            rnacy = luntic_copy.y -nyanya.y
        if nyanya.y == luntic_copy.y:
            rnacy = 0



        if not is_hilled:
            if nyanya.x < luntic.x:
                nyanya.x += 1
            if nyanya.y < luntic.y:
                nyanya.y += 1
            if nyanya.x > luntic.x:
                nyanya.x -= 1
            if nyanya.y > luntic.y:
                nyanya.y -= 1
        else:
            if math.sqrt(rnalx*rnalx + rnaly*rnaly) < math.sqrt(rnacx*rnacx + rnacy*rnacy):
                if nyanya.x < luntic.x:
                    nyanya.x += 1
                if nyanya.y < luntic.y:
                    nyanya.y += 1
                if nyanya.x > luntic.x:
                    nyanya.x -= 1
                if nyanya.y > luntic.y:
                    nyanya.y -= 1
            if math.sqrt(rnalx*rnalx + rnaly*rnaly) > math.sqrt(rnacx*rnacx + rnacy*rnacy):
                if nyanya.x < luntic_copy.x:
                    nyanya.x += 1
                if nyanya.y < luntic_copy.y:
                    nyanya.y += 1
                if nyanya.x > luntic_copy.x:
                    nyanya.x -= 1
                if nyanya.y > luntic_copy.y:
                    nyanya.y -= 1


        if nhp >0:
            if nyanya.colliderect(luntic):
                luntik_hp -= 5 - zashita
                sum_damage += 5 - zashita



        if egik.x > luntic.x:
            realx = egik.x - luntic.x
        if egik.x < luntic.x:
            realx = luntic.x -egik.x
        if egik.x == luntic.x:
            realx = 0
        if egik.y > luntic.y:
            realy = egik.y - luntic.y
        if egik.y < luntic.y:
            realy = luntic.y -egik.y
        if egik.y == luntic.y:
            realy = 0

        if egik.x > luntic_copy.x:
            reacx = egik.x - luntic_copy.x
        if egik.x < luntic_copy.x:
            reacx = luntic_copy.x -egik.x
        if egik.x == luntic_copy.x:
            reacx = 0
        if egik.y > luntic_copy.y:
            reacy = egik.y - luntic_copy.y
        if egik.y < luntic_copy.y:
            reacy = luntic_copy.y -egik.y
        if egik.y == luntic_copy.y:
            reacy = 0



        if not is_hilled:
            if egik.x < luntic.x:
                egik.x += 3
            if egik.y < luntic.y:
                egik.y += 3
            if egik.x > luntic.x:
                egik.x -= 3
            if egik.y > luntic.y:
                egik.y -= 3
        else:
            if math.sqrt(realx*realx + realy*realy) < math.sqrt(reacx*reacx + reacy*reacy):
                if egik.x < luntic.x:
                    egik.x += 3
                if egik.y < luntic.y:
                    egik.y += 3
                if egik.x > luntic.x:
                    egik.x -= 3
                if egik.y > luntic.y:
                    egik.y -= 3
            if math.sqrt(realx*realx + realy*realy) > math.sqrt(reacx*reacx + reacy*reacy):
                if egik.x < luntic_copy.x:
                    egik.x += 3
                if egik.y < luntic_copy.y:
                    egik.y += 3
                if egik.x > luntic_copy.x:
                    egik.x -= 3
                if egik.y > luntic_copy.y:
                    egik.y -= 3
    ##    if egik.x < luntic.x:
    ##        egik.x += 3
    ##    if egik.y < luntic.y:
    ##        egik.y += 3
    ##    if egik.x > luntic.x:
    ##        egik.x -= 3
    ##    if egik.y > luntic.y:
    ##        egik.y -= 3


        if ehp >0:
            if egik.colliderect(luntic):
                luntik_hp -= 1 - zashita
                sum_damage += 1 - zashita


        if pin.x > luntic.x:
            rpalx = pin.x - luntic.x
        if pin.x < luntic.x:
            rpalx = luntic.x -pin.x
        if pin.x == luntic.x:
            rpalx = 0
        if pin.y > luntic.y:
            rpaly = pin.y - luntic.y
        if pin.y < luntic.y:
            rpaly = luntic.y -pin.y
        if pin.y == luntic.y:
            rpaly = 0

        if pin.x > luntic_copy.x:
            rpacx = pin.x - luntic_copy.x
        if pin.x < luntic_copy.x:
            rpacx = luntic_copy.x -pin.x
        if pin.x == luntic_copy.x:
            rpacx = 0
        if pin.y > luntic_copy.y:
            rpacy = pin.y - luntic_copy.y
        if pin.y < luntic_copy.y:
            rpacy = luntic_copy.y -pin.y
        if pin.y == luntic_copy.y:
            rpacy = 0



        if not is_hilled:
            if pin.x < luntic.x:
                pin.x += 0.5
            if pin.y < luntic.y:
                pin.y += 0.5
            if pin.x > luntic.x:
                pin.x -= 0.5
            if pin.y > luntic.y:
                pin.y -= 0.5
        else:
            if math.sqrt(rpalx*rpalx + rpaly*rpaly) < math.sqrt(rpacx*rpacx + rpacy*rpacy):
                if pin.x < luntic.x:
                    pin.x += 0.5
                if pin.y < luntic.y:
                    pin.y += 0.5
                if pin.x > luntic.x:
                    pin.x -= 0.5
                if pin.y > luntic.y:
                    pin.y -= 0.5
            if math.sqrt(rpalx*rpalx + rpaly*rpaly) > math.sqrt(rpacx*rpacx + rpacy*rpacy):
                if pin.x < luntic_copy.x:
                    pin.x += 0.5
                if pin.y < luntic_copy.y:
                    pin.y += 0.5
                if pin.x > luntic_copy.x:
                    pin.x -= 0.5
                if pin.y > luntic_copy.y:
                    pin.y -= 0.5
    ##    if pin.x < luntic.x:
    ##        pin.x += 0.5
    ##    if pin.y < luntic.y:
    ##        pin.y += 0.5
    ##    if pin.x > luntic.x:
    ##        pin.x -= 0.5
    ##    if pin.y > luntic.y:
    ##        pin.y -= 0.5



        if pihp >0:
            if pin.colliderect(luntic):
                luntik_hp -= 8 - zashita
                sum_damage += 8 - zashita


        update_luntic()
##        if luntic.colliderect(pin) or luntic.colliderect(nyanya):
##            if random.randint(1,tpch) == 1:
##                if random.randint(1,4) == 1:
##    ##                sounds.inecraft_portal.play()
##                    luntic.x += 200
##                elif random.randint(1,4) == 2:
##    ##                sounds.inecraft_portal.play()
##                    luntic.x -= 200
##                elif random.randint(1,4) == 3:
##    ##                sounds.inecraft_portal.play()
##                    luntic.y += 200
##                elif random.randint(1,4) == 4:
##    ##                sounds.inecraft_portal.play()
##                    luntic.y -= 200
##        if not luntic.colliderect(crosh) and not luntic.colliderect(egik) and not luntic.colliderect(pin) and not luntic.colliderect(nyanya):
##            if random.randint(1,4) == 1:
##                luntic.x += lunsd
##            elif random.randint(1,4) == 2:
##                luntic.x -= lunsd
##            elif random.randint(1,4) == 3:
##                luntic.y += lunsd
##            elif random.randint(1,4) == 4:
##                luntic.y -= lunsd
##        if luntic.colliderect(crosh) or luntic.colliderect(egik) or luntic.colliderect(pin) or luntic.colliderect(nyanya):
##            if random.randint(1,4) == 1:
##                luntic.x += lunsd
##            elif random.randint(1,4) == 2:
##                luntic.x -= lunsd
##            elif random.randint(1,4) == 3:
##                luntic.y += lunsd
##            elif random.randint(1,4) == 4:
##                luntic.y -= lunsd
##        if luntic.x < 0:
##            luntic.x = 600
##    ##        sounds.inecraft_portal.play()
##        elif luntic.x > WIDTH:
##            luntic.x = 600
##    ##        sounds.inecraft_portal.play()
##        elif luntic.y < 0:
##            luntic.y = 400
##    ##        sounds.inecraft_portal.play()
##        elif luntic.y > HEIGHT:
##            luntic.y = 400
##    ##        sounds.inecraft_portal.play()
##        if luntic.colliderect(crosh):
##            if random.randint(1,atch) == 1:
##                chp -= ldmg
##                sum_blocked_dmg+=ldmg
##        if luntic.colliderect(egik):
##            if random.randint(1,atch) == 1:
##                ehp -= ldmg
##                sum_blocked_dmg+=ldmg
##        if luntic.colliderect(nyanya):
##            if random.randint(1,atch) == 1:
##                nhp -= ldmg
##                sum_blocked_dmg+=ldmg
##        if luntic.colliderect(pin):
##            if random.randint(1,atch) == 1:
##                pihp -= ldmg
##                sum_blocked_dmg+=ldmg
##        if luntic.colliderect(sova):
##            if random.randint(1,atch) == 1:
##                shp -= ldmg
##                sum_blocked_dmg+=ldmg

        if random.randint(1,4)==1:
            sova.x +=15
        elif random.randint(1,4)==2:
            sova.x -=15
        elif random.randint(1,4)==3:
            sova.y +=15
        elif random.randint(1,4)==4:
            sova.y -=15

        if sova.x < 0:
    ##        sounds.inecraft_portal.play()
            sova.x = 600
        if sova.x > WIDTH:
    ##        sounds.inecraft_portal.play()
            sova.x = 600
        if sova.y < 0:
    ##        sounds.inecraft_portal.play()
            sova.y = 400
        if sova.y > HEIGHT:
    ##        sounds.inecraft_portal.play()
            sova.y = 400

        if shp > 0:
            if random.randint(1,100)==1:
                u = random.randint(1,6)
                if u == 1:
                    chp+=20
                    sum_heal+=20
                elif u == 2:
                    ehp+=20
                    sum_heal+=20
                elif u == 3:
                    nhp+=20
                    sum_heal+=20
                elif u == 4:
                    pihp+=20
                    sum_heal+=20
                elif u == 5 or u==6:
                    shp += 10
                    sum_heal+=10
        if sova.colliderect(luntic):
            if random.randint(1,100) == 1:
                if random.randint(1,4) == 1:
    ##                sounds.inecraft_portal.play()
                    sova.x += 200
                elif random.randint(1,4) == 2:
    ##                sounds.inecraft_portal.play()
                    sova.x -= 200
                elif random.randint(1,4) == 3:
    ##                sounds.inecraft_portal.play()
                    sova.y += 200
                elif random.randint(1,4) == 4:
    ##                sounds.inecraft_portal.play()
                    sova.y -= 200



def loading():


    t1 = Turtle()

    t1.speed(0)
    t1.shape("turtle")
    t1.ht()

    colors = ["red", "blue","green","yellow"]

    bgcolor("black")

    t1.speed(0)
    t1.ht()
    x=10
    t1.color(random.choice(colors))
    for i in range(180):
      t1.fd(x)
      t1.bk(x)
      t1.rt(1)
      x+=2
      t1.color(random.choice(colors))
    t1.color(random.choice(colors))
    bgcolor("black")
    x=10
    for i in range(180):
      t1.fd(x)
      t1.bk(x)
      t1.rt(1)
      x+=2
      t1.color(random.choice(colors))
    bye()

##is_hilled=True
try:
    os.mkdir(os.environ["appdata"] + "\\igraprocosu")
except FileExistsError:
    pass
sounds.golos.play()
music.play("soundtrack.mp3")
pgzrun.go()