import sys

def main():
    with open("./data/gen1.out", "r", encoding="utf-8") as f:
        data1 = f.read()
    with open("./res.out", "r", encoding="utf-8") as f:
        data2 = f.read()

    if len(data1) != len(data2):
        print("길이 불일치")
        exit(0)
    for v, i in enumerate(data1):
        if data1[i] != data2[i]:
            print(v)

if __name__ == "__main__":
    main()
