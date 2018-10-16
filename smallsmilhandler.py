#!/usr/bin/python3
# -*- coding: utf-8 -*-


from xml.sax import make_parser 
from xml.sax.handler import ContentHandler 


class SmallSmilHandler(ContentHandler):

    def __init__(self):
        
        """
        Inicializamos las variables
        """
    
        self.lista = []
        self.dic = {'root-layout':['widht', 'height', 'background-color'],
                        'region':['id', 'top','bottom', 'left', 'right'],
                        'img':['src', 'begin', 'dur'],
                        'textstream':['src', 'region']}
        
        
    def startElement(self, name, atrib):
        """
        Metodo para abrir etiqueta 
        """
    
        if name in self.dic:
            #Asi cogemos todos losatributos de mi diccionario y no tengo que hacer varios if
            for atributo in self.dic[name]:
                self.atrib = {}
                self.atrib[atributo] = atrib.get(atributo, "")
                self.lista.append(self.atrib)
            
    
    def get_tags(self):
        return self.lista
    
            
if __name__ == "__main__":
        
    CHandler = SmallSmilHandler()
    parser = make_parser()
    parser.setContentHandler(CHandler)
    parser.parse(open('karaoke.smil'))
    print(CHandler.get_tags())