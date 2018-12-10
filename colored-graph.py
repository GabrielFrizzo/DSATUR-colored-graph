import sys
import csv

class Node:
	def __init__(self, key):
		self.key = key
		self.nbhood = []
		self.color = None

	def add_edge(self, node):
		self.nbhood.append(node)

	def deg(self):
		return len(self.nbhood)

	def deg_sat(self):
		return sum(node.color is not None for node in self.nbhood)

	def colorize_node(self):
		self.color = self.best_color()
		best_node = self.best_node()
		while best_node is not None:
			best_node.colorize_node()
			best_node = self.best_node()

	def best_node(self):
		sat_degrees = {}
		degrees = {}
		for node in self.nbhood:
			if node.color is None:
				sat_degrees[node] = node.deg_sat()
				degrees[node] = node.deg()

		if len(sat_degrees):
			best_sat_degree = max(sat_degrees.values())
			best_sat_degrees = { node: sat_degree for node, sat_degree in degrees.items() if sat_degrees[node] == best_sat_degree }

			return max(best_sat_degrees, key = best_sat_degrees.get)

	def best_color(self):
		best = 0
		for node in self.nbhood:
			if node.color == best:
				best += 1
		return best

	def __str__(self):
		return self.key + ': ' + ', '.join([node.key for node in self.nbhood])

class Graph:
	def __init__(self, graph_dict={}):
		self.node_dict = {}
		for key in graph_dict:
			self.node_dict[key] = Node(key)
		for key, node in self.node_dict.items():
			for adj in graph_dict[key]:
				node.add_edge(self.node_dict[adj])


	def nodes(self):
		return self.node_dict.values()

	def colorize_graph(self):
		first = max(self.nodes(), key = lambda node: node.deg())
		first.colorize_node()

def main(argv):
	graph_dict = {}
	file = open(sys.argv[1], 'r')
	for row in csv.reader(file):
		graph_dict[row[0]] = [col[1:] for col in row[1:]]
	file.close()

	graph = Graph(graph_dict)
	graph.colorize_graph()

	for node in graph.nodes():
		print(node.color)


if __name__ == '__main__':
	main(sys.argv)