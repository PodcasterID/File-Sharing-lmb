import os, fnmatch
import sys, argparse
#from bot import Bot
#from test import result




print(" Telegram Bot Manager")

selected_env = ""


def run():
    num_files = 1
    env_files= []
    env_path = 'config'
    if not os.path.exists(env_path):
        os.makedirs(env_path)


    files = os.listdir(env_path)
    for f in files:
        if fnmatch.fnmatch(f, '*.env'):
            print( str(num_files),str(f))
            num_files=num_files+1
            env_files.append(str(f))
        
    fileselector = input("Pilih file host : ")
    print("File yang anda pilih adalah : " + env_files[int(fileselector)-1])
    selected_env = str(env_path) +"/"+ str(env_files[int(fileselector)-1])
    return selected_env
#if (selected_env == ''):
#    selected_env=run()
selected_env=run()


if __name__ == '__main__':
    selected_env=run()
    #print(selected_env)
    #Bot().run()
    print("RUNNIG")