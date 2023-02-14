import pandas as pd 
from pyvis.network import Network
import numpy as np 

PI = 3.141592653589793238    
def makeNetwork(nodeListName, edgeListName, nodeMapName):
    #init the network
    
    nodeList = pd.read_csv(nodeListName)
    edgeList = pd.read_csv(edgeListName)
    print(nodeList.to_string())
    print(edgeList.to_string())
    nodeNetwork = Network()

    for row in nodeList.iterrows():
        #add nodes to the list
        print(row["id"])
        print(row["name"])
        nodeNetwork.add_node(n_id = row["id"], label = row["name"])
    for row in edgeList.iterrows():
        
        lat1 = nodeList["latitude"].loc[nodeList.index[row["from"]-1]]/(180/PI)
        lat2 = nodeList["latitude"].loc[nodeList.index[row["to"]-1]]/(180/PI)
        long1 = nodeList["longitude"].loc[nodeList.index[row["from"]-1]]/(180/PI)
        long2 = nodeList["longitude"].loc[nodeList.index[row["to"]-1]]/(180/PI)
    
        #TODO: Make sure to double check on how sin cos and arccos take in degrees or radians
        dist = 6378.8 * np.arccos(np.sin(lat1) * np.sin(lat2) + np.cos(lat1) * np.cos(lat2) * np.cos(long2 - long1))
        nodeNetwork.add_edge(row["from"], row["to"], weight = dist, title = dist)
        
    nodeNetwork.barnes_hut()
    nodeNetwork.save_graph(nodeMapName) 
    return nodeNetwork
