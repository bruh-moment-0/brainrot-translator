# brainrot translator v1
# takes in brainrotted sentence and gives a more understandable one.
from tkinter import Tk, Label, Button, Entry, IntVar, messagebox, scrolledtext, END, WORD # gui imports
from time import time
import re

DICTIONARY = [ # dictionary is defined here
    # usage: add a comma bellow and add brackets [] and inside add another comma.
    # the left side of the comma is the brainrot equivalent of the rigth side.
    # PLEASE NOTE THAT THE FOLLOWING TEXT IS NOT FOR HARMING ANYBODY, IT IS ONLY TO BE USED FOR
    # CONTEXT IN ONLINE COMUNICATIONS!
    ["pmo", "piss(ed) me off"], ["ts", "this (shit)"], ["icl", "i can't lie"], ["twin", "bro"], ["vro", "bro"],
    ["hb", "home boy (bro)"], ["n", "and"], ["lowk", "lowkey"], ["ngl", "not going to lie"],
    ["kys", "kill yourself"], ["eyp", "eat your pussy OR enjoy your penis"],
    ["lmeyptycomf", "let me eat your pussy till you cum on my face OR let me excite your penis till you cum on my face"],
    ["ik", "i know"], ["stfu", "shut the fuck up"], ["u", "you"], ["sm", "so much"], ["liek", "like"],
    ["ru", "are you"], ["fr", "for real"], ["rn", "rigth now"], ["sybau", "shut your bitch ass up"],
    ["wyd", "[what (are) you doing OR what (would) you do]"], ["nga", "nigga"],
    ["ikiag", "i am going to keep it a gurt"], ["tuff", "tough (impressive, cool)"],
    ["wivs", "[what (are) you doing OR what (would) you do] is very smart"],
    ["yg", "yo gurt"], ["tg", "this (shit) gurt"], ["cbvd", "could be very dangerous"],
    ["itwh", "i know this shit was happening"], ["gurt", "gurt"], ["gurting", "gurting"],
    ["cro", "bro"], ["jorking it", "masturbating"], ["syfm", "shut your fucking mouth"],
    ["sym", "shut your mouth"], ["lmao", "laughing my ass off"], ["lmfao", "laughing my fucking ass off"],
    ["mf", "motherfucker(s)"], ["mfs", "motherfucker(s)"], ["mfers", "motherfucker(s)"],
    ["bru", "bro"], ["bruh", "bro (disbelief, surprise)"], ["on foenem", "i swear"], ["ofn", "i swear"],
    ["on foenem grave", "i am deathly serious"], ["gng", "going OR gang"], ["cya", "see ya (you later)"],
    ["goon", "masturbating"], ["gooner", "degenerate OR masturbator"], ["gooning", "masturbating"],
    ["ez", "easy"], ["buss", "good"], ["bussing", "good OR masturbating and cuming"], ["bussin", "good OR masturbating and cuming"],
    ["rizz", "charisma"], ["bet", "yes"], ["ig", "i guess"], ["ty", "thank you"],
]

DICTIONARY2 = [ # secondary dictionary to add context to certain words that apper more
    ["gurt", "gurt (means doing something that's very smart but also very dangerous)"],
    ["gurting", "gurting (means doing something that's very smart but also very dangerous)"],
    ["till", "untill"]
]

def convert():
    sentence = readscroll(inscroll)
    if not sentence:
        messagebox.showerror("no input", "input is empty")
        return
    start = time()
    sentence = sentence.lower()
    wordcount = 0
    sorteddict = sorted(DICTIONARY, key=lambda x: len(x[0].split()), reverse=True)
    sortedcontext = sorted(DICTIONARY2, key=lambda x: len(x[0].split()), reverse=True)
    placeholders = []
    for i, (brainrot, meaning) in enumerate(sorteddict):
        pattern = r'(?<!\w)' + re.escape(brainrot) + r'(?!\w)'
        placeholder = f"__BR{i}__"
        newsentence, count = re.subn(pattern, placeholder, sentence)
        if count > 0:
            wordcount += 1
        sentence = newsentence
        placeholders.append((placeholder, meaning))
    for placeholder, meaning in placeholders:
        sentence = sentence.replace(placeholder, meaning)
    for brain, contextual in sortedcontext:
        pattern = r'\b' + re.escape(brain) + r'\b'
        sentence = re.sub(pattern, contextual, sentence)
    writescroll(outscroll, sentence)
    end = time()
    messagebox.showinfo("operation done", f"done, converted {wordcount} unique words, took {end-start} seconds")

def updatetext():
    inscroll.config(font=("Consolas", fontsize.get()), width=width.get(), height=height.get())
    outscroll.config(font=("Consolas", fontsize.get()), width=width.get(), height=height.get())

def writescroll(scroll, data):
    scroll.delete(1.0, END)
    scroll.insert(END, data)

def readscroll(scroll):
    return scroll.get("1.0", END).strip()

root = Tk() # root is defined here
fontsize = IntVar(value=11)
height = IntVar(value=20)
width = IntVar(value=80)
root.title("brainrot translator v1")
Label(root, text="brainrot translator v1").grid(row=0, column=0, columnspan=4)
Label(root, text="input").grid(row=1, column=0, columnspan=2)
Label(root, text="output").grid(row=1, column=2, columnspan=2)
inscroll = scrolledtext.ScrolledText(root, height=20, width=80, wrap=WORD, font=("Consolas", 11))
inscroll.grid(row=2, column=0, columnspan=2)
outscroll = scrolledtext.ScrolledText(root, height=20, width=80, wrap=WORD, font=("Consolas", 11))
outscroll.grid(row=2, column=2, columnspan=2)
btn = Button(root, text="convert", command=convert)
btn.grid(row=3, column=0, columnspan=4)
Label(root, text="settings").grid(row=4, column=0)
fontent = Entry(root, width=16, textvariable=fontsize, font=("Consolas", 11))
fontent.grid(row=4, column=1)
heightent = Entry(root, width=16, textvariable=height, font=("Consolas", 11))
heightent.grid(row=4, column=2)
widthent = Entry(root, width=16, textvariable=width, font=("Consolas", 11))
widthent.grid(row=4, column=3)
setbtn = Button(root, text="set", command=updatetext)
setbtn.grid(row=5, column=0)
Label(root, text="font").grid(row=5, column=1)
Label(root, text="height").grid(row=5, column=2)
Label(root, text="width").grid(row=5, column=3)
root.mainloop()
