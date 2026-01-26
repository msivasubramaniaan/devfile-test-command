import sys
import os
import time

class Demo:

    # 1. Real “app”
    def hello(self, name="Devfile"):
        print(f"Hello {name}, from Python Devfile playground!!!")

    # 2. Real “build” (simulate compilation)
    def build(self):
        print("Building project...")
        with open("build.log", "w") as f:
            f.write("Build successful\n")
        print("build.log generated")

    # 3. Real “test” (checks build output)
    def test(self):
        print("Running tests...")
        if not os.path.exists("build.log"):
            print("Tests failed: build.log not found")
            sys.exit(1)
        print("All tests passed")

    # 4. Real “lint” (simple code quality check)
    def lint(self):
        print("Linting code...")
        with open(__file__, "r") as f:
            lines = f.readlines()
        long_lines = [i+1 for i, l in enumerate(lines) if len(l) > 120]
        if long_lines:
            print(f"Lint warning: long lines at {long_lines}")
        else:
            print("Lint passed")

    # 5. Used for multiline "\" demo
    def multiline(self):
        print("Multiline execution succeeded")

    # 6. Used for semicolon demo
    def semicolon(self):
        ts = time.strftime("%H:%M:%S")
        print(f"Semicolon step executed at {ts}")

    # 7. Used for pipe demo
    def pipe(self):
        # Output is meaningful for grep/wc
        print("python devfile demo example")

    # 8. Used for OR operator demo
    def or_fail(self):
        print("Intentional failure triggered")
        sys.exit(1)

    # 9. Windows backslash demo
    def windows_backslash(self):
        print("Windows-style \\\\ backslash normalization worked")

    # 10. Small file generation (useful for chaining)
    def generate_file(self):
        with open("demo.txt", "w") as f:
            f.write("Devfile demo file\n")
        print("demo.txt created")

    # 11. Read file (useful for pipelines)
    def read_file(self):
        if not os.path.exists("demo.txt"):
            print("demo.txt not found")
            sys.exit(1)
        with open("demo.txt") as f:
            print(f.read().strip())


if __name__ == "__main__":
    demo = Demo()

    if len(sys.argv) < 2:
        print("Usage: python demo.py <method> [args]")
        sys.exit(1)

    method = sys.argv[1]
    args = sys.argv[2:]

    if not hasattr(demo, method):
        print(f"Unknown method: {method}")
        sys.exit(1)

    getattr(demo, method)(*args)
