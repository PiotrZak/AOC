import os

year = 2023
path = 'C:/Users/pizak1/Desktop/AOC2022/AOC/' + str(year)

folders = [x for x in range(1, 26)]
filenames = [str(x) + '.py' for x in range(1, 26)]
puzzles = [str(x) + '.txt' for x in range(1, 26)]


for i, folder in enumerate(folders):
    os.mkdir(os.path.join(path, str(folder)))
    
    folder_path = os.path.join(path, str(folder))

    with open(os.path.join(folder_path, filenames[i]), 'wb') as temp_file:
        temp_file.write(b'')

    with open(os.path.join(folder_path, puzzles[i]), 'wb') as temp_file:
        temp_file.write(b'')