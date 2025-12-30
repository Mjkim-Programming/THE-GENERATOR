import sys

def main():
    path = "./data/gen1.out"
    with open(path, "r", encoding="utf-8") as f:
        data = f.read()

    lines = data.splitlines()

    cnt = 0
    res = []
    for line in lines:
        if line:
            prev = ""
            for i in range(0, len(line)):
                if line[i] != prev:
                    res.append(cnt+1)
                    cnt = 0
                    print(line[i], end="")
                    prev = line[i]
                else:
                    cnt += 1
    print()
    print(*res, sep=",")

if __name__ == "__main__":
    main()
