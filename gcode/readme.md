
# Inkscape G-code Generator - Tutorial Example

![Inkscape](https://img.shields.io/badge/Inkscape-1.0+-blue.svg) ![Python](https://img.shields.io/badge/Python-3.x-green.svg) ![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📖 Description

This is a **practical example** for those who want to learn the basics of **Inkscape extensions** and transform a vector image into **G-code** for 3-axis machines (X, Y, Z).

> **⚠️ IMPORTANT:** This is NOT a finished and solid program... it is only a **tutorial example** with minimal lines of code!

## 🎯 What it does

- Converts a selected path in Inkscape to **G-code**
- Generates code for **3-axis machines (X, Y, Z)**
- Supports basic G-code commands (G01, G21, G90, G92)
- Saves the G-code file automatically

## 📋 Prerequisites

Before using this extension, make sure your object is a **path**. If not, convert it using:

```
Menu > Path > Object to Path
```
(Alternative options: `Stroke to Path` or `Bitmap to Path`)

## 🚀 Installation

### Method 1 (recommended - user extensions)
Copy `gcode.inx` and `gcode.py` to:

```
C:\Users\YOUR_USERNAME\AppData\Roaming\inkscape\extensions
```

### Method 2 (system-wide - requires admin rights)
Copy the files to:

```
C:\Program Files\Inkscape\share\inkscape\extensions
```

> **Note:** This method may give a "file cannot be written" error.

### After installation
1. **Restart Inkscape**
2. The extension will appear in: `Menu > Extensions > helloworld > gcode`

> 🔍 **If you don't find the extension in the menu... it means something went wrong!**

## 💻 How to use

1. **Draw or import** a vector image in Inkscape
2. **Convert to path** if necessary (see Prerequisites)
3. **Select the path** you want to convert
4. Go to `Menu > Extensions > helloworld > gcode`
5. **Run the extension**

## 📁 Output

After execution, you will find the `gcode.nc` file in:

```
C:\Users\YOUR_USERNAME\AppData\Roaming\inkscape\extensions\gcode.nc
```

> **Note:** The `gcode.nc` file will be **overwritten** every time you run the extension.

## 🔧 Code explanation

Here's what your script does step by step:

```python
import inkex
from inkex import bezier
from inkex.elements import Group, Line
```

**Import** the necessary Inkscape modules.

```python
class hello(inkex.EffectExtension):
```
Main class inheriting from `EffectExtension`.

```python
def effect(self):
```
Main method executed by the extension.

```python
g = "G21 F500 G90\nG92 X0 Y0\n"
```
Initializes the G-code with:
- `G21` = millimeter units
- `F500` = feed rate 500 mm/min
- `G90` = absolute positioning
- `G92 X0 Y0` = set current position as origin

```python
current_layer = self.svg.get_current_layer()
path_list = current_layer.xpath('./svg:path')
```
Gets the current layer and finds all paths inside it.

```python
for path in path_list:
    csp_list = path.path.to_superpath()
    bezier.cspsubdiv(csp_list, 1)
```
For each path, converts to CSP (Curve Super Path) format and subdivides it to approximate curves.

```python
for cord in csp:
    g += "G01 X" + "{:.2f}".format(cord[0][0]) + " Y" + "{:.2f}".format(cord[0][1]) + "\n"
```
Generates a `G01` command for each point in the path, formatting coordinates with 2 decimal places.

```python
with open("gcode.nc", "w") as f:
    f.write(g)
```
Saves the generated G-code to the `gcode.nc` file.

## 🎨 Customization - Adding custom commands

The code is **very simple and easy to modify** to add commands like:

```python
# Add at the beginning of the G-code, after initialization:
g += "M03 S1000\n"  # Spindle on at 1000 RPM
g += "G04 P2\n"     # Pause 2 seconds

# Add at the end, before G01 X0 Y0:
g += "M05\n"        # Spindle off
g += "M30\n"        # Program end
```

### Example commands you can add:

| Command | Function |
|---------|----------|
| `M03 S1000` | Spindle on at 1000 RPM |
| `M05` | Spindle off |
| `M08` | Coolant on |
| `M09` | Coolant off |
| `G04 P1` | Pause 1 second |
| `M30` | Program end and reset |

## 📊 Example G-code output

Here's an example of what the extension produces:

```gcode
G21 F500 G90
G92 X0 Y0
G01 X10.50 Y15.20
G01 Z5
G01 Z0
G01 X20.30 Y25.40
G01 X30.10 Y10.80
G01 Y0
G01 X0
```

## ❗ Troubleshooting

| Problem | Solution |
|---------|----------|
| "No path found!" | Make sure you have a path selected (convert object with `Object to Path`) |
| Extension doesn't appear in menu | Restart Inkscape or check the installation folder |
| Permission error | Use the user extensions folder (AppData/Roaming) |
| gcode.nc file not created | Check write permissions in the extensions folder |
| Strange or too large coordinates | Verify your path doesn't have incorrect scale |

## 🔄 Current limitations

- ❌ Does not handle Bezier curves properly (approximates them with straight lines)
- ❌ Does not support multiple layers
- ❌ Does not ask user for settings (feed rate, Z depth, etc.)
- ❌ Does not support arc movements (G02/G03)

## 📈 Possible future improvements

- [ ] Add UI dialog for parameters (Z depth, feed rate)
- [ ] Improve curve handling
- [ ] Support arcs with G02/G03
- [ ] Add option for output filename
- [ ] Handle multiple paths across different layers

## 📝 License

This project is purely **educational** - feel free to use, modify, and share it!

## 🙏 Acknowledgments

Created as an example for the Inkscape community and CNC enthusiasts.

---

**Happy coding and happy CNC cutting!** 🎯⚙️


**Buon coding e buon taglio CNC!** 🎯⚙️
