import re

def reverse( string):
    li = string.split("@")
    sentence = ""
    for item in reversed(li):
    	sentence += "(" + str(item) + ") @ "
    sentence = sentence[0: len(sentence) - 2]  + ";"
    print sentence

reverse("rflags # [8:0] @ b1 @ rflags # [63:10]")