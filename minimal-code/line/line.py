import inkex
from inkex.elements import Line

class tutorial(inkex.EffectExtension):

    def effect(self):
    
        line=self.svg.add(Line(x1='0', y1= '0', x2='100', y2='100'))
        line.style = {'stroke-width': 3, 'stroke': 'blue'}  
		
if __name__ == '__main__':
    tutorial().run()
