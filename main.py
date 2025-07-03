import os
import time

LETTERS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', ',', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ':', '_', '"', "'", '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
ART = """
·▄▄▄▄  ▄• ▄▌• ▌ ▄ ·.  ▄▄▄·    ▄▄▄▄▄ ▄ .▄▄▄▄ .    ·▄▄▄▄  ▄• ▄▌• ▌ ▄ ·.  ▄▄▄·
██▪ ██ █▪██▌·██ ▐███▪▐█ ▄█    •██  ██▪▐█▀▄.▀·    ██▪ ██ █▪██▌·██ ▐███▪▐█ ▄█
▐█· ▐█▌█▌▐█▌▐█ ▌▐▌▐█· ██▀·     ▐█.▪██▀▐█▐▀▀▪▄    ▐█· ▐█▌█▌▐█▌▐█ ▌▐▌▐█· ██▀·
██. ██ ▐█▄█▌██ ██▌▐█▌▐█▪·•     ▐█▌·██▌▐▀▐█▄▄▌    ██. ██ ▐█▄█▌██ ██▌▐█▌▐█▪·•
▀▀▀▀▀•  ▀▀▀ ▀▀  █▪▀▀▀.▀        ▀▀▀ ▀▀▀ · ▀▀▀     ▀▀▀▀▀•  ▀▀▀ ▀▀  █▪▀▀▀.▀      
                            Made by @iAvra v0.1  
                           Lightweight & Fastest                         
"""


def reset_grabbed():
    with open("grabbed.txt", mode='w+') as g:
        g.flush()

def grab_triggers(lua_file):
    grabbed_triggers = []
    try:
        with open(lua_file, encoding="utf-8") as trigger:
            data = trigger.readlines()
            for line in data:
                if "TriggerServerEvent" in line:
                    line = list(line)
                    for i in line:
                        if line[0] not in LETTERS:
                            line.pop(0)
                    line = "".join(line)
                    line.replace("}", ")").replace("{", ")")
                    grabbed_triggers.append(line)
        grabbed_triggers = set(grabbed_triggers)
        grabbed_triggers = list(grabbed_triggers)
        with open("grabbed.txt", "r", encoding="utf-8") as f:
            txt_data = f.read()
        with open("grabbed.txt", "a", encoding="utf-8") as f:
            if grabbed_triggers != []:
                for i in grabbed_triggers:
                    if i not in txt_data:
                        f.write(f"{i}")
    except:
        pass

                 

def find_and_grab(dirpath, filename):
    for _ in filename:
            if ".lua" in _:
                full_path = f"{dirpath}/{_}"
                grab_triggers(full_path)

print(ART)    
print("[1] Grab Dump Triggers")
print("[2] Exit")
if int(input("Choose an operation: ")) == 1:
    os.system('cls')
    PATH = input("[/] Enter Dump Path: ")
    head_directory_contents = os.listdir(PATH)
    reset_grabbed()       
    for i in range(len(head_directory_contents)):
        directory_file_names = os.listdir(f"{PATH}/{head_directory_contents[i]}")
        full_p = f"{PATH}/{head_directory_contents[i]}"
        for dirpath, dirnames, filenames in os.walk(f"{full_p}"):
            find_and_grab(dirpath,filenames)
            print(f"[+]{PATH}/{head_directory_contents[i]}/{filenames}")
            if dirnames != []:
                for _ in dirnames:
                    new_path = f"{dirpath}/{_}"
                    for p, o, filenames in os.walk(f"{new_path}"):
                        print(f"[+]{new_path}/{filenames}")
                        find_and_grab(new_path,filenames)
                        
    time.sleep(0.15)
    print("[v] Process Done, Grabbed Triggers to: /grabbed.txt")
    
time.sleep(1)
os._exit(1)