__author__ = 'siddiqui'

import os
import sys
from os.path import basename


replace = [".avi","1.4","5.1","-","DVDRip","BRRip","XviD","1CDRip","aXXo","[","]","(",")","{","}","{{","}}"
    "x264","x265","720p","StyLishSaLH (StyLish Release)","DvDScr","MP3","HDRip","WebRip",
    "ETRG","YIFY","StyLishSaLH","StyLish Release","TrippleAudio","EngHindiIndonesian",
    "385MB","CooL GuY","a2zRG","x264","Hindi","AAC","PSK","CyBorG","AC3","MP3"," R6","HDRip","H264","ESub","AQOS",
    "ALLiANCE","UNRATED","ExtraTorrentRG","BrRip","mkv","mpg","DiAMOND","UsaBitcom","AMIABLE",
    "BRRIP","XVID","AbSurdiTy","DVDRiP","TASTE","BluRay","HR","COCAIN","_",".","BestDivX","MAXSPEED",
    "Eng","500MB","FXG","Ac3","Feel","Subs","S4A","BDRip","FTW","Xvid","Noir","1337x","ReVoTT",
    "GlowGaze","mp4","Unrated","hdrip","ARCHiViST","TheWretched","www","torrentfive","com",
    "1080p","1080","SecretMyth","Kingdom","Release","RISES","DvDrip","ViP3R","RISES","BiDA","READNFO",
    "HELLRAZ0R","tots","BeStDivX","UsaBit","FASM","NeroZ","576p","LiMiTED","Series","ExtraTorrent","DVDRIP","~",
    "BRRiP","699MB","700MB","greenbud","B89","480p","AMX","007","DVDrip","h264","phrax","ENG","TODE","LiNE",
    "XVid","sC0rp","PTpower","OSCARS","DXVA","MXMG","3LT0N","TiTAN","4PlayHD","HQ","HDRiP","MoH","MP4","BadMeetsEvil",
    "XViD","3Li","PTpOWeR","3D","HSBS","CC","RiPS","WEBRip","R5","PSiG","'GokU61","GB","GokU61","NL","EE","Rel","NL",
    "PSEUDO","DVD","Rip","NeRoZ","EXTENDED","DVDScr","xvid","WarrLord","SCREAM","MERRY","XMAS","iMB","7o9",
    "Exclusive","171","DiDee","v2","WEB","DL"

    ]

def rena (nameoffile) :

    for value in replace:
            nameoffile = nameoffile.replace(value," ")

    for y in range(1900,2015):
            if str(y) in nameoffile:
                nameoffile = nameoffile.replace(str(y)," ")

    return nameoffile



temp = os.walk(sys.argv[1], topdown=False)


for root, dirs, files in temp:
    for i in files:
        folder = os.path.join(root)
        file = os.path.join(root,i)
        fileName, fileExtension = os.path.splitext(file)
        name = basename(os.path.join(root,i))
        newname = rena (name)
        newname = newname + fileExtension
        os.rename(file, os.path.join(root) + "\\" + newname)
    for i in dirs:
        dir = os.path.join(root,i)
        name = basename(os.path.join(root,i))
        newname = rena (name)
        os.rename(dir, os.path.join(root) + "\\" + newname)

#TODO truncate white space
#TODO add more rippers
print "Renaming Complete"
raw_input()
