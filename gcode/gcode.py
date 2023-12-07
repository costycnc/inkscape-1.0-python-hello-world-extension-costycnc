import inkex
from inkex import bezier
from inkex.elements import Group, Line


class hello(inkex.EffectExtension):

    def effect(self):
        g="G21 F500 G90\nG92 X0 Y0\n"
        current_layer = self.svg.get_current_layer()
        path_list = current_layer.xpath('./svg:path')
        first = True
        if len(path_list) < 1:
            self.msg('No path found !')
            return
        for path in path_list:
            csp_list = path.path.to_superpath()
            bezier.cspsubdiv(csp_list, 1)           
            for csp in csp_list:                
                first=True
                for cord in csp:
                    g +="G01 X"+"{:.2f}".format(cord[0][0])+" Y"+"{:.2f}".format( cord[0][1])+"\n"                   
                    if first:
                        first=False
                        g +="G01 Z5\n"
                g +="G01 Z0\n"
 
        g +="G01 Y0\nG01 X0" 
        with open("gcode.nc", "w") as f:
            f.write(g)
		
if __name__ == '__main__':
    hello().run()
