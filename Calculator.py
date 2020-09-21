import tkinter as tk

win = tk.Tk()
win.geometry('400x580')
win.title('Calculator by Cavad')
win.resizable('False', 'False')






class Process():
    def __init__(self):
        self.protext = ''
        self.expressions = '-+/x'
        
    def _show(self):
        labtext['text'] = self.protext
        
    def _add(self, value):
        if len(self.protext) < 22:
            self.protext += value
            self._show()
        else:
            pass
        
    def _arithmetic(self, expression):
        if self.protext:
            if self.protext[-1].isdigit():
                self._add(expression)
            else:
                self.protext[:-1] + expression
                self._show()
        else:
            self.protext = 'Invalid!'
            self._show()
            self.protext = ''
        
    def mce(self):
        self.protext = self.protext.rstrip('1234567890')
        self._show()
        
    def mc(self):
        self.protext = ''
        self._show()
    
    def mbackspace(self):
        self.protext = self.protext[:-1]
        self._show()
        
    
        
            
    def mn0(self):
    	if self.protext and self.protext[-1].isdigit():
    		self._add('0')

    mn1 = lambda self: self._add('1')
    mn2 = lambda self: self._add('2')
    mn3 = lambda self: self._add('3')
    mn4 = lambda self: self._add('4')
    mn5 = lambda self: self._add('5')
    mn6 = lambda self: self._add('6')
    mn7 = lambda self: self._add('7')
    mn8 = lambda self: self._add('8')
    mn9 = lambda self: self._add('9')
    
    
    mdivi = lambda self: self._arithmetic('/')
    mmult = lambda self: self._arithmetic('x')
    mquitout = lambda self: self._arithmetic('-')
    madd = lambda self: self._arithmetic('+')
    
    
    def mpoint(self):
        if (not self.protext) or (self.protext[-1] in self.expressions ):
            self._add('0.')
        elif self.protext.endswith('.'):
            pass
        else:
            self._add('.')
            
    
    def mposneg(self):
        
        listed = list(reversed(self.protext))
        
        
        if not listed:
            listed = ['-']
            
        elif not set(listed) & set(self.expressions):
            listed.append('-')
        elif listed[-1] == '-' and not set(listed[:-1]) & set(self.expressions):
            del listed[-1]
        
        else:
            for i in range(len(listed)):
                if listed[i] in self.expressions and not listed[i+1].isspace():
                    listed[i] = listed[i] + ' -'
                    break
                
                elif listed[i] == '-' and listed[i+1].isspace():
                    del listed[i+1], listed[i]
                    break
        
        self.protext = ''.join(listed[::-1])
        self._show()
        
        
    
    
    
    def mequal(self):
        self.protext = self.protext.rstrip(self.expressions).replace('x', '*')
        result = eval(self.protext)
        self.protext = str(round(result, 7))

        self._show()
        
        
        
            
            
        


ps = Process()


labtext = tk.Label(text = '', fg = 'black', bg = 'white',
                 anchor = 'e', justify = 'right',
                 font = ('Open Sans', 25, 'bold'))


labtext.pack()
labtext.place(relx = 0, rely = 0.005, relwidth = 1, relheight = 0.95/6)

ce = tk.Button(text = 'CE', bg = 'aquamarine2' , font = ('Open Sans', 15, 'bold'), command = ps.mce)
ce.pack()
ce.place(relx = 0, rely = 1/6, relwidth = 1/4, relheight = 1/6)

c = tk.Button(text = 'C', bg = 'aquamarine2' , font = ('Open Sans', 15, 'bold'), command = ps.mc)
c.pack()
c.place(relx = 1/4, rely = 1/6, relwidth = 1/4, relheight = 1/6)

backspace = tk.Button(text = '<', bg = 'aquamarine2' , font = ('Open Sans', 25, 'bold'), command = ps.mbackspace)
backspace.pack()
backspace.place(relx = 2/4, rely = 1/6, relwidth = 1/4, relheight = 1/6)

divi = tk.Button(text = '/', bg = 'aquamarine2' , font = ('Open Sans', 20, 'bold'), command = ps.mdivi)
divi.pack()
divi.place(relx = 3/4, rely = 1/6, relwidth = 1/4, relheight = 1/6)





