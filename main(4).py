import heapq
from collections import deque

class City():
    def __init__(self,index:str,name:str) -> None:
        self.name = name
        self.index = index

    def __str__(self) -> str:
        return f"City {self.index} {self.name}"
    
    
class Graph:
    def __init__(self) -> None:
        self.cities = {} #index -> Город
        self.edges = {} #город -> список [(город,вес)]
    def add_city(self, index, name):
        if index not in self.cities:
            city = City(index,name)
            self.cities[index] = city
            self.edges[city] = []
    
    def add_edge(self,index_z,index_v,weight):
        city_z = self.cities.get(index_z)
        city_v = self.cities.get(index_v)
        if not city_v or not city_z:
            print("error")
            return
        if city_v is city_z:
            self.edges[city_v].append((city_z,weight))
            return
        self.edges[city_v].append((city_z, weight))
        self.edges[city_z].append((city_v, weight))
    
    def __str__(self) -> str:
        main_str = ""
        for city,gumlers in self.edges.items():
            main_str += city.name + " | "  + " , ".join([f"{str(c.name)} {str(w)}" for c, w in gumlers])
            main_str += "\n"
        return main_str
    
    def dijkstra(self,start, end):
        distance = {index:float('inf') for index in self.cities}
        distance[start] = 0
        route = {index:None for index in self.cities}
        points = [(0,start)]
        current_point = start
        while points and end != current_point:
            current_dist, current_index = heapq.heappop(points)
            city = self.cities[current_index]
            if current_dist > distance[current_index]:
                continue
            for neighbor, weight in self.edges[city]:
                new_dist = current_dist + weight
                if new_dist < distance[neighbor.index]:
                    distance[neighbor.index] = new_dist
                    route[neighbor.index] = current_index
                    heapq.heappush(points,(new_dist,neighbor.index))
        return distance, route
    
    @staticmethod
    def reguml_path(route, start, end):
        path = []
        current = end
        while start != current:
            path.append(current)
            current = route.get(current,None)
        if current is None:
            return None
        path.append(start)
        path = list(reversed(path))
        return path



tst = Graph()

tst.add_city(1,"Урюпинск")
tst.add_city(2,"Гумлерск")
tst.add_city(3,"Фрязино")
tst.add_city(4,"Подольск")
tst.add_city(5,"Балабаново")
tst.add_city(6,"гусь-хрустальный")
tst.add_edge(1,2,92)
tst.add_edge(2,3,15)
tst.add_edge(3,4,32)
tst.add_edge(4,5,100)
tst.add_edge(5,6,14)
tst.add_edge(6,1,8)
tst.add_edge(2,5,2)
path = [2,6]
print(tst.reguml_path(tst.dijkstra(*path)[1], *path))
print(tst)

