import pathlib
import sys

data = pathlib.Path(sys.argv[1]).read_text().splitlines()
print(data)
data = [list(filter(lambda x: x.isnumeric(), a)) for a in data]
print(sum([int(f'{x[0]}{x[-1]}') for x in data]))
