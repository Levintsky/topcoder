"""
Articulation Points (or Cut Vertices) in a Graph

A vertex in an undirected connected graph is an articulation point (or cut vertex) iff removing it (and edges through it) disconnects the graph. Articulation points represent vulnerabilities in a connected network – single points whose failure would split the network into 2 or more disconnected components. They are useful for designing reliable networks.
For a disconnected undirected graph, an articulation point is a vertex removing which increases number of connected components.

Following are some example graphs with articulation points encircled with red color.

How to find all articulation points in a given graph?
A simple approach is to one by one remove all vertices and see if removal of a vertex causes disconnected graph. Following are steps of simple approach for connected graph.

1) For every vertex v, do following
…..a) Remove v from graph
..…b) See if the graph remains connected (We can either use BFS or DFS)
…..c) Add v back to the graph

Time complexity of above method is O(V*(V+E)) for a graph represented using adjacency list. Can we do better?

A O(V+E) algorithm to find all Articulation Points (APs)
The idea is to use DFS (Depth First Search). In DFS, we follow vertices in tree form called DFS tree. In DFS tree, a vertex u is parent of another vertex v, if v is discovered by u (obviously v is an adjacent of u in graph). In DFS tree, a vertex u is articulation point if one of the following two conditions is true.
1) u is root of DFS tree and it has at least two children.
2) u is not root of DFS tree and it has a child v such that no vertex in subtree rooted with v has a back edge to one of the ancestors (in DFS tree) of u.

Following figure shows same points as above with one additional point that a leaf in DFS Tree can never be an articulation point.

We do DFS traversal of given graph with additional code to find out Articulation Points (APs). In DFS traversal, we maintain a parent[] array where parent[u] stores parent of vertex u. Among the above mentioned two cases, the first case is simple to detect. For every vertex, count children. If currently visited vertex u is root (parent[u] is NIL) and has more than two children, print it.
How to handle second case? The second case is trickier. We maintain an array disc[] to store discovery time of vertices. For every node u, we need to find out the earliest visited vertex (the vertex with minimum discovery time) that can be reached from subtree rooted with u. So we maintain an additional array low[] which is defined as follows.

low[u] = min(disc[u], disc[w]) 
where w is an ancestor of u and there is a back edge from 
some descendant of u to w.
Following are C++, Java and Python implementation of Tarjan’s algorithm for finding articulation points.
"""

# Python program to find articulation points in an undirected graph 

from collections import defaultdict 

#This class represents an undirected graph 
#using adjacency list representation 
class Graph: 

	def __init__(self,vertices): 
		self.V= vertices #No. of vertices 
		self.graph = defaultdict(list) # default dictionary to store graph 
		self.Time = 0

	# function to add an edge to graph 
	def addEdge(self,u,v): 
		self.graph[u].append(v) 
		self.graph[v].append(u) 

	'''A recursive function that find articulation points 
	using DFS traversal 
	u --> The vertex to be visited next 
	visited[] --> keeps tract of visited vertices 
	disc[] --> Stores discovery times of visited vertices 
	parent[] --> Stores parent vertices in DFS tree 
	ap[] --> Store articulation points'''
	def APUtil(self,u, visited, ap, parent, low, disc): 

		#Count of children in current node 
		children =0

		# Mark the current node as visited and print it 
		visited[u]= True

		# Initialize discovery time and low value 
		disc[u] = self.Time 
		low[u] = self.Time 
		self.Time += 1

		#Recur for all the vertices adjacent to this vertex 
		for v in self.graph[u]: 
			# If v is not visited yet, then make it a child of u 
			# in DFS tree and recur for it 
			if visited[v] == False : 
				parent[v] = u 
				children += 1
				self.APUtil(v, visited, ap, parent, low, disc) 

				# Check if the subtree rooted with v has a connection to 
				# one of the ancestors of u 
				low[u] = min(low[u], low[v]) 

				# u is an articulation point in following cases 
				# (1) u is root of DFS tree and has two or more chilren. 
				if parent[u] == -1 and children > 1: 
					ap[u] = True

				#(2) If u is not root and low value of one of its child is more 
				# than discovery value of u. 
				if parent[u] != -1 and low[v] >= disc[u]: 
					ap[u] = True	
					
				# Update low value of u for parent function calls	 
			elif v != parent[u]: 
				low[u] = min(low[u], disc[v]) 


	#The function to do DFS traversal. It uses recursive APUtil() 
	def AP(self): 

		# Mark all the vertices as not visited 
		# and Initialize parent and visited, 
		# and ap(articulation point) arrays 
		visited = [False] * (self.V) 
		disc = [float("Inf")] * (self.V) 
		low = [float("Inf")] * (self.V) 
		parent = [-1] * (self.V) 
		ap = [False] * (self.V) #To store articulation points 

		# Call the recursive helper function 
		# to find articulation points 
		# in DFS tree rooted with vertex 'i' 
		for i in range(self.V): 
			if visited[i] == False: 
				self.APUtil(i, visited, ap, parent, low, disc) 

		for index, value in enumerate (ap): 
			if value == True:
				print(index)

# Create a graph given in the above diagram 
g1 = Graph(5) 
g1.addEdge(1, 0) 
g1.addEdge(0, 2) 
g1.addEdge(2, 1) 
g1.addEdge(0, 3) 
g1.addEdge(3, 4) 

print("\nArticulation points in first graph ")
g1.AP() 

g2 = Graph(4) 
g2.addEdge(0, 1) 
g2.addEdge(1, 2) 
g2.addEdge(2, 3) 
print("\nArticulation points in second graph ")
g2.AP() 


g3 = Graph (7) 
g3.addEdge(0, 1) 
g3.addEdge(1, 2) 
g3.addEdge(2, 0) 
g3.addEdge(1, 3) 
g3.addEdge(1, 4) 
g3.addEdge(1, 6) 
g3.addEdge(3, 5) 
g3.addEdge(4, 5) 
print("\nArticulation points in third graph ")
g3.AP() 

#This code is contributed by Neelam Yadav 
