# pyLux
python script for simplify the work with lumerical

this script is made to semplify the process of coding with Lumerical software

The use is quite simple 


1. Prepare a txt file that will contain your lumerical script formatted with the rules that will be mentioned in Formatting
2. Go to the mainHack.py script and modify the last programm line, inserting your txt name and path, or you can load the script as a module and call the function execution( path)
3. The lumerical formatting is copied on your clipboard and in the write_out.txt file in the pyLux directory 
4. Go to lumerical and use paste on and empty editor.


**Installation**

To run correctly the you need to have installed the pyperclip package, use pip install pyperclip if you don't have


**Formatting**

the pylux script is intended to speed up the process of coding in Lumerical,since the most annoying thing in this program is the calling of the set() function.
Using this script you don't have to call this function once. 

rules:


1. All the lines that end with ; are reported as they are, you can use this for simple lumerical function like addrect; . 
2. All the lines without ; are intended as a input for a set function.

in the second case the inputs of the funciton are separated by a , . 

1. The first element of the line is always intended as a parameter for the function and the '' are added automatically,. 
2. The second element is the parameter value and you can use ! after the name to add '' around the element, see the example.


name, waveguide!--> set('name','waveguide');

x span, 10e-6 --> set('x span',10e-6);



