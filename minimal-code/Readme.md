
# Inkscape Minimal Extension - Line & Path Examples

![Inkscape](https://img.shields.io/badge/Inkscape-1.0+-blue.svg) ![Python](https://img.shields.io/badge/Python-3.x-green.svg) ![Minimal](https://img.shields.io/badge/Code-Minimal-red.svg)

## 📖 Description

This is a **minimal code example** for creating Inkscape extensions that generate vector elements with just a few lines of code.

Two examples are included:
- **Draw a Line** - Creates a blue line from (0,0) to (100,100)
- **Draw a Path** - Creates a square path using SVG path syntax

> **🎯 Goal:** Learn the absolute basics of Inkscape extension development with minimal, easy-to-understand code!

## 📁 Extension structure

Each extension requires **two files**:

| File | Purpose |
|------|---------|
| `name.inx` | XML description file (tells Inkscape about your extension) |
| `name.py` | Python script (does the actual work) |

### Example 1: Line extension (`line.inx` + `line.py`)

**Python code (`line.py`):**
```python
import inkex
from inkex.elements import Line

class tutorial(inkex.EffectExtension):

    def effect(self):
    
        line = self.svg.add(Line(x1='0', y1='0', x2='100', y2='100'))
        line.style = {'stroke-width': 3, 'stroke': 'blue'}  
        
if __name__ == '__main__':
    tutorial().run()
```

**What this does:**
- Creates a line from (0,0) to (100,100)
- Sets stroke width = 3 pixels
- Sets stroke color = blue

---

### Example 2: Path extension (`path.inx` + `path.py`)

**Python code (`path.py`):**
```python
import inkex
from inkex.elements import PathElement

class tutorial(inkex.EffectExtension):

    def effect(self):
    
        self.svg.add(PathElement(d='M 0 0 L 0 100 L 100 100 L 100 0 L 0 0 z'))
        
if __name__ == '__main__':
    tutorial().run()
```

**What this does:**
- Creates a square path using SVG path syntax
- `M 0 0` = Move to (0,0)
- `L 0 100` = Line to (0,100)
- `L 100 100` = Line to (100,100)
- `L 100 0` = Line to (100,0)
- `L 0 0` = Line back to (0,0)
- `z` = Close path

## 🚀 Installation

### Step 1: Create the folder structure

Create a folder named `minimal-code` containing:

```
minimal-code/
├── line.inx
├── line.py
├── path.inx
└── path.py
```

### Step 2: Copy to Inkscape extensions folder

Copy the entire `minimal-code` folder to:

```
C:\Program Files\Inkscape\share\inkscape\extensions
```

Or for user installation (no admin rights):

```
C:\Users\YOUR_USERNAME\AppData\Roaming\inkscape\extensions
```

### Step 3: Restart Inkscape

Close and reopen Inkscape for changes to take effect.

## 🎮 How to use

### Using the Line extension:

1. Open Inkscape
2. Go to `Menu > Extensions > Minimal > Draw Line`
3. A blue line will appear on your canvas

### Using the Path extension:

1. Open Inkscape
2. Go to `Menu > Extensions > Minimal > Draw Square Path`
3. A square will appear on your canvas

> 🔍 **If you don't find "Minimal" in the Extensions menu... something went wrong with the installation!**

## 📝 Required .inx files

### `line.inx`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<inkscape-extension xmlns="http://www.inkscape.org/namespace/inkscape/extension">
    <name>Draw Line</name>
    <id>minimal.line</id>
    <effect>
        <object-type>all</object-type>
        <effects-menu>
            <submenu name="Minimal"/>
        </effects-menu>
    </effect>
    <script>
        <command location="inx" interpreter="python">line.py</command>
    </script>
</inkscape-extension>
```

### `path.inx`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<inkscape-extension xmlns="http://www.inkscape.org/namespace/inkscape/extension">
    <name>Draw Square Path</name>
    <id>minimal.path</id>
    <effect>
        <object-type>all</object-type>
        <effects-menu>
            <submenu name="Minimal"/>
        </effects-menu>
    </effect>
    <script>
        <command location="inx" interpreter="python">path.py</command>
    </script>
</inkscape-extension>
```

## 🔧 Code Breakdown

### Line extension breakdown:

```python
import inkex                         # Import the main Inkscape extension library
from inkex.elements import Line      # Import the Line element class

class tutorial(inkex.EffectExtension):  # Create extension class
    
    def effect(self):                   # Main method that runs when extension is called
    
        line = self.svg.add(Line(x1='0', y1='0', x2='100', y2='100'))
        # self.svg.add()    → Adds element to the current SVG document
        # Line(...)         → Creates a line with coordinates (x1,y1) to (x2,y2)
        
        line.style = {'stroke-width': 3, 'stroke': 'blue'}  
        # Sets line appearance: 3px thick, blue color

if __name__ == '__main__':
    tutorial().run()  # Run the extension
```

### Path extension breakdown:

```python
import inkex                           # Import main library
from inkex.elements import PathElement # Import Path element class

class tutorial(inkex.EffectExtension):  # Create extension class
    
    def effect(self):                    # Main method
    
        self.svg.add(PathElement(d='M 0 0 L 0 100 L 100 100 L 100 0 L 0 0 z'))
        # self.svg.add()           → Adds element to SVG document
        # PathElement(d='...')     → Creates path with SVG syntax
        # d=...                    → The 'd' attribute contains path data:
        #   M 0 0   = Move to (0,0)
        #   L 0 100 = Line to (0,100)
        #   L 100 100 = Line to (100,100)
        #   L 100 0 = Line to (100,0)
        #   L 0 0   = Line to (0,0)
        #   z       = Close path (connect back to start)

if __name__ == '__main__':
    tutorial().run()  # Run the extension
```

## 🎨 SVG Path Syntax Quick Reference

| Command | Meaning | Example |
|---------|---------|---------|
| `M x y` | Move to (absolute) | `M 10 20` |
| `m dx dy` | Move to (relative) | `m 10 20` |
| `L x y` | Line to (absolute) | `L 100 200` |
| `l dx dy` | Line to (relative) | `l 100 200` |
| `z` or `Z` | Close path | `z` |
| `H x` | Horizontal line | `H 50` |
| `V y` | Vertical line | `V 50` |

### Example paths you can try:

```python
# Triangle
d='M 0 100 L 50 0 L 100 100 z'

# Rectangle (same as square example)
d='M 0 0 L 0 100 L 100 100 L 100 0 z'

# Cross
d='M 50 0 L 50 100 M 0 50 L 100 50'

# Star outline
d='M 50 0 L 61 35 L 98 35 L 68 57 L 79 90 L 50 70 L 21 90 L 32 57 L 2 35 L 39 35 z'
```

## 🎨 Styling Options for Lines and Paths

You can add styles to your elements:

```python
# For lines
line.style = {
    'stroke-width': '5',
    'stroke': 'red',
    'stroke-dasharray': '5,5',  # Dashed line
    'opacity': '0.8'
}

# For paths
path.style = {
    'fill': 'yellow',
    'stroke': 'black',
    'stroke-width': '2',
    'fill-opacity': '0.5'
}
```

## ❗ Troubleshooting

| Problem | Solution |
|---------|----------|
| Extension not showing in menu | Restart Inkscape completely |
| No "Minimal" submenu | Check files are in correct folder with .inx extension |
| Python error | Make sure .py files have no syntax errors |
| Nothing appears on canvas | Check that the coordinates are within view (zoom out) |
| File not found | Use user extensions folder if you lack admin rights |

## 📊 Menu Structure after installation

```
Extensions
├── Minimal (NEW!)
│   ├── Draw Line
│   └── Draw Square Path
├── Render
├── Generate from Path
└── ...
```

## 🔄 Next steps to learn

Once you understand these basics, you can:

1. **Add user input** - Create dialogs with parameters
2. **Modify existing elements** - Select and change existing objects
3. **Generate complex paths** - Create SVG programmatically
4. **Add transformations** - Move, rotate, scale elements
5. **Export data** - Generate G-code, plots, or reports

## 📚 Educational Value

These examples teach:

- ✅ How Inkscape extensions are structured
- ✅ Basic Python syntax for Inkscape
- ✅ How to add elements programmatically
- ✅ SVG coordinate systems
- ✅ Path syntax fundamentals
- ✅ Minimal working examples (no extra complexity)

## 📝 License

This is **educational code** - completely free to use, modify, and share!

## 🙏 Acknowledgments

Created as a **minimal tutorial** for absolute beginners to Inkscape extension development.

---

**Start simple, learn fast, build amazing things!** 🚀🎨

<img src="https://raw.githubusercontent.com/costycnc/inkscape-1.0-hello-world-extension-costycnc/main/minimal-code/minimal.jpg"> 


