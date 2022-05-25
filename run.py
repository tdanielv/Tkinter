from tkinter import *
import codecs
import pprint
 
 
class Block:
    def __init__(self, master, func):
        self.arr = []
        # -*- coding: cp1251 -*-
        with codecs.open("D:\Python etc\examples\LA3.txt", 'r', 'utf-8') as r:
            self.stroki = r.readlines()
            for line in self.stroki:
                self.arr.append(line)
        self.finish = []
        self.ent = Entry(master, width=100)
        self.but = Button(master,
                          text='добавляем в список')
        self.but2 = Button(master,
                          text='исключаем из списка')
        self.but3 = Button(master,
                          text='Результат')
        self.lab = Label(master, width=200,
                         bg='white', fg='black', text = 'введи любой запрос')
        self.but['command'] = getattr(self, 'func')
        self.but2['command'] = getattr(self, 'func2')
        self.but3['command'] = getattr(self, 'func3')
        self.but2.pack()
        self.but3.pack()
        self.ent.pack()
        self.but.pack()
        self.lab.pack()
 
    def func(self):
        self.l = []
        a = self.ent.get()
        for i in range(len(self.arr)):
            if a in self.arr[i]:
                self.l.append(self.arr[i])
                self.finish.append(self.arr[i])
        if self.l == []:
            self.lab['text'] = 'нет в наличии или неверно указаны данные'
        else: 
            self.lab['text'] = (self.l)

    def func2(self):
        l = []
        a = self.ent.get()
        for i in self.finish:
            if a not in i:
                l.append(i)
        self.finish = l 
        self.lab['text'] = (self.finish)

    def func3(self):
        self.lab['text'] = self.finish
    def Salon(self):
        self.l = []
        self.n = []
        a = self.ent.get()
        for i in range(len(self.arr)):
            if a in self.arr[i]:
                self.l.append(self.arr[i])
                self.finish.append(self.arr[i])
                self.n.append(i)
        if self.n == []:
            self.lab['text'] = 'нет в наличии или неверно указаны данные'
        else: 
            self.lab['text'] = ('Инвентарные номера:', self.n,'\n', self.l)
    def Year(self):
        self.l = []
        self.n = []
        a = self.ent.get()
        for i in range(len(self.arr)):
            if a in self.arr[i]:
                self.l.append(self.arr[i])
                self.finish.append(self.arr[i])
                self.n.append(i)
                print(self.arr[i].index(a))
        if self.n == []:
            self.lab['text'] = 'нет в наличии или неверно указаны данные'
        else: 
            self.lab['text'] = ('Инвентарные номера:', self.n,'\n', self.l)
    def Km(self):
        s = self.ent.get()
        s = s.split()
        s.reverse()
        self.lab['text'] = ' '.join(s)
    def V(self):
        self.l = []
        self.n = []
        a = self.ent.get()
        for i in range(len(self.arr)):
            if a in self.arr[i]:
                self.l.append(self.arr[i])
                self.finish.append(self.arr[i])
                self.n.append(i)
                print(self.arr[i].index(a))
        if self.n == []:
            self.lab['text'] = 'нет в наличии или неверно указаны данные'
        else: 
            self.lab['text'] = ('Инвентарные номера:', self.n,'\n', self.l)
    def Price(self):
        self.l = []
        self.n = []
        a = self.ent.get()
        for i in range(len(self.arr)):
            if a in self.arr[i]:
                self.l.append(self.arr[i])
                self.finish.append(self.arr[i])
                self.n.append(i)
                print(self.arr[i].index(a))
        if self.n == []:
            self.lab['text'] = 'нет в наличии или неверно указаны данные'
        else: 
            self.lab['text'] = ('Инвентарные номера:', self.n,'\n', self.l)
    def Korob(self):
        self.l = []
        self.n = []
        a = self.ent.get()
        for i in range(len(self.arr)):
            if a in self.arr[i]:
                self.l.append(self.arr[i])
                self.finish.append(self.arr[i])
                self.n.append(i)
                print(self.arr[i].index(a))
        if self.n == []:
            self.lab['text'] = 'нет в наличии или неверно указаны данные'
        else: 
            self.lab['text'] = ('Инвентарные номера:', self.n,'\n', self.l)    
 
 
root = Tk()
root.title('Следуйте пошагово сверху вниз' )
block1 = Block(root, 'Marka')
# block2 = Block(root, 'Salon')
# block3 = Block(root, 'Year')
# block4 = Block(root, 'Km')
# block5 = Block(root, 'V')
# block6 = Block(root, 'Price')
# block7 = Block(root, 'Korob')
 
root.mainloop()
