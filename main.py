from fastapi import Form
from fastapi import FastAPI,Request,Query
import pandas as pd
import folium
from math import radians ,sin,cos,acos,asin,sqrt,atan2
import sys
from heapq import heapify,heappush,heappop
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse,HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
templates =Jinja2Templates(directory="templates")
app = FastAPI()
df = pd.read_excel('coordinates.xlsx')

app.mount("/static", StaticFiles(directory="static"), name="static")

global coordinates;
@app.get("/", response_class=HTMLResponse)
async def landing_page(request: Request):
  
    return templates.TemplateResponse("index.html", {"request": request})
@app.get("/generate_map", response_class=HTMLResponse)
async def generate_map(request: Request,current_destination: str = Query(..., description="current-destination"),final_destination: str = Query(..., description="final-destination"),):

    shortest_distance, shortest_path = dijkstra(graph, current_destination, final_destination)

    mapobj=folium.Map(location=([13.0087337344283, 74.7950647457415]),zoom_start=17)
    coordinates=[]  
    for node in shortest_path:
        row = df[df['From'] == node]
        if not row.empty:
            lat, lon = row.iloc[0]["coordinate"].split(', ')
            coordinates.append([float(lat), float(lon)])
     
    file_path=polyline_generator(coordinates,mapobj)
    return FileResponse(file_path, media_type='text/html')

    
def polyline_generator(coordinates,mapobj):
    folium.PolyLine(
         locations=coordinates,
         color="blue",
         weight=7,
     ).add_to(mapobj)
    folium.Marker(
        location=coordinates[0],
        tooltip="Click me!",
        popup="example",
        icon=folium.Icon(color='darkblue')
     ).add_to(mapobj)
    folium.Marker(
        location=coordinates[len(coordinates)-1],
        tooltip="Click me!",
        popup="example",
        icon=folium.Icon(color='red')
     ).add_to(mapobj)
    file_path="UpdatedMap.html"
    mapobj.save(file_path)
    coordinates.clear()
    return file_path

graph = {}

for index, row in df.iterrows():
    source = row['From']
    destination = row['To']
    distance = row['Distance']

   
    if source not in graph:
        graph[source] = {}
    if destination not in graph:
        graph[destination] = {}

  
        graph[source][destination] = distance
    if source not in graph[destination]:
        graph[destination][source] = distance



def dijkstra(graph, src, dest):
    inf = sys.maxsize
    node_data = {node: {'cost': inf, 'pred': None} for node in graph}
    node_data[src]['cost'] = 0
    min_heap = [(0, src)]

    while min_heap:
        current_cost, current_node = heappop(min_heap)

        if current_cost > node_data[current_node]['cost']:
            continue

        for neighbor, weight in graph[current_node].items():
            cost = current_cost + weight

            if cost < node_data[neighbor]['cost']:
                node_data[neighbor]['cost'] = cost
                node_data[neighbor]['pred'] = current_node
                heappush(min_heap, (cost, neighbor))

    # Reconstruct the shortest path
    shortest_path = []
    current_node = dest
    while current_node is not None:
        shortest_path.append(current_node)
        current_node = node_data[current_node]['pred']
    shortest_path.reverse()

    return node_data[dest]['cost'], shortest_path



