#!/usr/bin/python3
# -*- coding: utf-8 -*-


from xml.sax import make_parser 
from xml.sax.handler import ContentHandler 


class SmallSMILHandler(ContentHandler)

    def __init__(self):
    """
    Inicializamos las variables
    """
        self.etiquetas = []
        self.list = {'root-layout':['widht', 'height', 'background-color'],
                        'region':['id', 'top','bottom', 'left', 'right'],
                        'img':['src', 'begin', 'dur'],
                        'textstream':['src', 'region']}
        
        
    def startElement(self, name, attrs):
    """
    Metodo para abrir etiqueta 
    """
    
    if name in self.list:
        #Asi cogemos todos losatributos de mi diccionario y no tengo que hacer varios if
        print(name)
        for attrs in self.list[name]
            self.attrs = {}
            self.attr[valor] = attrs.get(valor, "")
            self.list.appenjd(self.attrs)
            
    
    def get_tags(self):
        return self.etiquetas
    
            
    if __name__ == "__main__":
        
        cHandler = SmallSMILHandler()
        parser = make_parser()
        parser.setContentHandler(cHandler)
        parser.parse(open('karaoke.smil'))