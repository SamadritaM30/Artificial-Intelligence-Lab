#include<bits/stdc++.h>
using namespace std;

struct State {
    vector<int> tiles;
    vector<vector<int>> path;
};

vector<vector<int>> bfsSlidingPuzzle(vector<int> initialState, vector<int> goalState) {
    queue<State> q;
    set<vector<int>> visited;
    
    q.push({initialState, {initialState}});
    visited.insert(initialState);
    
    while (!q.empty()) {
        State current = q.front();
        q.pop();
        
        if (current.tiles == goalState) {
            return current.path;
        }
        
        int zeroIndex = find(current.tiles.begin(), current.tiles.end(), 0) - current.tiles.begin();
        
        vector<pair<int, int>> moves = {{-1, 0}, {1, 0}}; // Left and Right moves
        
        for (auto move : moves) {
            int newIndex = zeroIndex + move.first;
            if (newIndex >= 0 && newIndex < 3) {
                vector<int> newTiles = current.tiles;
                swap(newTiles[zeroIndex], newTiles[newIndex]);
                
                if (visited.find(newTiles) == visited.end()) {
                    vector<vector<int>> newPath = current.path;
                    newPath.push_back(newTiles);
                    q.push({newTiles, newPath});
                    visited.insert(newTiles);
                }
            }
        }
    }
    return {};
}

int main() {
    vector<int> initialState = {2, 1, 0};
    vector<int> goalState = {1, 2, 0};
    
    vector<vector<int>> solution = bfsSlidingPuzzle(initialState, goalState);
    
    if (!solution.empty()) {
        cout << "Solution found:" << endl;
        for (const auto& step : solution) {
            for (int num : step) {
                cout << num << " ";
            }
            cout << endl;
        }
    } else {
        cout << "No solution found." << endl;
    }
    return 0;
}
