
# Inkscape Python Extension – Hello World (Create Square)

This project is a minimal educational extension for Inkscape 1.0+, written in Python using the `inkex` API.

It demonstrates how to create a basic Inkscape extension and how to generate and manipulate SVG elements programmatically.

---

## 🧩 What this extension does

When executed, this extension:

* Creates a new SVG layer
* Draws a **red square** using a path element
* Adds a **blue diagonal line** inside the square
* Centers the drawing in the current document

The result is a simple visual example of how Inkscape extensions can generate vector graphics.

---

## 🎯 Purpose

This project is designed as a **learning resource**, not a production tool.

It helps you understand:

* How Inkscape extensions are structured
* How the `inkex` Python API works
* How SVG elements are created programmatically
* How transformations and styles are applied

---

## 🧠 What you will learn

* Creating custom extensions for Inkscape
* Using the `EffectExtension` base class
* Working with SVG elements:

  * Group (layers)
  * PathElement (shapes)
  * Line (geometry)
* Manipulating document structure and layers

---

## ⚙️ How it works

The extension:

* Creates a new layer in the current document
* Generates a square using SVG path commands
* Centers the shape in the canvas
* Applies red fill styling
* Adds a blue diagonal line

The square is defined using this SVG path:

```python
M 0 0 L 0 100 L 100 100 L 100 0 z
```

---

## 🚀 Example output

After running the extension, you will see:

* A red square
* A blue diagonal line crossing it
* All elements placed inside a new layer

### Result preview:


<img src="https://raw.githubusercontent.com/costycnc/inkscape-1.0-python-hello-world-extension-costycnc/main/create-square/square.jpg">


---

## 📂 Files included

* `square.py` → Python extension logic
* `square.inx` → Inkscape extension definition
* `square.jpg` → visual output example
* `editor.jpg` → XML structure preview

---

## 🛠 Installation

Copy the files:

* `square.inx`
* `square.py`

into the Inkscape extensions folder:

```text
C:\Program Files\Inkscape\share\inkscape\extensions
```

Then restart Inkscape.

---

## 🔍 Inspect SVG structure

To inspect the generated SVG:

> Go to **Edit → XML Editor**

inside Inkscape


<img src="https://raw.githubusercontent.com/costycnc/inkscape-1.0-python-hello-world-extension-costycnc/main/create-square/editor.jpg">


---

## ⚠️ Notes

* This is a minimal example
* It is intended for educational purposes only
* It can be extended to create more complex drawing tools

---

## 📚 Possible next steps

* Add UI parameters (user input in Inkscape)
* Generate dynamic shapes
* Create reusable drawing tools
* Build more advanced SVG automation scripts

---

## 👤 Author

costycnc
