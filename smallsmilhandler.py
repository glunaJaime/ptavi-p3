#!/usr/bin/python3
# -*- coding: utf-8 -*-


from xml.sax import make_parser 
from xml.sax.handler import ContentHandler 

class SmallSmilHandler(ContentHandler)

    def __init__(self):
    """
    Inicializamos las variables
    """
        self.etiquetas = {}
        self.lista = {'root-layout':['widht', 'height', 'background-                                color'],
                        'region':['id', 'top','bottom', 'left',                 'right'],
                        'img':['src', 'begin', 'dur'],
                        'textstream':['src', 'region']}
        self.atr{}
        
    def startElement(self, name, attrs):
    """
    Metodo para abrir etiqueta 
    """
    
    if name == 'self.lista':
        #Asi cogemos todos losatributos de mi diccionario y no tengo que hacer varios if
        for name in self.etiquetas: #iteramos por el diccionario 
                self.atr = attrs.get('valor', "")
                
    if __name__ == "__main__":
        
        parser = makeparser()
        cHandler = CHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open('karaoke.smil'))