import os

year = 2023
path = '/Users/piotrzak/Documents/GitHub/AOC/' + str(year)

folders = [x for x in range(1, 26)]
filenames = [str(x) + '.py' for x in range(1, 26)]
puzzles = [str(x) + '.txt' for x in range(1, 26)]

for i, folder in enumerate(folders):
    folder_path = os.path.join(path, str(folder))
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    with open(os.path.join(folder_path, filenames[i]), 'wb'):
        pass

    with open(os.path.join(folder_path, puzzles[i]), 'wb'):
        pass