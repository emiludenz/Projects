class Cipher(object):
    def __init__(self, map1, map2):
        self.map1 = dict()
        self.map2 = dict()
        for c1,c2 in zip(map1,map2):
           self.map1.update({c1:c2})
           self.map2.update({c2:c1})
    def encode(self, s):
        ret = ""
        for c in s:
            if c in self.map1.keys(): 
                ret += self.map1[c]
            else:
                ret += c       
        return ret
    
    def decode(self, s):
        ret = ""
        for c in s:
            if c in self.map2.keys(): 
                ret += self.map2[c]
            else:
                ret += c       
        return ret

def assertEquals(var1, var2):
    if var1 == var2:
        return True
    else:
        return False

map1 = "abcdefghijklmnopqrstuvwxyz";
map2 = "etaoinshrdlucmfwypvbgkjqxz";

cipher = Cipher(map1, map2)
print(assertEquals(cipher.encode("abc"), "eta"))
print(assertEquals(cipher.encode("xyz"), "qxz"))
print(assertEquals(cipher.decode("eirfg"), "aeiou"))
print(assertEquals(cipher.decode("erlang"), "aikcfu"))

map2 = 'tfozcivbsjhengarudlkpwqxmy';
cipher = Cipher(map1, map2);
print(assertEquals(cipher.encode('abc'), 'tfo'))
print(assertEquals(cipher.decode('tfo'), 'abc'))
print(assertEquals(cipher.decode('kjpphi'), 'tjuukf'))
print(assertEquals(cipher.encode('ajqqtb'), 'tjuukf'))