#include <fstream>
#include <iostream>
#include <string>
#include <vector>

int main() {
    int count = 0;
    char person = '^';
    std::vector<std::vector<char>> map;
    std::string MyReadFileName = "input.txt";
    std::ifstream MyReadFile(MyReadFileName);
    std::string myText = "";

    while (std::getline(MyReadFile, myText)) {
        std::vector<char> row(myText.begin(), myText.end());
        map.push_back(row);
    }

    // Finding the starting position
    int x = -1, y = -1;
    for (int i = 0; i < map.size(); i++) {
        for (int j = 0; j < map[i].size(); j++) {
            if (map[i][j] == '^' or map[i][j] == '>' or map[i][j] == 'v' or map[i][j] == '<') {
                x = i;
                y = j;
                break;
            }
        }
        if (x != -1) break;
    }


    bool game_over = false;
    while (!game_over) {
        map[x][y] = 'x'; 

        if (person == '^') {
            if (x > 0 && map[x - 1][y] != '#') {
                x--;
            } else if (x == 0 || map[x - 1][y] == '#') {
                person = '>';
            }
        } else if (person == '>') {
            if (y < map[x].size() - 1 && map[x][y + 1] != '#') {
                y++;
            } else if (y == map[x].size() - 1 || map[x][y + 1] == '#') {
                person = 'v';
            }
        } else if (person == 'v') {
            if (x < map.size() - 1 && map[x + 1][y] != '#') {
                x++;
            } else if (x == map.size() - 1 || map[x + 1][y] == '#') {
                person = '<';
            }
        } else if (person == '<') {
            if (y > 0 && map[x][y - 1] != '#') {
                y--;
            } else if (y == 0 || map[x][y - 1] == '#') {
                person = '^';
            }
        }

        if ((person == '^' && x == 0) or (person == 'v' && x == map.size() - 1) or
            (person == '>' && y == map[x].size() - 1) or (person == '<' && y == 0)) {
            game_over = true;
        }
    }

    std::cout << "Resulting map:" << std::endl;
    for (const auto &row : map) {
        std::cout << "[ ";
        for (const auto &cell : row) {
            std::cout << cell << " ";
            if(cell == 'x'){
                count++;
            }
        }
        std::cout << "]" << std::endl;
    }

    std::cout<<"count is: "<<count + 1<<std::endl;

    
}
