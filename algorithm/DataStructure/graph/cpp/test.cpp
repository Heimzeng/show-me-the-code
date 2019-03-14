#include "Graph.cpp"
#include <iostream>
using namespace std;

int degree(Graph G, int v){
	int degree = 0;
	return G.adj(v).size();
}

int maxDegree(Graph G){
	int max = 0;
	for (int v = 0; v < G.V(); v++){
		int degreev = degree(G, v);
		if (degreev > max)
			max = degreev;
	}
	return max;
}

float avgDegree(Graph G){
	return 2.0 * G.E() / G.V();
}

int numberOfSelfLoops(Graph G){
	int count = 0;
	for (int v = 0; v < G.V(); v++)
		for (int w : G.adj(v))
			if (v == w)
				count ++;
	return count / 2;
}

int main(int argc, char const *argv[])
{
	Graph graph(10);
	graph.addEdge(1, 2);
	graph.addEdge(2, 3);
	graph.addEdge(2, 4);
	graph.addEdge(2, 2);
	int d1 = degree(graph, 1);
	cout << "d1: " << d1 << endl;
	int maxd = maxDegree(graph);
	cout << "maxd: " << maxd << endl;
	cout << "avgDegree: " << avgDegree(graph) << endl;
	cout << "selfLoops: " << numberOfSelfLoops(graph) << endl;
	cout << graph.toString();
	return 0;
}