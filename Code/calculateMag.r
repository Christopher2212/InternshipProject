library(dplyr)

edgelist <- read.csv(file = "S://InternshipProject/Other/EdgeandVertListsCSV/ParisEdge.csv")
vertices <- read.csv(file = "S://InternshipProject/Other/EdgeandVertListsCSV/ParisVert.csv")

deg2rad <- function(deg) {(deg * pi) / (180)}
rad2deg <- function(rad) {(rad * 180) / (pi)}

new_edgelist <- edgelist |> 
  dplyr::inner_join(vertices |> 
                      dplyr::select(id, latitude, longitude), 
                    by = c("from" = "id")) |> 
  dplyr::rename(lat_from = latitude, lon_from = longitude) |> 
  dplyr::inner_join(vertices |> 
                      dplyr::select(id, latitude, longitude), 
                    by = c("to" = "id")) |> 
  dplyr::rename(lat_to = latitude, lon_to = longitude)
  


for(i in 1:nrow(new_edgelist)){
    
    lat_from <- (new_edgelist[i,5] * pi) / (180)
    lon_from <- (new_edgelist[i,6] * pi) / (180)
    lat_to <- (new_edgelist[i,7] * pi) / (180)
    lon_to <- (new_edgelist[i,8] * pi) / (180)

    #print(lat_from)
    #print(lon_from)
    #print(lat_to)
    #print(lon_to)

    

    distance <- (3963.0 * (acos((sin(lat_from) * sin(lat_to) + cos(lat_from) * cos(lat_to) * cos(lon_to-lon_from)))))
    
}