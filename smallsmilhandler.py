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
        self.atr{}
        
    def startElement(self, name, attrs):
    """
    Metodo para abrir etiqueta 
    """
    
    if name == 'self.list':
        #Asi cogemos todos losatributos de mi diccionario y no tengo que hacer varios if
        for name in self.etiquetas: #iteramos por el diccionario 
                self.atr = attrs.get('valor', "")
    self.nueva_list(name, self.atributo)
    
    def get_tags(self):
        return self.etiquetas
    
    def nueva_lista(self, nombre, atributos):
        etiqueta = []
        self.etiqueta = self.endetiqueta(name)
            self.etiqueta = self.ednetiqueta(atributo)
            
    if __name__ == "__main__":
        
        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open('karaoke.smil'))