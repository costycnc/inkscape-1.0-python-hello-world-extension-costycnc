import inkex,sys,math,time,ctypes
from inkex import bezier
from inkex.elements import Group, Line,Circle,PathElement




class tutorial(inkex.EffectExtension):

    def effect(self):
        
        self.svg.add(Line(x1='0', y1= '0', x2='100', y2='100'))
        line1.style = {'stroke-width': 3, 'stroke': 'blue'}  
		
if __name__ == '__main__':
    tutorial().run()
