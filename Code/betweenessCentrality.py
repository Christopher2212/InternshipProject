import pandas as pd 
from pyvis.network import Network
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall


def getBetweenessArray(nodeNetwork):
    disArray = getDistanceArray(nodeNetwork)

    return

def getDistanceArray(nodeNetwork):
    numNodes = nodeNetwork.num_nodes()

    nodeList = nodeNetwork.get_nodes()

    dArray = []
    
    for i in numNodes:
        row = []
        for j in numNodes:
            

    return