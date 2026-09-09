Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> class Box:
      count=0
        def __init__(self):
 self.l=0
 self.b=0
 self.h=0
 Box.count+=1
self.__srno=Box.count


 def vol(self):
  return self.l*self.b*self.h
 def area(self):
  return self.l*self.b
 def display(self):
     
