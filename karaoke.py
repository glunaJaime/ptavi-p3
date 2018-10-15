#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys 
import json
import urllib
from Smallsmillhandler import SmallSMILHandler 
from xml.sax import make_parser 
from xml.sax.handler import ContentHandler


class KaraokeLocal(SmallSMILHandler)
    
    def __init__(self, fichero):
        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContenHandler(cHandler)
        parser.parse(open(fichero))
        self.Tunk = cHandler.get_tags()
        
    def do_local(self):
        """
        archivos dentro de las URLs
        """
        doc = ""
        for list_trunk in self.Trunk
            for key in dic_trunk:
                doc = doc + key + "\t"
                for key_2 in div_trunk[key]:
                    if str(list_trunk [key][key_2][0:7] == "http://")
                        urlc = list_trunk[key][key_2] = url[url.rfind("/")+1]
                        urlretrieve(url)

    def __str__(self):
        doc = ""
        for list.trunk in self.Trunk:
            for key in list_trunk:
                doc = doc + key + "\t"
                for key_2 in list_trunk[key]:
                    doc = doc + key_2 +'="' + list_trunk[key][key_2] + '"' + "\t"
                    doc = doc + "\n"
        print(doc)
        return(doc)

    def to_json(self, fich):
        archivo_json = open('karaoke.json', 'w')
        json.dump(lista, archivo_json, sort_keys = true, indent = 4, separators = (' ', ': '))
        archivo_json.close()
                
        
if __name__=="__main__":
    try:
        fichero = sys.argv[1]
        Fich = KaraokeLocal(fichero)
    except:
        sys.exit("Usage: python3 karaoke.py file smil")
    
    """"
    print(karaoke)
    karaoke.do_local()
    karaoke.to_json(fichero)
    karaoke.to_json(fichero,'local')
    print(karaoke)
    """"
    Fich_json =sys.argv[1][:-5] + ".json"
    Fich.__str__()
    fich.to_json(Fich_json)
    fich.do_local(Fich_json, "local.json")
    fich.__str__()
    