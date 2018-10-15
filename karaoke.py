#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys 
from Smallsmillhandler import SmallSMILHandler 
from xml.sax import make_parser 
from xml.sax.handler import ContentHandler

def new_list(fichero):
        parser = make_parrser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(fichero)
        list = cHandler.get_tags()
        return list
    
def print_list(list)


def open_fichero():
    try:
        fichero = open(sys.argv[1],'r')
        return fichero
    except IndexError:
        sys.exit("Usage:python3 Karaoke.py file.smil")
        
if __name__ == "__main__":
    
    