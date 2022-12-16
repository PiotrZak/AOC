from collections import defaultdict

MAX_SIZE = 100_000
DISK_SPACE = 70_000_000
THRESHOLD = 30_000_000

with open("7.txt") as f:
    commands = f.readlines()

dir_path = []
dir_sizes = defaultdict(int)
for c in commands:
    c = c.strip().split()
    match c:
        case ["$", "cd", ".."]:
            dir_path.pop()
        case ["$", "cd", dir]:
            ext = f"/{dir if dir != '/' else ''}"
            dir_path.append("/".join(dir_path) + ext)
        case [size_str, _] if "$" != size_str != "dir":
            for dir in dir_path:
                dir_sizes[dir] += int(size_str)

total = sum([size for size in dir_sizes.values() if size <= MAX_SIZE])
print(total)

remaining = THRESHOLD - (DISK_SPACE - dir_sizes["/"])
best = min([size for size in dir_sizes.values() if size >= remaining])
print(best)