#include "Graph.h"

Graph::Graph(int V){
	vertives_count = V;
	edges_count = 0;
}

int Graph::V(){
	return vertives_count;
}

int Graph::E(){
	return edges_count;
}

void Graph::addEdge(int v, int w){
	edges_count += 1;
	edges.push_back(pair<int, int>(v, w));
}

vector<int> Graph::adj(int v){
	vector<int> res;
	for (auto pair : edges){
		if (pair.first == v)
			res.push_back(pair.second);
		if (pair.second == v)
			res.push_back(pair.first);
	}
	return res;
}

string Graph::toString(){
	string s =  to_string(vertives_count) + " vertices, " + to_string(edges_count) + " edges.\n";
	for (int v = 0; v < vertives_count; v++){
		s += to_string(v) + ": ";
		for (int w : this->adj(v))
			s += to_string(w) + " ";
		s += "\n";
	}
	return s;
}