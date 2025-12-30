import subprocess
import sys
import hashlib
from pathlib import Path

CPP_FILE = "index.cpp"
BIN_FILE = "./index"
DATA_DIR = Path("./data")

def compile_cpp():
    res = subprocess.run(
        ["g++", "-O2", "-std=c++17", CPP_FILE, "-o", BIN_FILE],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    if res.returncode != 0:
        print("컴파일 실패")
        print(res.stderr)
        sys.exit(1)

def run_program(i):
    res = subprocess.run(
        [BIN_FILE],
        input=(str(i) + "\n").encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    if res.returncode != 0:
        print("실행 중 에러")
        print(res.stderr.decode(errors="ignore"))
        sys.exit(1)
    return res.stdout

def load_answer(i):
    path = DATA_DIR / f"gen{i}.out"
    if not path.exists():
        print("정답 파일 없음:", path)
        sys.exit(1)
    return path.read_bytes()

def sha256(b):
    return hashlib.sha256(b).hexdigest()

def diff_output(expected, actual):
    if expected == actual:
        print("✅ 완벽 일치")
        return

    print("❌ 출력 불일치")

    print("expected size:", len(expected))
    print("actual   size:", len(actual))

    print("expected hash:", sha256(expected))
    print("actual   hash:", sha256(actual))

    limit = min(len(expected), len(actual))
    for i in range(limit):
        if expected[i] != actual[i]:
            print("❌ 최초 차이 위치:", i)
            print("expected:", expected[i:i+50])
            print("actual  :", actual[i:i+50])
            return

    print("❌ 한쪽이 더 김")

def main():
    if len(sys.argv) != 2:
        print("사용법: python checker.py <i>")
        sys.exit(1)

    i = int(sys.argv[1])
    if not (0 <= i <= 10):
        print("i는 0~10")
        sys.exit(1)

    compile_cpp()
    actual = run_program(i)
    expected = load_answer(i)
    diff_output(expected, actual)

if __name__ == "__main__":
    main()