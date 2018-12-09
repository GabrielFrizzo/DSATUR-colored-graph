import sys
import csv

graph = {}
file = open(sys.argv[1], 'r')
for row in csv.reader(file):
	graph[row[0]] = row[1:]
print(graph)
file.close()

