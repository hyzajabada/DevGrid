from tkinter import *
import Node
import os
import subprocess

fileName = os.path.join(os.environ.get('APPDATA'), 'Multichain', 'DevGrid', 'multichain.conf')

if os.path.isfile(fileName) == False:
    subprocess.call(['multichaind', 'DevGrid@18.195.171.99:9541', '-daemon'])

node = Node.Node(fileName)
root = Tk()


def printInfo():
    node.printInfo()


getInfoBtn = Button(root, text="Get info", command=printInfo)
getInfoBtn.pack()

root.mainloop()
