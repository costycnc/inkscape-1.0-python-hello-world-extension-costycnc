Inkscape Python Extension – Hello World Example

This project is a minimal educational extension for Inkscape 1.0+, written in Python using the inkex API.

It demonstrates the basic structure of an Inkscape extension and how to create and manipulate SVG elements programmatically.

📌 What this extension does

When executed, the extension:

Creates a new SVG layer
Draws a red square (path element)
Adds a blue diagonal line inside the layer
Applies simple transforms and styles

The result is a simple visual demonstration of how Inkscape extensions can generate vector graphics.

🎯 Purpose

This project is designed as a learning resource, not a production tool.

It helps you understand:

How Inkscape extensions are structured
How the inkex Python API works
How to create SVG elements programmatically
How to apply transformations and styles
🧠 What you will learn
Creating custom extensions for Inkscape
Using EffectExtension base class
Working with SVG elements like:
Group
PathElement
Line
Manipulating document structure and layers
🧩 How it works

The extension:

Creates a new layer in the current document
Generates a square path using SVG commands
Centers the shape in the canvas
Applies red fill styling
Adds a blue diagonal line
🚀 Example output
Create element ... in this case square

put square.inx and square.py in C:\Program Files\Inkscape\share\inkscape\extensions

<img src="https://raw.githubusercontent.com/costycnc/inkscape-1.0-hello-world-extension-costycnc/main/create-square/square.jpg"> 

for see xml document goto menu Edit > XML editor

<img src="https://raw.githubusercontent.com/costycnc/inkscape-1.0-hello-world-extension-costycnc/main/create-square/editor.jpg"> 
You will see:

A red square shape
A blue diagonal line crossing the square
All elements placed inside a new layer
📂 Requirements
Inkscape 1.0 or higher
Python 3.x
inkex (included with Inkscape extensions environment)
🛠 Usage
Copy the extension into your Inkscape extensions folder
Restart Inkscape
Run the extension from the Extensions menu
⚠️ Notes
This is a minimal example
It is intended for educational purposes only
You can extend it to create more complex drawing tools
📚 Possible next steps
Add user input parameters (GUI)
Generate dynamic shapes
Create reusable drawing tools
Build advanced SVG automation scripts
👤 Author

costycnc
