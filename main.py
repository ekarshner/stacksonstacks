from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
polygons = []
temp = new_matrix()
ident(temp)
cstack = [temp]

parse_file( 'script', edges, polygons, cstack, screen, color )
