#include <algorithm>
#include <chrono>
#include <fstream>
#include <iostream>
#include <iterator>
#include <numeric>
#include <sstream>
#include <vector>
#include <iostream>
#include <string>
#include <map>


std::vector<std::pair<std::pair<size_t, size_t>, std::pair<size_t, size_t>>> generateGalaxyPairs(const std::map<std::pair<size_t, size_t>, char>& galaxies) {
    std::vector<std::pair<std::pair<size_t, size_t>, std::pair<size_t, size_t>>> galaxyPairs;

    for (auto it1 = galaxies.begin(); it1 != std::prev(galaxies.end()); ++it1) {
        for (auto it2 = std::next(it1); it2 != galaxies.end(); ++it2) {
            galaxyPairs.emplace_back(it1->first, it2->first);
        }
    }

    return galaxyPairs;
}
int main()
{
    
    std::string input = R"(...#......
                        .......#..
                        #.........
                        ..........
                        ......#...
                        .#........
                        .........#
                        ..........
                        .......#..
                        #...#.....)";
    
    
    // Remove empty spaces from the string
    input.erase(std::remove_if(input.begin(), input.end(), ::isspace), input.end());
    size_t width = input.find_first_of("\n") - 1;  // Assuming all lines have the same width
    
    std::map<std::pair<size_t, size_t>, char> galaxies;
    
    
        for (size_t i = 0; i < input.length(); ++i) {

        size_t row = i / (width + 1);  // Calculate row number
        size_t col = i % (width + 1);  // Calculate column number
        std::cout << "Row: " << row << ", Col: " << col << ", Char: " << input[i] << std::endl;
        
        if (input[i] == '#') {
            galaxies.insert(std::make_pair(std::make_pair(row, col), input[i]));
        }
        
    }
    
    for (const auto& entry : galaxies) {
        std::cout << "Galaxy at Row: " << entry.first.first << ", Col: " << entry.first.second << std::endl;
    }
    
    // Generate pairs for every galaxy
    std::vector<std::pair<std::pair<size_t, size_t>, std::pair<size_t, size_t>>> galaxyPairs = generateGalaxyPairs(galaxies);

    // Print the generated pairs
    for (const auto& pair : galaxyPairs) {
        std::cout << "Pair 1: (" << pair.first.first << ", " << pair.first.second << ") - Pair 2: (" << pair.second.first << ", " << pair.second.second << ")" << std::endl;
    }

    return 0;

}



