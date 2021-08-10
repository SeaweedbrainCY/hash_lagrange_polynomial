"""

Copyright (C) 2021  Nathan Stchepinsky

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""


import numpy as np
import sys
import random
import string
import time as t
from scipy.interpolate import lagrange

class Lagrange:
    def __init__(self, length, show_print = False):
        """
            Init the object

            length = len of the final hash (in char)
        """
        self.length = length
        self.alphabet =  string.ascii_lowercase + "1234567890" 
        self.show_print = show_print

    def encode(self,string): # ASCII
        encoded = [ord(c) for c in string]
        return encoded
    
    def decode(self,tab):
        """
            Decode on our alphabet
        """
        decoded = ""
        len_latin = len(self.alphabet)
        #print(len_latin)
        for e in tab:
            modulo  = int(e)
            #print(modulo%len_latin, end=' ')
            decoded += self.alphabet[modulo%len_latin]
        
        return decoded

    def padding(self, bits):
        """
            Padd the binary with a method inspired by Merkle-Damgard
        """
        init_len = len(bits)
        if init_len < self.length : # We don't pad if we have enough char
            if len(bits) == 0:
                bits.append(2)
            if  len(bits)%(self.length) != 0:
                bits.append(2) 
            while len(bits)%(self.length)-1 != 0 :                
                bits.append(1)
            bits.append(init_len + 256) # That's a char unreachable bc it ascii code it too high
        return bits


    def hash_lagrange(self,encoded_string):
        """
            Generate the hashing polynomial
        """
        poly = np.poly1d(0)
        max_degree = np.poly1d([1] + [0]*(self.length+1)) # X^n pour le modulo
        if encoded_string == "":
            raise TypeError("FATAL ERROR : [hash_lagrange func] The word to interpolate is empty")
        last = np.poly1d(1)
        for i in range(len(encoded_string)):
            last = np.polymul(last, np.poly1d([1,-encoded_string[i]]))
            poly = np.polyadd((encoded_string[i])*last, poly)
            (_,poly) = np.polydiv(poly, max_degree) # on récupère le modulo
            last = np.poly1d(np.mod(last,100008)) # Pour ne pas manipuler de coefficient trop grand. C'est un multiple de 36. 
        return np.array(poly,dtype = int)[1:]# on a un polynôme unitaire de degré self.length, donc self.length + 1 coefficients

    def hash(self,clear):
        """
            Main func, call the different func to build the algo
        """
        if self.show_print :
            print("[*] Encoding ...")
        encoded = self.encode(clear) # Encoding on the latin alphabet
        if self.show_print :
            print("[*] Encoded = ", encoded)
            print("[*] Padding ...")
        padded  = self.padding(encoded) # We pad if we need
        if self.show_print :
            print("[*] Padded = ", padded)
            print("[*] Hashing ...")
        hashed = self.hash_lagrange(padded)
        if self.show_print :
            print("[*] Hashed polynom = ", hashed)
            print("[*] Decoding ...")
        decoded = self.decode(hashed)
        if self.show_print :
            print("[*] Decoded = ", decoded)
        return decoded
        

