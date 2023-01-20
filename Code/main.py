import pandas as pd 
from pyvis.network import Network
import numpy as np 

PI = 3.141592653589793238

def main():
    #init the network
    nodeList = pd.read_csv("Other\EdgeandVertListsCSV\BangkokVert.csv")
    edgeList = pd.read_csv("Other\EdgeandVertListsCSV\BangkokEdge.csv")
    print(nodeList.to_string())
    print(edgeList.to_string())
    nodeNetwork = Network()

    for i, row in nodeList.iterrows():
        #add nodes to the list
        print(row["id"])
        print(row["name"])
        nodeNetwork.add_node(n_id = row["id"], label = row["name"])
    for i, row in edgeList.iterrows():
        
        lat1 = nodeList["latitude"].loc[nodeList.index[row["from"]-1]]/(180/PI)
        lat2 = nodeList["latitude"].loc[nodeList.index[row["to"]-1]]/(180/PI)
        long1 = nodeList["longitude"].loc[nodeList.index[row["from"]-1]]/(180/PI)
        long2 = nodeList["longitude"].loc[nodeList.index[row["to"]-1]]/(180/PI)
    
        #TODO: Make sure to double check on how sin cos and arccos take in degrees or radians
        dist = 6378.8 * np.arccos(np.sin(lat1) * np.sin(lat2) + np.cos(lat1) * np.cos(lat2) * np.cos(long2 - long1))
        nodeNetwork.add_edge(row["from"], row["to"], weight = dist)

    nodeNetwork.barnes_hut()
    nodeNetwork.save_graph("nodeMap.html")
    nodeNetwork.show("nodeMap.html")   
    return 
    
if __name__ == "__main__":
    main()


