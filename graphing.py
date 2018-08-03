# parts of the graphing class by Konstantinos Xynos (drawing methods)

from graphvizlayout import graph
from graphvizlayout import extended_graph
from tkinter import *
from tkinter import ttk
import random

class graphing:

    def initialize_colors(self):
        file = open('/Users/bstoll19/Desktop/t2activity','r')
        counter = 0
        self.lines = file.readlines()
        for x in range(1,len(self.lines)):
            if counter == 1:
                break
            if not 'by' in self.lines[x]:
                counter += 1
            if counter == 1:
                self.index=x+1
            info = self.lines[x].replace('\t','').replace('\n','').split(':')
            if info[1][1] == '0':
                try:
                    if self.graph == self.current_graph:
                        r = lambda: random.randint(0,255)
                        l = self.wc.create_line(15,85,20,85, fill = '#%02X%02X%02X' % (r(),r(),r()), state = 'hidden')
                        self.wc.tag_bind(l,'<Button-1>',self.click)
                        self.wc.tag_bind(l,'<Enter>',self.wc_hover)
                        self.wc.tag_bind(l,'<Leave>',self.wc_hover_leave)
                        self.wc_items.append(self.graph.u.find_object(info[0].split()[1]))
                        self.wc_coords.append([15,85,20,85])
                    if self.c.itemcget(self.items.index('node '+self.graph.u.find_object(info[0].split()[1]))+1, 'fill') != 'purple':
                        self.c.itemconfig(self.items.index('node '+self.graph.u.find_object(info[0].split()[1]))+1, fill = "red")
                except:
                    pass
            else:
                try:
                    if self.graph == self.current_graph:
                        r = lambda: random.randint(0,255)
                        l = self.wc.create_line(15,20,20,20, fill = '#%02X%02X%02X' % (r(),r(),r()), state = 'hidden')
                        self.wc.tag_bind(l,'<Button-1>',self.click)
                        self.wc.tag_bind(l,'<Enter>',self.wc_hover)
                        self.wc.tag_bind(l,'<Leave>',self.wc_hover_leave)
                        self.wc_items.append(self.graph.u.find_object(info[0].split('0')[1].replace(' ','')))
                        self.wc_coords.append([15,20,20,20])
                    if self.c.itemcget(self.items.index('node '+self.graph.u.find_object(info[0].split()[1]))+1, 'fill') != 'purple':
                        self.c.itemconfig(self.items.index('node '+self.graph.u.find_object(info[0].split()[1]))+1, fill = "green")
                except:
                    pass
        self.c.update_idletasks()

    def read_data(self):
        self.initialize_colors()
        data = [[]for i in range(1000)]
        diff = int(self.lines[self.index].split()[0])/10
        for y in range(self.index,len(self.lines)):
            try:
                data[int(int(self.lines[y].replace('\t','').replace('\n','').split(':')[0].split(' ')[-3])/10-diff)].append([self.lines[y].replace('\t','').replace('\n','').split(':')[0].split(' ')[-2],self.lines[y].replace('\t','').replace('\n','').split(':')[1].split('by')[-1].replace(' ',''),self.lines[y].split(':')[1].replace(' ','').split('[')[0]])
            except:
                pass
        self.change_colors(data)

    def change_colors(self,data):
        for index in range(0,len(data)):
            if index>self.time:
                self.root.update()
            r = self
            while True:
                for y in range(0,len(r.items)):
                    if r.items[y][0] == 'e':
                        r.c.itemconfig(y+1, fill = 'black', width = 1)
                        r.time = self.time
                try:
                    r = r.graphing
                except:
                    break
            if index>self.time:
                self.root.after(2000, self.change(data[index], index))
                self.time += 1
            else:
                self.change(data[index], index)

    def change(self,info,index):
        if self.graph == self.current_graph:
            self.wc_bool = [False]*len(self.wc_coords)
        else:
            self.graphing.change(info, index)
        for x in info:
            self.c.itemconfig(str(len(self.items)+1), text = 't = '+str(index*10))
            if x[2].replace('\t','') == '0':
                try:
                    if self.c.itemcget(self.items.index('node '+self.graph.u.find_object(x[0]))+1,'fill') != 'purple':
                        self.c.itemconfig(self.items.index('node '+self.graph.u.find_object(x[0]))+1,fill = "red")
                except:
                    try:
                        if self.c.itemcget(self.items.index('node '+self.current_graph.compressionu.find_object(self.graph.u.find_object(x[0])))+1,'fill') != 'purple':
                            self.c.itemconfig(self.items.index('node '+self.current_graph.compressionu.find_object(self.graph.u.find_object(x[0])))+1,fill = "red")
                    except:
                        pass
            else:
                try:
                    if self.c.itemcget(self.items.index('node '+self.graph.u.find_object(x[0]))+1,'fill') != 'purple':
                        self.c.itemconfig(self.items.index('node '+self.graph.u.find_object(x[0]))+1,fill = "green")
                except:
                    try:
                        if self.c.itemcget(self.items.index('node '+self.current_graph.compressionu.find_object(self.graph.u.find_object(x[0])))+1,'fill') != 'purple':
                            self.c.itemconfig(self.items.index('node '+self.current_graph.compressionu.find_object(self.graph.u.find_object(x[0])))+1,fill = "green")
                    except:
                        pass
            try:
                self.c.itemconfig(self.items.index('edge '+self.current_graph.compressionu.find_object(self.graph.u.find_object(x[1]))+' '+self.current_graph.compressionu.find_object(self.graph.u.find_object(x[0])))+1,fill = 'blue',width = 3)
            except:
                try:
                    self.c.itemconfig(self.items.index('edge '+self.graph.u.find_object(x[1])+' '+self.graph.u.find_object(x[0]))+1,fill = 'blue',width = 3)
                except:
                    pass
            if self.graph == self.current_graph:
                if len(self.dc.find_overlapping(index*10+21,self.graph.all_nodes.index(self.graph.u.find_object(x[0]))*7+15,index*10+25,self.graph.all_nodes.index(self.graph.u.find_object(x[0]))*7+20)) == 0:
                    if x[2][0] == '0':
                        o = self.dc.create_oval(index*10+20,self.graph.all_nodes.index(self.graph.u.find_object(x[0]))*7+15,index*10+25,self.graph.all_nodes.index(self.graph.u.find_object(x[0]))*7+20, fill = 'red', outline = 'red')
                        self.dc_items.append(self.graph.u.find_object(x[0])+' at t = '+str(index*10))
                        self.dc.tag_bind(o,'<Enter>',self.hover)
                        self.dc.tag_bind(o,'<Leave>', self.hover_leave)
                        try:
                            self.wc_coords[self.wc_items.index(self.graph.u.find_object(x[0]))-6].extend([index*10+20,20,index*10+20,85])
                            self.wc.coords(self.wc_items.index(self.graph.u.find_object(x[0]))+1,self.wc_coords[self.wc_items.index(self.graph.u.find_object(x[0]))-6])
                            self.wc_bool[self.wc_items.index(self.graph.u.find_object(x[0]))-6] = True
                        except:
                            pass
                    else:
                        o = self.dc.create_oval(index*10+20,self.graph.all_nodes.index(self.graph.u.find_object(x[0]))*7+15,index*10+25,self.graph.all_nodes.index(self.graph.u.find_object(x[0]))*7+20, fill = 'green', outline = 'green')
                        self.dc_items.append(self.graph.u.find_object(x[0])+' at t = '+str(index*10))
                        self.dc.tag_bind(o,'<Enter>',self.hover)
                        self.dc.tag_bind(o,'<Leave>',self.hover_leave)
                        try:
                            self.wc_coords[self.wc_items.index(self.graph.u.find_object(x[0]))-6].extend([index*10+20,85,index*10+20,20])
                            self.wc.coords(self.wc_items.index(self.graph.u.find_object(x[0]))+1,self.wc_coords[self.wc_items.index(self.graph.u.find_object(x[0]))-6])
                            self.wc_bool[self.wc_items.index(self.graph.u.find_object(x[0]))-6] = True
                        except:
                            pass
                    o = self.dc.create_line(index*10+15,self.graph.all_nodes.index(self.graph.u.find_object(x[1]))*7+17,index*10+20,self.graph.all_nodes.index(self.graph.u.find_object(x[0]))*7+17, fill = 'black')
                    self.dc.tag_bind(o,'<Enter>',self.hover)
                    self.dc.tag_bind(o,'<Leave>',self.hover_leave)
                    self.dc_items.append(self.graph.u.find_object(x[1])+' at t = '+str((index-1)*10)+' to '+self.graph.u.find_object(x[0])+' at t = '+str(index*10))
                    for r in range(0,len(self.wc_bool)):
                        if self.wc_bool[r] == False and self.wc_coords[r][-2] != index*10+20:
                            self.wc_coords[r].extend([index*10+20,self.wc_coords[r][-1]])
                            self.wc.coords(r+7,self.wc_coords[r])
                self.wc.xview_moveto((index*10+20-self.wc_root.winfo_screenwidth())/100500)
                self.dc.xview_moveto((index*10+20-self.dc_root.winfo_screenwidth())/100500)
                if index*10+20 > self.wc_root.winfo_screenwidth():
                    self.wc.coords(self.wc_label, index*10+20-self.wc_root.winfo_screenwidth()/2, 106)
                    self.dc.coords(self.dc_label, index*10+20-self.dc_root.winfo_screenwidth()/2, len(self.graph.all_nodes)*7+22)

    def inch2px(self,inch):
        return int(float(inch) * self.PIXELS_PER_INCH)

    def get_eg_parameters(self,root,graph,time,p,graphing):
        self.root = root
        self.graph = graph
        self.time = time
        self.q = p
        self.graphing = graphing

    def hover(self,event):
        self.dc.itemconfig(self.dc_label, text = 'Current Position: '+self.dc_items[self.dc.find_withtag(CURRENT)[0]-1])
        self.dc_root.update()

    def wc_hover(self,event):
        self.wc.itemconfig(self.wc_label, text = 'Current Position: '+self.wc_items[self.wc.find_withtag(CURRENT)[0]-1]+' at t = '+str(int((self.wc_root.winfo_pointerx()-20)/10)*10))
        self.wc_root.update()

    def wc_hover_leave(self,event):
        self.wc.itemconfig(self.wc_label, text = 'Current Position: ')
        self.wc_root.update()

    def hover_leave(self,event):
        self.dc.itemconfig(self.dc_label, text = 'Current Position: ')
        self.dc_root.update()

    def click(self,event):
        if self.wc.itemcget(CURRENT, 'width') == '1.0':
            self.wc.itemconfig(CURRENT, width = 3)
        else:
            self.wc.itemconfig(CURRENT, width = 1)
        self.wc_root.update()

    def main(self,filename):
        if filename == 'chipgraph':
            file = open('/Users/bstoll19/Desktop/t2.prs','r')
            self.time = 0
            g = graph(file)
            g.main()
            g.c.render()
            self.graph = g
            self.current_graph = g
        else:
            e = extended_graph(self.root,self.graph,self.q)
            e.main()
            e.c.render()
            self.current_graph = e
        self.items = []
        self.root = Tk()
        if filename == 'chipgraph':
            self.root.title('Chip Graph')
            self.dc_items = []
            self.dc_root = Tk()
            self.dc_root.title('Dot Graph')
            self.dc_root.rowconfigure(0, weight = 1)
            self.dc_root.columnconfigure(0, weight = 1)
            dcFrame = Frame(self.dc_root, width = self.dc_root.winfo_screenwidth(), height = len(self.graph.all_nodes)*7+30)
            dcFrame.grid(sticky = N+E+S+W)
            dcFrame.rowconfigure(0, weight = 1)
            dcFrame.columnconfigure(0, weight = 1)
            dcFrame.focus_set()
            self.dc = Canvas(dcFrame, width = self.dc_root.winfo_screenwidth(), height = len(self.graph.all_nodes)*7+30, bg = 'white', scrollregion = (0,0,100500, len(self.graph.all_nodes)*7+30))
            self.dc.grid(column = 0, row = 0, sticky = N+W+E+S)
            scroll_x = Scrollbar(dcFrame, orient = HORIZONTAL, command = self.dc.xview)
            scroll_y = Scrollbar(dcFrame, orient = VERTICAL, command = self.dc.yview)
            scroll_x.grid(row = 1, column = 0, sticky = E+W)
            scroll_y.grid(row = 0, column = 1, sticky = N+S)
            self.dc.configure(xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)
            self.dc.create_line(0,len(self.graph.all_nodes)*7+12,100500,len(self.graph.all_nodes)*7+12, fill = 'black')
            self.dc_items.append('x-axis')
            self.dc.create_text(50,len(self.graph.all_nodes)*7+22, text = 'time', fill = 'black')
            self.dc_items.append('x-axis label')
            self.dc.create_line(15,0,15,len(self.graph.all_nodes)*7+30, fill = 'black')
            self.dc_items.append('y-axis')
            self.dc.create_text(7,50,text = '\n'.join('nodes'), fill = 'black')
            self.dc_items.append('y-axis label')
            self.dc_label = self.dc.create_text(self.dc_root.winfo_screenwidth()/2,len(self.graph.all_nodes)*7+22, text = 'Current Position: ', fill = 'black')
            self.dc_items.append('tracker')

            self.wc_items = []
            self.wc_coords = []
            self.wc_root = Tk()
            self.wc_root.title('Wave Graph')
            self.wc_root.rowconfigure(0, weight = 1)
            self.wc_root.columnconfigure(0, weight = 1)
            wcFrame = Frame(self.wc_root, width = self.wc_root.winfo_screenwidth(), height = 115)
            wcFrame.grid(sticky = N+E+S+W)
            wcFrame.rowconfigure(0, weight = 1)
            wcFrame.columnconfigure(0, weight = 1)
            wcFrame.focus_set()
            self.wc = Canvas(wcFrame, width = self.wc_root.winfo_screenwidth(), height = 115, bg = 'white', scrollregion = (0,0,100500, 115))
            self.wc.grid(column = 0, row = 0, sticky = N+W+E+S)
            scroll_x = Scrollbar(wcFrame, orient = HORIZONTAL, command = self.wc.xview)
            scroll_y = Scrollbar(wcFrame, orient = VERTICAL, command = self.wc.yview)
            scroll_x.grid(row = 1, column = 0, sticky = E+W)
            scroll_y.grid(row = 0, column = 1, sticky = N+S)
            self.wc.configure(xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)
            self.wc.create_line(0,98,100500,98, fill = 'black')
            self.wc_items.append('x-axis')
            self.wc.create_text(50,106, text = 'time', fill = 'black')
            self.wc_items.append('x-axis label')
            self.wc.create_line(15,0,15,115, fill = 'black')
            self.wc_items.append('y-axis')
            self.wc.create_text(7,20,text = '1')
            self.wc_items.append('y-axis label 1')
            self.wc.create_text(7,85,text = '0')
            self.wc_items.append('y-axis label 0')
            self.wc_label = self.wc.create_text(self.wc_root.winfo_screenwidth()/2,106, text = 'Current Position: ', fill = 'black')
            self.wc_items.append('tracker')

        else:
            if int(self.current_graph.size) > 1:
                self.root.title('CLUSTER '+filename)
            else:
                self.root.title(filename)
        self.root.maxsize(self.root.winfo_screenwidth(),self.root.winfo_screenheight())
        self.root.rowconfigure(0, weight = 1)
        self.root.columnconfigure(0, weight = 1)

        self.PIXELS_PER_INCH  = self.root.winfo_fpixels('1i')
        self.DOT_FILE = '/Users/bstoll19/'+str(filename)+'.dot'
        self.X_OFFSET = 25
        self.SHOW_EDGE_LBL = False

        dot_file = open(self.DOT_FILE,'r',encoding = 'latin1')
        lines = dot_file.readlines()
        grph_lst = lines[1].replace('"',',').split(',')

        self.width_dot = int(float(grph_lst[3]))/2
        self.height_dot = int(float(grph_lst[4]))/2
        rootFrame = Frame(self.root,width = self.width_dot, height = self.height_dot)
        rootFrame.grid(sticky = N+E+S+W)
        rootFrame.rowconfigure(0, weight = 1)
        rootFrame.columnconfigure(0, weight = 1)
        rootFrame.focus_set()

        scrollbrY = Scrollbar(rootFrame, orient = VERTICAL)
        scrollbrX = Scrollbar(rootFrame, orient = HORIZONTAL)
        scrollbrY.grid(row = 0, column = 1, sticky = N+S)
        scrollbrX.grid(row = 1, column = 0, sticky = E+W)

        self.c = Canvas(rootFrame, width = self.width_dot+50, height = self.height_dot+50, bg = 'white', xscrollcommand = scrollbrX.set, yscrollcommand = scrollbrY.set, scrollregion = (0,0,self.width_dot+20,self.height_dot +20))
        self.c.grid(column = 0,row = 0,sticky = N+W+E+S)

        def click(event):
            node = ''
            if self.items[self.c.find_withtag(CURRENT)[0]-1][0] == 'n':
                node = self.items[self.c.find_withtag(CURRENT)[0]-1].split(' ')[1]
            elif self.items[self.c.find_withtag(CURRENT)[0]-2][0] == 'n':
                node = self.items[self.c.find_withtag(CURRENT)[0]-2].split(' ')[1]
            x = graphing()
            x.get_eg_parameters(node,self.graph,self.time,self.current_graph,self)
            x.main(node)

        def left_click(event):
            r = self
            while True:
                try:
                    r = r.graphing
                except:
                    break
            node = ''
            if self.items[self.c.find_withtag(CURRENT)[0]-1][0] == 'n':
                node = self.items[self.c.find_withtag(CURRENT)[0]-1].split(' ')[1]
            elif self.items[self.c.find_withtag(CURRENT)[0]-2][0] == 'n':
                node = self.items[self.c.find_withtag(CURRENT)[0]-2].split(' ')[1]
            if r.wc.itemcget(r.wc_items.index(node)+1, 'state') == 'hidden':
                r.wc.itemconfig(r.wc_items.index(node)+1, state = 'normal')
            else:
                r.wc.itemconfig(r.wc_items.index(node)+1, state = 'hidden')
            r.wc_root.update()

        self.c.bind('<Button-1>',click)
        self.c.bind('<Button-2>',left_click)
        scrollbrY.config(command = self.c.yview)
        scrollbrX.config(command = self.c.xview)
        for x in range(1,len(lines)):
            if 1<len(lines[x].split()) and lines[x].split()[1] == '->':
                self.drw_edge(lines,x)
            elif '[color' in lines[x].replace(' ','=').split('='):
                self.drw_node(lines,x)
        self.c.create_text(25,10,text = 't = 0',fill = 'black',font = ("Times", 10))
        self.read_data()
        dot_file.close()
        self.root.mainloop()

    def drw_node(self,lines,x):
        color = lines[x].replace(',','=').split('=')[1]
        X = int(((float(lines[x+4].replace(',','"').split('"')[1]))-(self.inch2px(lines[x+6].replace(']','=').split('=')[1]))/2)/2+self.X_OFFSET)
        Y = int(self.height_dot-((int(lines[x+4].replace(',','"').split('"')[2])-(self.inch2px(lines[x+1].replace(',','=').split('=')[1]))/2))/2)
        X2 = int((self.inch2px(lines[x+6].replace(']','=').split('=')[1]))/2+X)
        self.node_height=(self.inch2px(lines[x+1].replace(',','=').split('=')[1]))/2
        self.node_width=(self.inch2px(lines[x+6].replace(']','=').split('=')[1]))/2
        Y2 = self.node_height+Y
        aOval = self.c.create_oval(X,Y,X2,Y2,fill = color)
        self.items.append('node '+lines[x].replace('"','').replace('\t','').split(' ')[0])
        label = lines[x+2].replace('"','').replace(',','=').split('=')[1]
        aLabel = self.c.create_text(X+(float(self.node_width)/2),Y+(float(self.node_height)/2),text = label,fill = 'black',font = ("Times", 8), width = self.node_width)
        self.items.append('label ')

    def drw_edge(self,lines,x):
        points_list = lines[x+3].replace(' ',',').replace('"',',').split(',')[4:-1]
        count = x+3
        while lines[count][-2] != ';':
            points_list.extend(lines[count+1].replace(' ',',').replace('"',',').split(',')[:-1])
            count += 1
        points_list.extend(lines[x+3].replace(' ',',').replace('"',',').split(',')[2:4])
        for y in range(1,len(points_list),2):
            points_list[y]=(float(self.height_dot)-float(points_list[y])/2+float(self.node_height))
        for z in range(0,len(points_list),2):
            points_list[z]=float(points_list[z])/2+float(self.X_OFFSET)
        aLine = self.c.create_line(points_list, fill = 'black',arrow = 'last',smooth = True)
        self.items.append('edge '+lines[x].replace('->','').replace('\t','').replace('"','').split(' ')[0]+' '+lines[x].replace('->','').replace('\t','').replace('"','').split(' ')[2])
        if self.SHOW_EDGE_LBL:
            label = lines[x].replace(',','=').split('=')[1]
            X = float(lines[x+2].replace(',','"').split('"')[1])+self.X_OFFSET
            Y = self.height_dot-float(lines[x+2].replace(',','"').split('"')[2])+self.node_height
            aLabel = self.c.create_text(X,Y,text = label,fill = 'black',font = ("Times", 8))
            self.items.append('label ')

if __name__ == '__main__':
    grph = graphing()
    grph.main('chipgraph')
