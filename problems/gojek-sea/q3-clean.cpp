#include<iostream>
#include<string>
#include<vector>
#include<set>
#include<map>

using namespace std;

// This algorithm use Depth First Search

bool isNeighborExist(vector<string> &maps, int x, int y) {
	if ((y >= 0 && y < maps.size()) && (x >= 0 && x < maps[0].size()) && maps[y][x] != '#') return true;
	return false;
}

void doDFS(vector<string> &maps, int x, int y, vector<vector<bool>> &visited, vector<set<char>> &factions, set<char> &f) {
	if (visited[y][x]) {
		return;
	}

	if (maps[y][x] != '.') f.insert(maps[y][x]);
	visited[y][x] = true;
	//@debug cout << "Traversed " << x << " " << y << endl;

	//4 Checks up(0,-1) down(0,1) right (1,0) left (-1,0)

	if (isNeighborExist(maps, x, y - 1)) doDFS(maps, x, y - 1, visited, factions, f); // Up
	if (isNeighborExist(maps, x, y + 1)) doDFS(maps, x, y + 1, visited, factions, f); // Down
	if (isNeighborExist(maps, x + 1, y)) doDFS(maps, x + 1, y, visited, factions, f); // Right
	if (isNeighborExist(maps, x - 1, y)) doDFS(maps, x - 1, y, visited, factions, f); // Left
}

int main() {
	int T;
	cin >> T;
	for (int w = 1; w <= T; w++) {
		int N, M;
		cin >> N >> M;

		//Generate the grids
		vector<string> grids(N);
		string input;
		for (int i = 0; i < N; i++) {
			cin >> input;
			grids[i] = input;
		}

		//Generate visited grids
		vector<vector<bool>> visited(N, vector<bool>(M));

		//int count = 0; //count the region for debug
		vector<set<char>> factions; //faction available in a certain region

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (grids[i][j] != '#' && !visited[i][j]) {
					//@debug cout << "Clust " << j << " " << i << endl;
					set<char> f = {};
					//count++;
					doDFS(grids, j, i, visited, factions, f);
					factions.push_back(f);
				}
			}
		}

		//Mapping the factions
		map<char, int> ctrlScore; //controlled faction score
		int K = 0; //contested function

		for (set<char> faction : factions) {
			if (faction.size() == 1) {
				auto itr = faction.begin();
				ctrlScore[*itr] += 1;
			}
			else if (faction.size() > 1) {
				K++;
			}
		}

		//OUTPUT
		cout << "Case " << w << ":" << "\n";
		for (auto i = ctrlScore.begin(); i != ctrlScore.end(); i++) {
			cout << i->first << " " << i->second << "\n";
		}
		cout << "contested " << K << "\n";
	}
	return 0;
}