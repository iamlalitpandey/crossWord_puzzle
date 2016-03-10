# -*- coding: utf-8 -*-
"""
Created on Wed Mar 09 09:19:49 2016

@author: lalit
"""
import re 

#This function will generate the Transposed Pattern file required for vertical search
def getTranspose(filename):
    with open(filename, 'r') as fconn:
        lines = map(str.strip, fconn.readlines()[0:])
        maxx = len(max(lines, key=len))
        text=[]             # this list wil have the transposed elements        
        for i in range(maxx):
            l = ''
            for line in lines:
                try:
                    l += line[i]
                except :
                    l += ' '
            text.append(l)
        return text

#List for input file of words
words = []
for word in open('words.txt'):
    words.append(word.strip())
    #print word

#hboards is the default/given pattern in which text needs to be searched     
hboards=[] 
for line in open('puzzle.txt'):
    hboards.append(line.strip())    #take default pattern in list as hboards

#This loop will check for every word,if word exists in hboard-pattern for left to right & right to left.
for word in words:
    hline=1
    curr_word=word
    for line in hboards:
        hline+=1 # this will gove you the line number 
        curr_line=line
        position=re.search(curr_word,curr_line)
        if position!=None:
            print curr_word," is present in horizontal line :",hline-1,", Left to Right."
        
        #Reversing the pattern to search the text right to left.(required because search can be only left to right)
        rcurr_line=curr_line[::-1]
        position=re.search(curr_word,rcurr_line)        
        if position!=None:
            print curr_word," is present in horizontal line :",hline-1,", Right to Left."

#Creating vboards because regex can search on horizontal lines only.Hence transposed the default pattern as vboards.
vboards=getTranspose('puzzle.txt')
#print vboards

#This loop will check for every word,if word exists in vboard-pattern for left to right & right to left
for word in words:
    vline=1
    curr_word=word
    for line in vboards:
        vline+=1
        curr_line=line
        position=re.search(curr_word,curr_line)
        if position!=None:
            print curr_word," is present in vertical line :",vline-1,", Top to Bottom."
        rcurr_line=curr_line[::-1]
        position=re.search(curr_word,rcurr_line)        
        if position!=None:
            print curr_word," is present in vertical line :",vline-1,", Bottom to Top."
            
