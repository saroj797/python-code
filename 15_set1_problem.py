# what are the lengtg of the these set

s = set()

s.add(20)
s.add(20.0)  # output is two, kyoki python me 20==20.4 hota isme matter nahi karta hai ki data type kya hai
s.add('20')

print(len(s))

#what is the type of s 

s = {} # this is not  a  set 
print(type(s))