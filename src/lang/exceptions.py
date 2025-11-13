'''
Created on Aug 9, 2015

@author: karurosu
'''

class LangParseException(Exception):
    def __init__(self, error):
        self.msg = error
    
    def __str__(self):
        return "There was a problem parsing the language definition:"+self.msg