from itertools import product, permutations
import heapq
class Tile():
    def __init__(self,cords:[int],speed) -> None:
        self.cords = cords 
        self.speed = speed

class Graph():
    def __init__(self,matrix) -> None:
        self.matrix = matrix
        self.tiles = [] #cords -> Tile
        self.edges = {} #cords -> list
        self.fill()
        
    def change_matrix(self):
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[y])):
                if self.matrix[y][x] != -1:
                    self.matrix[y][x] = 1 - 0.25*self.matrix[y][x]
                
    def fill(self):
        d_main = list(product([1,0,-1], repeat=2))
        a = 0
        b = 0
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[y])):
                self.tiles.append((x,y))
                self.edges[(x,y)] = []
                for d in d_main:
                    if d != (0,0):
                        if x + d[0] > -1 and x + d[0] < len(self.matrix) and y + d[1] > -1 and y + d[1] < len(self.matrix):
                            if  self.matrix[y+d[1]][x+d[0]] != -1 and self.matrix[y][x] != -1:
                                self.edges[(x,y)].append((x+d[0], y+d[1]))

                                              
    def guml_path(self,start,end,mode):
        speed = 1
        dist_const = 10
        time = {index:float("inf") for index in self.tiles}
        route = route = {index:None for index in self.tiles}#point->point
        points = [(0,start)]
        if start[0] > -1 and start[1] > -1 and start[0] < len(self.matrix) and start[1] < len(self.matrix) and end[0] > -1 and end[0] < len(self.matrix) and end[1] > -1 and end[1] < len(self.matrix):
            current_point = start
            
            while points and current_point != end:
                current_time, current_index = heapq.heappop(points)

                if current_time > time[current_index]:
                    continue
                for neighbor in self.edges[(current_index)]:
                    if neighbor[1] == current_index[1] or neighbor[0] == current_index[0]:
                        new_time = dist_const/(speed/((self.matrix[current_index[1]][current_index[0]] + self.matrix[neighbor[1]][neighbor[0]])/2))
                    else:
                        new_time = dist_const/(speed/((1.4*(self.matrix[current_index[1]][current_index[0]] + self.matrix[neighbor[1]][neighbor[0]]))/2))
                    if new_time < time[neighbor]:
                        time[neighbor] = new_time
                        route[neighbor] = current_index
                        heapq.heappush(points,(new_time,neighbor))
            if mode == 0:
                print(time[start])
                return time[start]
            else:
                print(time[start])
                path = self.__get_path(start,end,route)
                print(path)
                return time[start], path
    
    def __get_path(self,start,end,route):
        main_list=[]
        current = end
        while current != start:
            main_list.append(current)
            current = route[current]             
        main_list.append(start)
        return list(reversed(main_list))
        
        

matrix = [
[1, 2],
[-1, 1]
]

gr = Graph(matrix)
gr.guml_path((0,0),(1,1),1)

