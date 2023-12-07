import inkex

class hello_world(inkex.EffectExtension):

    def effect(self):

        for node in self.svg.selection.filter(inkex.PathElement):
            csp_list = node.path.to_superpath()
            self.msg(csp_list)
            #node.path+=[["M", [0, 0]]]
            #node.path+=[["L", [f, h]]]

        with open("aaa.nc", "w") as f:
            f.write("aaaa")
if __name__ == '__main__':
    hello_world().run()
