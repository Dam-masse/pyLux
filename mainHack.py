# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 17:24:13 2019

@author: Damiano Massella
just to test git capabilities
"""
import pyperclip



def addingset(original):
    original=original.rstrip()
    if len(original)!=0:
        if original[-1]==';' or original[0]=='#':
            new=original
        else:
            new='set(\''
            line=original.split(',')
            setproperty=line[0].rstrip()
            new=new+setproperty+'\','
            setvalue=line[1].rstrip()
            setvalue=line[1].lstrip()
            if setvalue[-1]=='!':
                setvalue=setvalue.replace('!','')
                setvalue='\''+setvalue+'\''
            new=new+setvalue
            new=new+');'
    else:
        new=original
    return new



def execution(readfile):
    readfilename=readfile
    readfile=open(readfilename)
    writefilename='write_out.txt'
    writefile=open(writefilename,'w+')
    line=readfile.readline()
    while line:
        print(line)
        # here we apply the function 
        #write to the wrining file
        if len(line)>2:
            fout=addingset(line)+'\n'
        else:
            fout='\n'
        print(fout)
        writefile.write(fout)
        line=readfile.readline()
        
    readfile.close()
    writefile.close()
    fo=open(writefilename,'r')
    pyperclip.copy(fo.read())
    fo.close()
    print('the result is copied in your clipboard and in the write_out.txt file')

    
    
    
    
    
    
    
    
    