n7 = tk.Button(text = '7', bg = 'azure2' , font = ('Open Sans', 15, 'bold'), command = ps.mn7)
n7.pack()
n7.place(relx = 0, rely = 2/6, relwidth = 1/4, relheight = 1/6)

n8 = tk.Button(text = '8', bg = 'azure2' , font = ('Open Sans', 15, 'bold'), command = ps.mn8)
n8.pack()
n8.place(relx = 1/4, rely = 2/6, relwidth = 1/4, relheight = 1/6)

n9 = tk.Button(text = '9', bg = 'azure2' , font = ('Open Sans', 15, 'bold'), command = ps.mn9)
n9.pack()
n9.place(relx = 2/4, rely = 2/6, relwidth = 1/4, relheight = 1/6)

mult = tk.Button(text = 'x', bg = 'aquamarine2' , font = ('Open Sans', 20, 'bold'), command = ps.mmult)
mult.pack()
mult.place(relx = 3/4, rely = 2/6, relwidth = 1/4, relheight = 1/6)





n4 = tk.Button(text = '4', bg = 'azure2' , font = ('Open Sans', 15, 'bold'), command = ps.mn4)
n4.pack()
n4.place(relx = 0, rely = 3/6, relwidth = 1/4, relheight = 1/6)

n5 = tk.Button(text = '5', bg = 'azure2' , font = ('Open Sans', 15, 'bold'), command = ps.mn5)
n5.pack()
n5.place(relx = 1/4, rely = 3/6, relwidth = 1/4, relheight = 1/6)

n6 = tk.Button(text = '6', bg = 'azure2' , font = ('Open Sans', 15, 'bold'), command = ps.mn6)
n6.pack()
n6.place(relx = 2/4, rely = 3/6, relwidth = 1/4, relheight = 1/6)

quitout = tk.Button(text = '-', bg = 'aquamarine2' , font = ('Open Sans', 20, 'bold'), command = ps.mquitout)
quitout.pack()
quitout.place(relx = 3/4, rely = 3/6, relwidth = 1/4, relheight = 1/6)






n1 = tk.Button(text = '1', bg = 'azure2' , font = ('Open Sans', 15, 'bold'), command = ps.mn1)
n1.pack()
n1.place(relx = 0, rely = 4/6, relwidth = 1/4, relheight = 1/6)

n2 = tk.Button(text = '2', bg = 'azure2' , font = ('Open Sans', 15, 'bold'), command = ps.mn2)
n2.pack()
n2.place(relx = 1/4, rely = 4/6, relwidth = 1/4, relheight = 1/6)

n3 = tk.Button(text = '3', bg = 'azure2' , font = ('Open Sans', 15, 'bold'), command = ps.mn3)
n3.pack()
n3.place(relx = 2/4, rely = 4/6, relwidth = 1/4, relheight = 1/6)

add = tk.Button(text = '+', bg = 'aquamarine2' , font = ('Open Sans', 20, 'bold'), command = ps.madd)
add.pack()
add.place(relx = 3/4, rely = 4/6, relwidth = 1/4, relheight = 1/6)





posneg = tk.Button(text = '+/_', bg = 'aquamarine2' , font = ('Open Sans', 15, 'bold'), command = ps.mposneg)
posneg.pack()
posneg.place(relx = 0, rely = 5/6, relwidth = 1/4, relheight = 1/6)

r0 = tk.Button(text = '0', bg = 'azure2' , font = ('Open Sans', 15, 'bold'), command = ps.mn0)
r0.pack()
r0.place(relx = 1/4, rely = 5/6, relwidth = 1/4, relheight = 1/6)

point = tk.Button(text = '.', bg = 'aquamarine2' , font = ('Open Sans', 15, 'bold'), command = ps.mpoint)
point.pack()
point.place(relx = 2/4, rely = 5/6, relwidth = 1/4, relheight = 1/6)

equal = tk.Button(text = '=', bg = 'aquamarine2' , font = ('Open Sans', 20, 'bold'), command = ps.mequal)
equal.pack()
equal.place(relx = 3/4, rely = 5/6, relwidth = 1/4, relheight = 1/6)






win.mainloop()
































