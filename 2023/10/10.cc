#include <iostream>
#include <fstream>
#include <vector>
#include <utility>

// Solution based on: https://github.com/kurucsaiandras/advent-of-code/blob/main/Day-10/part1.cpp
// c++ is imperative, not functional

enum class Direction { LEFT, UP, RIGHT, DOWN };

const int MAZE_SIZE = 21;

std::vector<std::string> maze;

std::pair<int, int> findStart() {
    for (int row = 0; row < maze.size(); row++) {
        for (int col = 0; col < maze[row].size(); col++) {
            if (maze[row][col] == 'S') return {row, col};
        }
    }
    return {0, 0};
}

Direction getDirection(char symbol) {
    switch (symbol) {
        case 'L': return Direction::LEFT;
        case 'F': return Direction::UP;
        case '7': return Direction::RIGHT;
        case 'J': return Direction::DOWN;
        case '|': return Direction::UP; // Choose appropriate direction for '|'
        case '-': return Direction::RIGHT; // Choose appropriate direction for '-'
        default: throw std::runtime_error("Invalid symbol");
    }
}

std::pair<int, int> stepTo(int prevRow, int prevCol, int currRow, int currCol, Direction direction) {
    switch (direction) {
        case Direction::LEFT:
            return (maze[currRow][currCol] == '-') ? std::make_pair(currRow, currCol - 1) : std::make_pair(currRow - 1, currCol);
        case Direction::UP:
            return (maze[currRow][currCol] == '|') ? std::make_pair(currRow - 1, currCol) : std::make_pair(currRow, currCol + 1);
        case Direction::RIGHT:
            return (maze[currRow][currCol] == '-') ? std::make_pair(currRow, currCol + 1) : std::make_pair(currRow + 1, currCol);
        case Direction::DOWN:
            return (maze[currRow][currCol] == '|') ? std::make_pair(currRow + 1, currCol) : std::make_pair(currRow, currCol - 1);
        default:
            throw std::runtime_error("Invalid direction");
    }
}

int main() {
    std::ifstream file("10.txt");
    if (!file.is_open()) {
        std::cout << "Can't open file!" << std::endl;
        return 0;
    }

    std::string line;
    while (std::getline(file, line)) {
        maze.push_back(line);
    }

    std::pair<int, int> start = findStart();
    std::pair<int, int> dir1Pos = {start.first - 1, start.second};
    std::pair<int, int> dir2Pos = {start.first, start.second + 1};
    int step = 1;

    while (dir1Pos != dir2Pos) {
        std::pair<int, int> prevDir1 = dir1Pos;
        std::pair<int, int> prevDir2 = dir2Pos;

        Direction dir1 = getDirection(maze[dir1Pos.first][dir1Pos.second]);
        Direction dir2 = getDirection(maze[dir2Pos.first][dir2Pos.second]);

        dir1Pos = stepTo(prevDir1.first, prevDir1.second, dir1Pos.first, dir1Pos.second, dir1);
        dir2Pos = stepTo(prevDir2.first, prevDir2.second, dir2Pos.first, dir2Pos.second, dir2);

        step++;
    }

    std::cout << "Steps: " << step << std::endl;

    return 0;
}
