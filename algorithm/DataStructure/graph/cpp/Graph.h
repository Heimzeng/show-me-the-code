#include <vector>
#include <string>
using namespace std;
class Graph
{
public:
	Graph(int V);
	int V();
	int E();
	void addEdge(int v, int w);
	vector<int> adj(int v);
	string toString();
private:
	int vertives_count;
	int edges_count;
	vector<pair<int, int>> edges; 
};
