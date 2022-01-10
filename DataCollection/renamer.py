import os

for name in os.listdir("H://YouTube Clickbait Classification//DataCollection//isClickbait"):
    os.rename(name, name[:11] + "___" + name[13:])
    #if ";" in name:
        #i = name.find(";")
        #os.rename(name, name[:i] + name[i+1:])
