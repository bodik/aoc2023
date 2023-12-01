import pathlib
import sys


def firstlast(item):
    data = list(filter(lambda x: x.isnumeric(), item))
    return int(f"{data[0]}{data[-1]}")


trans = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

data = []

data1 = pathlib.Path(sys.argv[1]).read_text().splitlines()
# print(data1)

for item in data1:
    orig = item

    if nums := sorted(
        filter(lambda x: x[0] > -1, [(item.find(y), y) for y in trans.keys()])
    ):
        item = item.replace(nums[0][1], trans[nums[0][1]])

    if nums := sorted(
        filter(lambda x: x[0] > -1, [(item.rfind(y), y[::-1]) for y in trans.keys()])
    ):
        item = item[::-1].replace(nums[-1][1], trans[nums[-1][1][::-1]])[::-1]

    print(orig, "===", item, "===", firstlast(item))
    data.append(firstlast(item))

print(sum(data))
