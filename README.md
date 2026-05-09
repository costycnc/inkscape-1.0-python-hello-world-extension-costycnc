
# Inkscape Hello World Extension - Tutorial Example

![Inkscape](https://img.shields.io/badge/Inkscape-1.0+-blue.svg) ![Python](https://img.shields.io/badge/Python-3.x-green.svg) ![Beginner](https://img.shields.io/badge/Level-Beginner-brightgreen.svg)

## 📖 Description

A **simple "Hello World" extension** for Inkscape - the most minimal example possible!

This is the perfect starting point for learning how to create Inkscape extensions. It does one simple thing: displays a message box saying "Hello World!".

> 🎯 **Goal:** Learn the absolute basics of Inkscape extension development with the smallest possible working example.

## 🎯 What it does

- Displays a popup message in Inkscape
- Message: *"Tutorial - your first extension hello world!"*
- Perfect for testing if your extension system works

## 🚀 Installation

### Step 1: Prepare the files

Create two files:

**`hello.py`** (the Python script):
```python
import inkex

class hello_world(inkex.EffectExtension):

    def effect(self):
        self.msg("Tutorial - your first extension hello world!")

if __name__ == '__main__':
    hello_world().run()
```

**`hello.inx`** (the XML description - see below)

### Step 2: Copy to Inkscape extensions folder

Copy both files to:

```
C:\Program Files\Inkscape\share\inkscape\extensions
```

### Step 3: Restart Inkscape

Close and reopen Inkscape for changes to take effect.

## 💻 How to use

1. **Open Inkscape**
2. Go to `Menu > Extensions > Hello World > Tutorial` (or whatever name you define)
3. A **popup message** will appear with the text
4. Click OK to continue

## 📝 The .inx file (XML description)

Create `hello.inx` with this content:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<inkscape-extension xmlns="http://www.inkscape.org/namespace/inkscape/extension">
    <name>Tutorial</name>
    <id>hello.world</id>
    <effect>
        <object-type>all</object-type>
        <effects-menu>
            <submenu name="Hello World"/>
        </effects-menu>
    </effect>
    <script>
        <command location="inx" interpreter="python">hello.py</command>
    </script>
</inkscape-extension>
```

### .inx file explained:

| XML Tag | Purpose |
|---------|---------|
| `<name>` | Name shown in the menu |
| `<id>` | Unique identifier for the extension |
| `<submenu>` | Menu category where the extension appears |
| `<command>` | Tells Inkscape which Python file to run |

## 🔧 Code explained

```python
import inkex
```
Imports the Inkscape extension library - required for any extension.

```python
class hello_world(inkex.EffectExtension):
```
Creates a new class that inherits from `EffectExtension` (the base class for most extensions).

```python
def effect(self):
```
The main method that runs when the extension is called.

```python
self.msg("Tutorial - your first extension hello world!")
```
Displays a message box with the text. This is the **only line that does something visible**!

```python
if __name__ == '__main__':
    hello_world().run()
```
Runs the extension when the script is executed.

## 📊 Menu structure after installation

```
Extensions
├── Hello World (NEW!)
│   └── Tutorial
├── Render
├── Generate from Path
├── Images
└── ...
```

## ✅ Testing checklist

After installation, verify:

- [ ] Files are in the correct folder
- [ ] Inkscape has been restarted
- [ ] The "Hello World" submenu appears in Extensions menu
- [ ] "Tutorial" appears under the submenu
- [ ] Clicking it shows a popup message
- [ ] The message contains the correct text

## ❗ Troubleshooting

| Problem | Solution |
|---------|----------|
| Extension not in menu | Restart Inkscape completely (not just close document) |
| "Hello World" submenu missing | Check files are in the correct folder |
| Error message appears | Check Python syntax (copy exactly as shown) |
| Nothing happens | Make sure both .inx and .py have the exact same name (hello.inx / hello.py) |
| Permission denied | Use user extensions folder (AppData/Roaming) instead |
| Wrong interpreter error | Check `<interpreter="python">` in .inx file |

### Alternative installation folder (no admin rights):

```
C:\Users\YOUR_USERNAME\AppData\Roaming\inkscape\extensions
```

But note: the .inx file must be modified to specify the full path:

```xml
<script>
    <command location="inx" interpreter="python">
        C:\Users\YOUR_NAME\AppData\Roaming\inkscape\extensions\hello.py
    </command>
</script>
```

Or simply use the location attribute with relative path (simpler):

```xml
<script>
    <command location="inx" interpreter="python">hello.py</command>
</script>
```

## 🎓 What you learned

This minimal example teaches:

1. ✅ **Basic structure** of an Inkscape extension
2. ✅ **Two required files**: .inx (XML) and .py (Python)
3. ✅ **Where to install** extensions
4. ✅ **How to display messages** to users
5. ✅ **The class inheritance pattern** (`inkex.EffectExtension`)
6. ✅ **The `effect()` method** - where all the action happens
7. ✅ **How to run** an extension (`.run()`)

## 🔄 Next steps - Building on Hello World

Once this works, try these small modifications:

### 1. Change the message

```python
self.msg("Hello from my custom extension!")
```

### 2. Add multiple messages

```python
self.msg("First message")
self.msg("Second message")
self.msg("Third message")
```

### 3. Show a warning instead

```python
self.msg("Warning: This is just a demo!", style="warning")
```

### 4. Get document information

```python
def effect(self):
    doc_name = self.svg.getfilename()
    self.msg(f"Document: {doc_name}")
```

### 5. Add a simple calculation

```python
def effect(self):
    width = self.svg.get_viewbox_width()
    height = self.svg.get_viewbox_height()
    self.msg(f"Document size: {width} x {height}")
```

## 📁 File naming convention

| File | Naming rule | Example |
|------|-------------|---------|
| `.inx` | Must match `.py` name | `hello.inx` ↔ `hello.py` |
| `.py` | Can be any valid name | `my_extension.py` |

## 🎨 Customizing the menu

Change the `.inx` file to place your extension anywhere:

```xml
<!-- Different submenu name -->
<submenu name="My Tools"/>

<!-- No submenu (appears directly under Extensions) -->
<effects-menu/>

<!-- Multiple levels -->
<submenu name="My Tools/Test/Example"/>
```

## 💡 Pro tips

1. **Keep the code simple** - start with Hello World and build up
2. **Test frequently** - small changes, test often
3. **Check the console** - Inkscape has a debug console (Extensions > Development > Debug console)
4. **Use `self.msg()` for debugging** - it's like `print()` for Inkscape
5. **Backup your files** - before modifying working extensions

## 📚 Additional resources

- Inkscape Extension Documentation
- inkex Python module reference
- Other examples in the extensions folder

## 📝 License

This is **educational code** - completely free to use, modify, and share!

## 🙏 Acknowledgments

The classic "Hello World" example - the first step in learning any programming language or platform.

---

**Congratulations! You've created your first Inkscape extension!** 🎉🚀

*Now go build something amazing!*

<img src="https://raw.githubusercontent.com/costycnc/inkscape-1.0-hello-world-extension-costycnc/main/extension.jpg"> 

<img src="https://raw.githubusercontent.com/costycnc/inkscape-1.0-hello-world-extension-costycnc/main/hello.jpg"> 


