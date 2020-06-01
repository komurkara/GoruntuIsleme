# -*- coding: utf-8 -*-
"""
Created on Mon May 11 22:29:18 2020

@author: OGK
"""

class Singleton:
   __instance = None
   @staticmethod 
   def getInstance():
      """ Static access method. """
      a = int(input("Birinci Sayı:"))
      b = int(input("İkinci Sayı:"))
      if Singleton.__instance == None:
          
         Singleton()
     
      return  "Toplam:", a+b, "fark: ", a-b, "Carpim: ", a*b, "bolum: ", a/b 
  
    
   def __init__(self):
      """ Virtually private constructor. """
      if Singleton.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         Singleton.__instance = self
  

         
s = Singleton()
print(s)

s1 = Singleton.getInstance()
print(s1)


 