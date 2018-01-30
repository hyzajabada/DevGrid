from tkinter import *
import Node
import os
from multiprocessing import Process
import subprocess
import time

SEPARATE_CONSOLE = 0x00000010

def spawnMultichaind(command, chainName, flag):
    subprocess.run([command, chainName, flag],
    stdin=None, stdout=None, stderr=None, close_fds=True, creationflags=SEPARATE_CONSOLE)

if __name__ == '__main__':
    # Get the path using APPDATA env variable.
    fileName = os.path.join(os.environ.get('APPDATA'), 'Multichain', 'DevGrid', 'multichain.conf')

    try:
        # If file isn't there, chain has to be intialised.
        if os.path.isfile(fileName) == False:
            # Spawn separate process to connect to genesis node.
            p1 = Process(target=spawnMultichaind, args=('multichaind', 'DevGrid@18.195.171.99:4269', '-daemon'))
            p1.start()
            # Wait for it to create the multichain.conf file.
            while os.path.isfile(fileName) == False:
                if p1.is_alive() == True:
                    continue
                else:
                    # If file still hasn't been created, but the process
                    # terminated, something went wrong. Throw an error.
                    raise Exception()
            # Now stop this connection because we need to add rpcport to
            # multichain.conf file.
            p2 = Process(target=spawnMultichaind, args=('multichain-cli', 'DevGrid', 'stop'))
            p2.start()
            p2.join(10)
            p1.join(30)
            # Open and append the multichain.conf file
            f = open(fileName, 'a')
            f.write('rpcport=7419')
            f.close()

        # Connect to chain
        p = Process(target=spawnMultichaind, args=('multichaind', 'DevGrid', '-daemon'))
        p.start()

        # Create Node object. It will be used to invoke all blockchain related
        # functions using Savoir API.
        node = Node.Node(fileName)

        # Initialise window
        root = Tk()

        def printInfo():
            node.printInfo()

        getInfoBtn = Button(root, text="Get info", command=printInfo)
        getInfoBtn.pack()

        root.mainloop()
    except:
        print('Failed to connect')
