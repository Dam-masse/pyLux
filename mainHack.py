# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 17:24:13 2019

@author: Damiano Massella
"""
import pyperclip


def addingset(original):
    """ this function add the set () lumerical command line to all the lines that
    do not end with ; 
    the set command require a property and a value they are separated by , 
    if the value is a string, use! for adding the '' """
    if "#" in original:  # splitting the comments from the commands
        splitted = original.split("#")
        comment = " #" + splitted[1]
        original = splitted[0]
    else:
        comment = ""

    original = original.rstrip()
    if len(original) != 0:
        if (
            original[-1] == ";"
        ):  # check if the command is already in the lumerical format
            new = original + comment
        else:

            new = "set('"
            line = original.split(",")
            setproperty = line[0].rstrip()
            new = new + setproperty + "',"
            setvalue = line[1].rstrip()
            setvalue = line[1].lstrip()
            if (
                setvalue[-1] == "!"
            ):  # use the setvalue as a string if the ! is inserted after that
                setvalue = setvalue.replace("!", "")
                setvalue = "'" + setvalue + "'"
            new = new + setvalue
            new = new + ");" + comment
    else:
        new = original
    return new


def execution(readfile):
    """ this function add the set () lumerical command line to all the lines that
    do not end with ;
    the input is a text file containing all the commands for lumerical
    the result is written to the write_out.txt file and copyed to the clipboar 
    the set command require a property and a value they are separated by , 
    if the value is a string, use! for adding the '' """
    readfilename = readfile
    readfile = open(readfilename)  # open the file to read
    writefilename = "write_out.txt"
    writefile = open(writefilename, "w+")  # open the file to write or create it
    line = readfile.readline()
    while line:
        print(line)
        # here we apply the function
        # write to the wrining file
        if len(line) > 2:
            fout = addingset(line) + "\n"
        else:
            fout = "\n"
        print(fout)
        writefile.write(fout)
        line = readfile.readline()

    readfile.close()
    writefile.close()
    fo = open(writefilename, "r")
    pyperclip.copy(fo.read())  # copy the result to the clipboard
    fo.close()
    print("the result is copied in your clipboard and in the write_out.txt file")


execution("./testing.txt")
