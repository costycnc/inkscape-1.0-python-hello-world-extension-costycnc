
import inkex

class hello_world(inkex.EffectExtension):

    def effect(self):
        self.msg("Tutorial -you first extension hello world!")

if __name__ == '__main__':
    hello_world().run()
