#made by deviousname
#GNU Affero General Public License v3.0
#no permission to sell

import crewmate #login credentials, requires a Reddit account, open crewmate.py and put your info there

import keyboard #https://pypi.org/project/keyboard/
import pyautogui #https://pyautogui.readthedocs.io/en/latest/

import random 
import time 
import copy
import itertools
from itertools import cycle 
from ast import literal_eval as make_tuple

import subprocess
import numpy as np
from numpy import sqrt 

from PIL import ImageGrab #https://pillow.readthedocs.io/en/stable/
from PIL import Image
from PIL import ImageChops

from selenium import webdriver #https://selenium-python.readthedocs.io/
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

default_speed = .04
pyautogui.PAUSE = default_speed

class Sus_Bot():
    def __init__ (self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        self.login()
        self.load_colors()
        self.hotkeys()
        self.marker = None
        self.txty, self.bxby = None, None
        self.colorfilter = [None, None, None, None, None, None, None, None, None]
        self.ocean = [(204, 204, 204)]
        self.logos = True
        self.z = 1
        self.trunk_h = (3,4,5,6,7,8,9)
        self.trunk_hc = cycle(self.trunk_h)
        self.rgb = self.paint.values()
        self.rgb_list = list(self.rgb)
        self.palettedata = list(itertools.chain(*self.rgb_list))
        self.full_work_order = {}
        self.full_work_order2 = {}
        self.rect_fwo_list = []
        
    def hotkeys(self):
        keyboard.unhook_all()
        time.sleep(1)
        print("Hotkeys on. Press F8 to pause.")
        keyboard.on_press(self.onkeypress)
        keyboard.add_hotkey('`', lambda: self.get_coordinate())
        keyboard.add_hotkey('r', lambda: self.randtrees())
        keyboard.add_hotkey('k', lambda: self.randmongus())
        keyboard.add_hotkey("w+space", lambda: self.rainbowbrush(0))
        keyboard.add_hotkey("w+d+space", lambda: self.rainbowbrush(1))
        keyboard.add_hotkey("d+space", lambda: self.rainbowbrush(2))
        keyboard.add_hotkey("d+s+space", lambda: self.rainbowbrush(3))
        keyboard.add_hotkey("s+space", lambda: self.rainbowbrush(4))
        keyboard.add_hotkey("s+a+space", lambda: self.rainbowbrush(5))
        keyboard.add_hotkey("a+space", lambda: self.rainbowbrush(6))
        keyboard.add_hotkey("a+w+space", lambda: self.rainbowbrush(7))
        keyboard.add_hotkey("q+space", lambda: self.rainbowbrush(8))
        keyboard.add_hotkey('0', lambda: self.removefilters())
        keyboard.add_hotkey('y', lambda: self.zone(1))
        keyboard.add_hotkey('u', lambda: self.zone(2))
        keyboard.add_hotkey(']', lambda: self.zone(3))
        keyboard.add_hotkey('[', lambda: self.marker_toggle())
        keyboard.add_hotkey('shift+{', lambda: self.marker_toggle_remove())
        keyboard.add_hotkey('p', lambda: self.randpasteimg())
        keyboard.add_hotkey("'", lambda: self.rectangle_scatter())
        keyboard.add_hotkey(';', lambda: self.rectangle_alt_scatter())
        keyboard.add_hotkey('shift+P', lambda: self.loop_randpasteimg())
        keyboard.add_hotkey('shift+"', lambda: self.loop_rectangle_scatter())
        keyboard.add_hotkey('shift+:', lambda: self.loop_rectangle_alt_scatter())
        keyboard.add_hotkey('x', lambda: self.toggle_logos())
        keyboard.add_hotkey('f8', lambda: self.sus_pause())
        keyboard.add_hotkey('home', lambda: self.reset_page())
        
    def login(self):
        #login sequence
        self.driver.get("https://pixelplace.io/api/sso.php?type=2&action=login")
        self.driver.find_element(By.ID,'loginUsername').send_keys(crewmate.username)
        self.driver.find_element(By.ID,'loginPassword').send_keys(crewmate.password)
        self.driver.find_elements(By.XPATH,'/html/body/div/main/div[1]/div/div[2]/form/fieldset')[4].click()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div[2]/form/div/input'))).click()
        #remove pixeplace fluff
        try:
            WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH,'/html/body/div[5]/div[2]/a/img'))).click()
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[8]/a[2]/div[3]/button[2]'))).click()
        except:
            pass
        print('Logged in, loading colors now...')
        #activate tracking (premium users)
        #keyboard.press_and_release('l, t')
        return
        
    def load_colors(self):
        self.paint = {
            "white":(255,255,255), "grey1":(196,196,196), "grey2":(136,136,136), "grey3":(85,85,85),
            "grey4":(34,34,34), "black":(0,0,0), "green1":(0,102,0), "green2":(34,177,76),
            "green3":(2,190,1),"green4":(81,225,25), "green5":(148,224,68), "yellow1":(251,255,91),
            "yellow2":(229,217,0), "yellow3":(230,190,12), "yellow4":(229,149,0), "brown1":(160,106,66),
            "brown2":(153,83,13), "brown3":(99,60,31),"red1":(107,0,0), "red2":(159,0,0), "red3":(229,0,0),
            "orange":(255,57,4), "brown4":(187,79,0), "peach1":(255,117,95), "peach2":(255,196,159),
            "peach3":(255,223,204), "pink1":(255,167,209),"pink2":(207,110,228), "pink3":(236,8,236),
            "pink4":(130,0,128), "purple":(81,0,255), "blue1":(2,7,99), "blue2":(0,0,234),
            "blue3":(4,75,255), "blue4":(101,131,207), "blue5":(54,186,255),
            "blue6":(0,131,199), "blue7":(0,211,221), "cyan":(69,255,200)
            }
        self.color = {}
        for a, b in zip(self.paint.keys(),range(0,39)):      
             self.path = self.driver.find_elements(By.XPATH,'//*[@id="palette-buttons"]/a')[b]
             self.color.update({f"{a}":self.path}) #Example: self.color.get('white').click() 
        
        self.color8 = (self.color.get('white'),self.color.get('grey1'),self.color.get('grey3'),self.color.get('grey4'),self.color.get('black'),
                  self.color.get('green1'),self.color.get('green2'),self.color.get('green3'),self.color.get('green4'),self.color.get('green5'),
                  self.color.get('yellow1'),self.color.get('yellow2'),self.color.get('yellow3'),self.color.get('yellow4'),
                  self.color.get('brown1'),self.color.get('brown2'),self.color.get('brown3'),self.color.get('red1'),self.color.get('red2'),self.color.get('red3'),
                  self.color.get('orange'),self.color.get('brown4'),self.color.get('peach1'),self.color.get('peach2'),self.color.get('peach3'),
                  self.color.get('pink1'),self.color.get('pink2'),self.color.get('pink3'),self.color.get('pink4'),self.color.get('purple'),
                  self.color.get('blue1'),self.color.get('blue2'),self.color.get('blue3'),self.color.get('blue4'),
                  self.color.get('blue5'),self.color.get('blue6'),self.color.get('blue7'),self.color.get('cyan'))
        self.colors_cycle8 = cycle(self.color8)
        
        self.color7 = (self.color.get('blue1'),self.color.get('blue2'),self.color.get('blue3'),self.color.get('blue4'),
                       self.color.get('blue5'),self.color.get('blue6'),self.color.get('blue7'),self.color.get('cyan'))
        self.colors_cycle7 = cycle(self.color7)
        
        self.color6 = (self.color.get('black'),self.color.get('white'))
        self.colors_cycle6 = cycle(self.color6)
        
        self.color5 = (self.color.get('brown1'),self.color.get('brown2'),self.color.get('brown3')
                       ,self.color.get('brown4'),self.color.get('grey4'),self.color.get('peach3'))
        self.colors_cycle5 = cycle(self.color5)
        
        self.color4 = (self.color.get('brown1'),self.color.get('brown2'),self.color.get('brown3'),self.color.get('brown4'))
        self.colors_cycle4 = cycle(self.color4)
        
        self.color3 = (self.color.get('grey4'),self.color.get('grey3'),self.color.get('grey2'),self.color.get('grey1'))
        self.colors_cycle3 = cycle(self.color3)
        
        self.color2 = (self.color.get('yellow1'),self.color.get('yellow2'),self.color.get('yellow3'),self.color.get('yellow4'))
        self.colors_cycle2 = cycle(self.color2)
        
        self.color1 = (self.color.get('green1'),self.color.get('green2'),self.color.get('green3')
                       ,self.color.get('green4'),self.color.get('green5'))
        self.colors_cycle1 = cycle(self.color1)
        
        self.color0 = (self.color.get('red1'),self.color.get('red2'),self.color.get('red3'))
        self.colors_cycle0 = cycle(self.color0)
        
        self.cyclerlist = (self.colors_cycle0, self.colors_cycle1, self.colors_cycle2,
                           self.colors_cycle3, self.colors_cycle4, self.colors_cycle5,
                           self.colors_cycle6, self.colors_cycle7, self.colors_cycle8)
        
        self.tree_trunks = [self.paint.get('brown1'), self.paint.get('brown2'), self.paint.get('brown3'),
                       self.paint.get('brown4'), self.paint.get('grey4'), self.paint.get('peach3')]

        self.leaves = [self.paint.get('green1'), self.paint.get('green2'), self.paint.get('green3'),
                  self.paint.get('green4'), self.paint.get('green5')]
        
        self.trees = self.tree_trunks + self.leaves        
        print('Colors loaded.')
        return
    
    def rainbowbrush(self, hotkey):
        if hotkey == hotkey:
            try:
                next(self.cyclerlist[hotkey]).click()
            except:
                self.load_colors()
                
    def visibility_state(self):
        self.curcol = None
        try:
            vis = self.driver.execute_script("return document.visibilityState") == "visible"
        except:
            self.driver.switch_to.window(driver.window_handles[0])
            vis = self.driver.execute_script("return document.visibilityState") == "visible"
        if vis == False:
            p = self.driver.current_window_handle
            chwd = self.driver.window_handles
            for w in chwd:
                if(w!=p):
                    self.driver.switch_to.window(w)
            self.curcol = str(self.driver.find_element(By.XPATH,'/html/body/div[3]/div[2]').get_attribute("style"))
        else:
            self.curcol = str(self.driver.find_element(By.XPATH,'/html/body/div[3]/div[2]').get_attribute("style"))
            
    def getcurcolor(self):
        self.visibility_state()
        a = self.curcol.find('(')
        b = self.curcol.find(')');b+=1
        self.curcol = self.curcol[a:b]
        self.curcol = [make_tuple(self.curcol)]
        return

    def getcurcolorhotkey(self, col):
        self.getcurcolor()
        self.colorfilter[col-1] = self.curcol[0]
        print('Equipped {} to slot {}'.format(self.curcol[0], col))
        time.sleep(1)
        return
    
    def removefilters(self):
        self.colorfilter[0:] = None, None, None, None, None, None, None, None, None
        print("Filters dequipped.")
        time.sleep(1)

    def marker_toggle(self):
        self.marker = pyautogui.position()
        print (f'Mark set at: x={self.marker[0]},y={self.marker[1]}')
        time.sleep(.1)

    def marker_toggle_remove(self):
        self.marker = None
        print ('Marker removed.')
        time.sleep(.1)
    
    def copyimg(self):
        self.empty_work_order = { "white":{}, "grey1":{}, "grey2":{}, "grey3":{},
                        "grey4":{}, "black":{}, "green1":{}, "green2":{},
                        "green3":{},"green4":{}, "green5":{}, "yellow1":{},
                        "yellow2":{}, "yellow3":{}, "yellow4":{}, "brown1":{},
                        "brown2":{}, "brown3":{},"red1":{}, "red2":{}, "red3":{},
                        "orange":{}, "brown4":{}, "peach1":{}, "peach2":{},
                        "peach3":{}, "pink1":{},"pink2":{}, "pink3":{},
                        "pink4":{}, "purple":{}, "blue1":{}, "blue2":{},
                        "blue3":{}, "blue4":{}, "blue5":{},
                        "blue6":{}, "blue7":{}, "cyan":{} }            
        element = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[3]')
        self.driver.execute_script("placeholder.style.display = 'none';",element)
        image = pyautogui.screenshot(region=(self.txty[0], self.txty[1], self.bxby[0], self.bxby[1]))
        self.RANGE1, self.RANGE2 = self.bxby[0] - self.txty[0], self.bxby[1] - self.txty[1]
        self.full_work_order.clear()
        self.full_work_order2.clear()
        self.full_work_order=copy.deepcopy(self.empty_work_order.copy())
        self.full_work_order2=copy.deepcopy(self.empty_work_order.copy())
        self.px1 = image.load()
        for X in range(self.RANGE1):
            for Y in range(self.RANGE2):
                c = self.px1[X, Y]
                if c not in self.paint.keys() and c not in self.colorfilter and c != (204,204,204):
                    abc = self.closest_color(c[0],c[1],c[2])
                    self.full_work_order[list(self.paint.keys())[list(self.paint.values()).index(abc)]].update({(X,Y):(abc)})
                elif c in self.paint.keys() and c not in self.colorfilter:
                    self.full_work_order[list(self.paint.keys())[list(self.paint.values()).index(c[0],c[1],c[2])]].update({(X,Y):(c[0],c[1],c[2])})
        print(f'A {self.RANGE1} by {self.RANGE2} zone has been created.')
        return
    
    def closest_color(self, r, g, b): #thank you hbot000 for this function :) h for homie
        color_diffs = []
        for cr, cg, cb in zip(*[iter(self.palettedata)]*3):
            color_diff = sqrt(abs(r - cr)**2 + abs(g - cg)**2 + abs(b - cb)**2)
            color_diffs.append((color_diff, (cr, cg, cb)))
        return min(color_diffs)[1]
    
    def randpasteimg(self):
        if self.bxby and self.txty != None:
            try:
                if self.marker != None:
                    x1, y1 = self.marker
                else:
                    x1, y1 = pyautogui.position()
                self.disable_color_block()
                image2 = pyautogui.screenshot(region=(x1 - int(self.RANGE1/2), y1 - int(self.RANGE2/2), self.RANGE1, self.RANGE2))
                self.px2 = image2.load()    
                for X in range(self.RANGE1):
                    for Y in range(self.RANGE2):
                        r, g, b = self.px2[X, Y]
                        if (r, g, b) in self.paint.values() and (r, g, b) not in self.colorfilter:
                            self.full_work_order2[list(self.paint.keys())[list(self.paint.values()).index((r, g, b))]].update({(X,Y):(r,g,b)})
                self.work_order = {}
                for i in self.full_work_order:
                    for e in self.full_work_order[i]:
                        self.fwo = dict(self.full_work_order[i].items() - self.full_work_order2[i].items())
                        self.work_order.update({i:self.fwo})                
                for i in self.work_order:
                    if self.work_order[i] != {}:
                        self.newdict = dict(self.work_order[i])
                        self.color.get(i).click()
                        self.newdictR = {}
                        for item, value in random.sample(list(self.newdict.items()), len(self.newdict)):
                            self.newdictR.update({(item):(value)})                
                        for j in self.newdictR:
                            if self.px2[j[0],j[1]] != self.ocean[0]:
                                pyautogui.click(x1 + j[0] - int(self.RANGE1/2), y1 + j[1] - int(self.RANGE2/2))
                            if keyboard.is_pressed("j"):
                                pyautogui.moveTo(x1, y1)
                                self.full_work_order2.clear()
                                self.full_work_order2=copy.deepcopy(self.empty_work_order.copy())
                                return
                pyautogui.moveTo(x1, y1)
                self.full_work_order2.clear()
                self.full_work_order2=copy.deepcopy(self.empty_work_order.copy())
            except:
                self.load_colors()
                self.randpasteimg()
        return

    def loop_randpasteimg(self):
        while True:
            self.randpasteimg()
            if keyboard.is_pressed("j"):
                break
    
    def rectangle(self):
        try:
            self.getcurcolor()
            self.RANGE1, self.RANGE2 = self.bxby[0] - self.txty[0], self.bxby[1] - self.txty[1]
            self.scrnsht = pyautogui.screenshot(region=(self.txty[0], self.txty[1], self.bxby[0], self.bxby[1]))
            keyboard.press('space')
            for A in range(self.RANGE1):
                for B in range(self.RANGE2):
                    pix = self.scrnsht.getpixel((A, B))
                    if pix not in self.ocean + self.curcol + self.colorfilter:
                        pyautogui.moveTo(A + self.txty[0], B + self.txty[1])
                        if keyboard.is_pressed("j"):
                            keyboard.release('space')
                            return
            keyboard.release('space')
        except:
            self.load_colors()
            self.rectangle()

    def loop_rectangle(self):
        while True:
            self.rectangle()
            if keyboard.is_pressed("j"):
                break
            
    def rectangle_scatter(self):
        try:
            self.rect_fwo_list.clear()
            self.getcurcolor()
            self.RANGE1, self.RANGE2 = self.bxby[0] - self.txty[0], self.bxby[1] - self.txty[1]
            self.disable_color_block()
            self.scrnsht = pyautogui.screenshot(region=(self.txty[0], self.txty[1], self.bxby[0], self.bxby[1]))
            self.px1 = self.scrnsht.load()
            self.rect_fwo_list = []
            for X in range(self.RANGE1):
                for Y in range(self.RANGE2):
                    c = self.px1[X, Y]
                    if c not in self.ocean + self.curcol + self.colorfilter:
                        self.rect_fwo_list.append((X, Y)) 
            random.shuffle(self.rect_fwo_list)
            for i in self.rect_fwo_list:
                pyautogui.click(i[0]+self.txty[0], i[1]+self.txty[1])
                self.rect_fwo_list.pop()
                if keyboard.is_pressed("j"):
                    return
        except:
            self.load_colors()
            self.rectangle_scatter()
            
    def loop_rectangle_scatter(self):
        while True:
            self.rectangle_scatter()
            if keyboard.is_pressed("j"):
                break

    def rectangle_alt(self):
        try:
            self.RANGE1, self.RANGE2 = self.bxby[0] - self.txty[0], self.bxby[1] - self.txty[1]
            self.scrnsht = pyautogui.screenshot(region=(self.txty[0], self.txty[1], self.bxby[0], self.bxby[1]))
            keyboard.press('space')
            for A in range(self.RANGE1):
                for B in range(self.RANGE2):            
                    if self.scrnsht.getpixel((A, B)) in self.colorfilter:
                        pyautogui.moveTo(A + self.txty[0], B + self.txty[1])
                        if keyboard.is_pressed("j"):
                            keyboard.release('space')
                            return
            keyboard.release('space')
        except:
            self.load_colors()
            self.rectangle_alt()
            
    def loop_rectangle_alt(self):
        while True:
            self.rectangle_alt()
            if keyboard.is_pressed("j"):
                break

    def rectangle_alt_scatter(self):
        try:
            self.rect_fwo_list.clear()
            self.RANGE1, self.RANGE2 = self.bxby[0] - self.txty[0], self.bxby[1] - self.txty[1]
            self.disable_color_block()
            self.scrnsht = pyautogui.screenshot(region=(self.txty[0], self.txty[1], self.bxby[0], self.bxby[1]))
            self.px1 = self.scrnsht.load()
            self.rect_fwo_list = []
            for X in range(self.RANGE1):
                for Y in range(self.RANGE2):
                    c = self.px1[X, Y]
                    if c in self.colorfilter:
                        self.rect_fwo_list.append((X, Y)) 
            random.shuffle(self.rect_fwo_list)
            for i in self.rect_fwo_list:
                pyautogui.click(i[0]+self.txty[0], i[1]+self.txty[1])
                self.rect_fwo_list.pop()
                if keyboard.is_pressed("j"):
                    return
        except:
            self.load_colors()
            self.rectangle_alt_scatter()


    def loop_rectangle_alt_scatter(self):
        while True:
            self.rectangle_alt_scatter()
            if keyboard.is_pressed("j"):
                break

    def zone(self, hotkey):
        if hotkey == 1:
            self.txty = pyautogui.position()
            print (f'Top-left mark created at {self.txty}')
            try:
                if self.bxby[0] > self.txty[0] and self.bxby[1] > self.txty[1]:
                    print ('Zone ready.')
            except:
                pass
        if hotkey == 2:
            self.bxby = pyautogui.position()
            print (f'Bottom-right mark created at {self.bxby}')
            try:
                if self.bxby[0] > self.txty[0] and self.bxby[1] > self.txty[1]:
                    print ('Zone ready.')
            except:
                pass
        if hotkey == 3:
            if self.txty != None and self.bxby != None and self.txty[0] < self.bxby[0] and self.txty[1] < self.bxby[1]:
                self.copyimg()
                    
    def randmongus(self): #?????????????
        try:
            pyautogui.PAUSE = .06 #slow down the drawing speed as to not skip pixels
            while True:
                self.xr = random.randrange(self.txty[0],self.bxby[0])
                self.yr = random.randrange(self.txty[1],self.bxby[1])
                self.pix = ImageGrab.grab().getpixel((self.xr, self.yr))
                if self.pix not in self.ocean + self.colorfilter:
                    pyautogui.moveTo(self.xr,self.yr)
                    self.mongus()
                if keyboard.is_pressed("j"):
                    keyboard.release('space')
                    pyautogui.PAUSE = default_speed #return to normal speed
                    break            
        except:
            self.load_colors()
            self.randmongus()
        return
            
    def mongus(self): #draws mongus
        x, y = pyautogui.position()
        next(self.colors_cycle8).click()
        keyboard.press('space')
        for _ in range(2):
            pyautogui.moveTo(x, y)
            pyautogui.moveTo(x + self.z*2, y)
            y -= 1
        for _ in range(2):
            pyautogui.moveTo(x, y)
            pyautogui.moveTo(x, y + 1)
            x += self.z
        y = y + 2
        for _ in range(2):
            pyautogui.moveTo(x, y)
            pyautogui.moveTo(x + self.z, y - 2)
            y -= 1
        for _ in range(2):
            pyautogui.moveTo(x, y)
            y -= 1
        for _ in range(3):
            pyautogui.moveTo(x, y)
            x -= self.z
        x += self.z*2
        y += 1
        pyautogui.moveTo(x,y)
        self.color.get('cyan').click()
        pyautogui.moveRel(-self.z,0)
        keyboard.release('space')
        self.z = -self.z
            
    def randtrees(self):
        try:
            pyautogui.PAUSE = .05 #slow down the drawing speed as to not skip pixels
            while True:
                self.xr = random.randrange(self.txty[0],self.bxby[0])
                self.yr = random.randrange(self.txty[1],self.bxby[1])
                self.pix = ImageGrab.grab().getpixel((self.xr, self.yr))
                if self.pix not in self.colorfilter + self.trees + self.ocean:
                    pyautogui.moveTo(self.xr,self.yr)
                    if random.random() >= 0.5: #50/50 chance                    
                        self.trees_1()
                    else:
                        self.trees_alt()
                if keyboard.is_pressed("j"):
                    keyboard.release('space')
                    pyautogui.PAUSE = default_speed #return to normal speed
                    break
        except:
            self.load_colors()
            self.randtrees()
        return
        
    def trees_1(self):#draws trees
        x, y = pyautogui.position()
        next(self.colors_cycle5).click() #trunk
        keyboard.press('space')
        for _ in range(3):
            pyautogui.moveTo(x, y)
            y -= 1
        if self.z > 0:
            for _ in range(1):
                pyautogui.moveTo(x, y)
                y -= 1
        pyautogui.moveTo(x, y)
        next(self.colors_cycle1).click() #leaves
        pyautogui.moveTo(x - self.z, y)
        pyautogui.moveTo(x + self.z, y)
        pyautogui.moveTo(x, y - 1)
        y -= 1
        pyautogui.moveTo(x - self.z, y)
        pyautogui.moveTo(x + self.z, y)
        pyautogui.moveTo(x, y - 1)
        keyboard.release('space')
        return

    def trees_alt(self):#draws different trees
        x, y = pyautogui.position()
        keyboard.press('space')
        next(self.colors_cycle5).click() #trunk
        for i in range(next(self.trunk_hc)):
            y -= 1
            pyautogui.moveTo(x, y)
        next(self.colors_cycle1).click() #leaves
        for i in range(5):
            pyautogui.moveTo(x + i-2, y)
        for i in range(5):
            pyautogui.moveTo(x + i-2, y-1)
        for i in range(3):
            pyautogui.moveTo(x + i-1, y-2)
        pyautogui.moveTo((x, y-3))
        keyboard.release('space')
        return

    def reset_page(self): #resets pixelplace to freshly loaded and zoom level 1
        self.visibility_state()
        self.driver.get("https://pixelplace.io/7-pixels-world-war")
        self.load_colors()
        #keyboard.press_and_release('l,t')
        return

    def sus_pause(self):
        keyboard.unhook_all()
        print("Hotkeys off. You may safely type now. Press F8 to reactivate.")
        time.sleep(1)
        keyboard.add_hotkey('f8', lambda: self.hotkeys())
        return
    
    def get_coordinate(self):
        coord_element = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[4]').text
        print(type(coord_element))
        print(coord_element)
        coord_element = make_tuple(coord_element)
        print(type(coord_element))
        print(coord_element)
        
    def disable_color_block(self):
        e1 = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[2]')
        e2 = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[3]')
        self.driver.execute_script("arguments[0].style.display = 'none';",e1)
        self.driver.execute_script("arguments[0].style.display = 'none';",e2)
    
    def toggle_logos(self): #toggles guild war logos on and off
        self.visibility_state()
        if self.logos == True:
            for lg in range(10):
                try:
                    element = self.driver.find_element(By.XPATH,'//*[@id="areas"]/div[{}]'.format(str(lg)))
                    self.driver.execute_script("arguments[0].style.display = 'none';",element)
                except:
                    pass
            self.logos = False
        else:
            for lg in range(10):
                try:
                    element = self.driver.find_element(By.XPATH,'//*[@id="areas"]/div[{}]'.format(str(lg)))
                    self.driver.execute_script("arguments[0].style.display = 'block';",element)
                except:
                    pass
            self.logos = True
        time.sleep(1)
        return
            
    def onkeypress(self, event):
        if event.name == '1':
            self.getcurcolorhotkey(1)
        elif event.name == '2':
            self.getcurcolorhotkey(2)
        elif event.name == '3':
            self.getcurcolorhotkey(3)
        elif event.name == '4':
            self.getcurcolorhotkey(4)
        elif event.name == '5':
            self.getcurcolorhotkey(5)
        elif event.name == '6':
            self.getcurcolorhotkey(6)
        elif event.name == '7':
            self.getcurcolorhotkey(7)
        elif event.name == '8':
            self.getcurcolorhotkey(8)
        elif event.name == '9':
            self.getcurcolorhotkey(9)
        else:
            pass
        return
    
#start an instance of SusBot
SusBot = Sus_Bot(crewmate.username,crewmate.password)
#end of the line partner
