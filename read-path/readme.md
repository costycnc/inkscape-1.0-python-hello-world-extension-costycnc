
# Inkscape Path Info Extension - Selected Path Only

![Inkscape](https://img.shields.io/badge/Inkscape-1.0+-blue.svg) ![Python](https://img.shields.io/badge/Python-3.x-green.svg) ![Status](https://img.shields.io/badge/Status-Tutorial%20Example-yellow.svg)

## 📖 Description

This is a **minimal example** extension that works **only with paths** and **only if they are selected**!

It demonstrates how to:
- Detect selected elements in Inkscape
- Filter for `PathElement` only
- Access path data (CSP format)
- Print information to the Inkscape console

> ⚠️ **IMPORTANT:** This extension works **only with paths** and **only if at least one path is selected!**

## 🎯 What it does

- Checks for selected paths in the current document
- Filters the selection for `PathElement` objects only
- Converts each selected path to Superpath (CSP) format
- Prints the path data to the Inkscape message console
- Ready to be extended for file output (e.g., G-code generation)

## 📋 Requirements

Before using this extension:
1. **Select at least one path** in your Inkscape document
2. If your object is not a path, convert it using: `Menu > Path > Object to Path`

## 🚀 Installation

### Installation steps:

1. Copy `path.inx` and `path.py` to the Inkscape extensions folder:

```
C:\Program Files\Inkscape\share\inkscape\extensions
```

2. **Restart Inkscape**

### Alternative location (no admin rights required):

```
C:\Users\YOUR_USERNAME\AppData\Roaming\inkscape\extensions
```

## 💻 How to use

1. **Draw or import** a shape in Inkscape
2. **Convert to path** if needed (`Path > Object to Path`)
3. **Select the path(s)** you want to analyze
4. Go to `Menu > Extensions > Hello World > Path Info` (or whatever name you define in the .inx file)
5. **Run the extension**
6. Check the **console output** (Inkscape will show a message dialog with path data)

## 🔧 The Code Explained

```python
import inkex

class hello_world(inkex.EffectExtension):

    def effect(self):
    
        # Filter selection: keep only PathElement objects
        for node in self.svg.selection.filter(inkex.PathElement):
            
            # Convert path to Superpath format (CSP - Curve Super Path)
            csp_list = node.path.to_superpath()
            
            # Print the path data to Inkscape console
            self.msg(csp_list)
            
            # Commented example code for modifying the path:
            # node.path += [["M", [0, 0]]]      # Move to (0,0)
            # node.path += [["L", [f, h]]]      # Line to (f,h)
            
        # Commented code for writing to file:
        # with open("aaa.nc", "w") as f:
        #     f.write("aaaa")
            
if __name__ == '__main__':
    hello_world().run()
```

### Key lines explained:

| Code | What it does |
|------|--------------|
| `self.svg.selection` | Gets all selected elements |
| `.filter(inkex.PathElement)` | Filters to keep only path elements |
| `node.path.to_superpath()` | Converts path to Superpath (CSP) format - a list of bezier curves |
| `self.msg(csp_list)` | Prints the CSP data to Inkscape's message console |
| `node.path += [["M", [0, 0]]]` | Example: adds a "Move to" command to the path |

## 📊 Example Output

When you run this extension on a selected path, you'll see something like:

```
[[[[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]], [[100.0, 0.0], [100.0, 0.0], [100.0, 0.0]], [[100.0, 100.0], [100.0, 100.0], [100.0, 100.0]], [[0.0, 100.0], [0.0, 100.0], [0.0, 100.0]]]]
```

### Understanding CSP (Superpath) format:

A Superpath (CSP) is a list of subpaths. Each subpath is a list of bezier curves, and each bezier curve has 3 points:
- **Point 1**: Control point before
- **Point 2**: Anchor point
- **Point 3**: Control point after

For straight lines, all three points are identical.

## 🎮 Sample .inx file

Create a `path.inx` file like this:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<inkscape-extension xmlns="http://www.inkscape.org/namespace/inkscape/extension">
    <name>Path Info</name>
    <id>hello.pathinfo</id>
    <effect>
        <object-type>all</object-type>
        <effects-menu>
            <submenu name="Hello World"/>
        </effects-menu>
    </effect>
    <script>
        <command location="inx" interpreter="python">path.py</command>
    </script>
</inkscape-extension>
```

## 🔄 Extending the extension

Here are some ideas for extending this basic example:

### 1. Add file output (G-code style)

```python
def effect(self):
    output = ""
    for node in self.svg.selection.filter(inkex.PathElement):
        csp_list = node.path.to_superpath()
        for subpath in csp_list:
            for point in subpath:
                output += f"X{point[1][0]:.2f} Y{point[1][1]:.2f}\n"
    
    with open("output.txt", "w") as f:
        f.write(output)
    
    self.msg("File saved!")
```

### 2. Show path information

```python
def effect(self):
    count = 0
    for node in self.svg.selection.filter(inkex.PathElement):
        count += 1
        self.msg(f"Path {count}: {node.path}")
    
    if count == 0:
        self.msg("No path selected!")
```

### 3. Modify selected paths

```python
def effect(self):
    for node in self.svg.selection.filter(inkex.PathElement):
        # Add a line to the path
        node.path += [["L", [200, 200]]]
```

### 4. Get path bounding box

```python
def effect(self):
    for node in self.svg.selection.filter(inkex.PathElement):
        bbox = node.bounding_box()
        self.msg(f"Path bounds: X={bbox.x:.0f} to {bbox.right:.0f}, Y={bbox.y:.0f} to {bbox.top:.0f}")
```

## ❗ Troubleshooting

| Problem | Solution |
|---------|----------|
| "No output" or empty message | Make sure you have **selected a path** before running |
| Nothing happens | Check that your object is a path (`Path > Object to Path`) |
| Extension not in menu | Restart Inkscape after copying files |
| Error message about selection | The extension expects at least one path selected |
| Wrong folder selected | Use user extensions folder if you lack admin rights |

## 📋 Menu structure after installation

```
Extensions
├── Hello World (or whatever submenu name you choose)
│   └── Path Info
├── Render
├── Generate from Path
└── ...
```

## 🎯 Use cases for this pattern

This basic structure can be used for:

- ✂️ **Path analyzers** - Get information about selected paths
- 📐 **Path modifiers** - Scale, rotate, or transform selected paths
- 🔄 **Path exporters** - Export path data to custom formats (G-code, DXF, etc.)
- 📊 **Path statistics** - Calculate length, area, or number of points
- 🎨 **Path generators** - Create new paths based on selected ones

## 🔗 Next steps

Once you understand this basic example, you can:

1. **Uncomment the file writing code** to save path data to a file
2. **Add coordinates formatting** for G-code generation
3. **Process multiple paths** with different settings
4. **Add user interface** with parameters (using `<param>` in .inx file)
5. **Create complex transformations** on selected paths

## 📝 Educational value

This tutorial teaches:

- ✅ How to access **selected elements** in Inkscape
- ✅ How to **filter** specific element types
- ✅ How to read **path data** (CSP/Superpath format)
- ✅ How to **output messages** to the user
- ✅ Foundation for **file export** extensions
- ✅ How to **modify existing paths**

## 📄 License

This is **educational code** - completely free to use, modify, and share!

---

**Remember: Select a path first, or nothing will happen!** 🎯🔷
