import inkex
from inkex.elements import Group, PathElement

class hello_world(inkex.EffectExtension):

    def effect(self):
        self.msg("Tutorial -you first extension hello world!")
        layer = self.svg.add(Group.new('my_label', is_layer=True))
        layer.append(self.make_a_shape()) 

    def make_a_shape(self):
        my_shape = PathElement()
        # You can set the path through many different methods.
        # Lists of numbers, pythonic objects, Cubic curves etc.
        my_shape.path = "M 0 0 L 0 100 L 100 100 L 100 0 z"
        # Transform can be modified in many ways too
        my_shape.transform.add_translate(self.svg.namedview.center)        
        my_shape.style="fill:red"
        return my_shape

if __name__ == '__main__':
    hello_world().run()
