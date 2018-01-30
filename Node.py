from Savoir import Savoir


class Node:

    rpchost = 'localhost'
    rpcport = '7419'
    chainname = 'DevGrid'

    def __init__(self, fileName):

        f = open(fileName, 'r')
        rpcuser = f.readline()
        self.rpcuser = rpcuser.split('=')[1].strip('\n')
        rpcpasswd = f.readline()
        self.rpcpasswd = rpcpasswd.split('=')[1].strip('\n')
        self.api = Savoir(self.rpcuser, self.rpcpasswd, self.rpchost, self.rpcport, self.chainname)

    def printInfo(self):
        print(self.api.getinfo())
