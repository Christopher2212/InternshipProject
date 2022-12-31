#Going to start with a list of vectors and then a list of edges, we shall see what happens next. 
#Graph them out and hopefully I get a nice chart of nodes pointing to other nodes 
library(igraph)
library(dplyr)
library(ggraph)
library(ggmap)

vertices <- read.csv(file = "S://InternshipProject/Other/EdgeandVertListsCSV/ParisVert.csv")
edgelist <- read.csv(file = "S://InternshipProject/Other/EdgeandVertListsCSV/ParisEdge.csv")


#credit to this awesome person who made this thing: 
#https://towardsdatascience.com/the-5-minute-learn-create-pretty-and-geographically-accurate-transport-maps-in-r-63f2cb77c227

(tubegraph <- igraph::graph_from_data_frame(
d = edgelist, 
vertices = vertices,
directed = FALSE
))

lines <- edgelist |> 
  dplyr::distinct(line, linecolor)
print(lines)
head(tubegraph)
set.seed(123)
head(new_edgelist)
ggraph(tubegraph, layout = "kk") +
  geom_node_point(color = "black", size = 3) +
  geom_edge_link(aes(color = line), width = 1) +
  scale_edge_color_manual(name = "Line", values = lines$linecolor) +
  theme_void()


new_edgelist <- edgelist |> 
  dplyr::inner_join(vertices |> 
                      dplyr::select(id, latitude, longitude), 
                    by = c("from" = "id")) |> 
  dplyr::rename(lat_from = latitude, lon_from = longitude) |> 
  dplyr::inner_join(vertices |> 
                      dplyr::select(id, latitude, longitude), 
                    by = c("to" = "id")) |> 
  dplyr::rename(lat_to = latitude, lon_to = longitude)


tubegraph <- igraph::graph_from_data_frame(
d = new_edgelist, 
vertices = vertices,
directed = FALSE
)