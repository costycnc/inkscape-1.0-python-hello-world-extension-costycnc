from inkex.elements import PathElement

class tutorial(inkex.EffectExtension):

    def effect(self):
    
        self.svg.add(PathElement(d='M 0 0 L 0 100 L 100 100 L 100 0 L 0 0 z'))
		
if __name__ == '__main__':
    tutorial().run()
