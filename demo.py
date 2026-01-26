import sys
from typing import List


class Demo:
    """
    Lightweight demo class that simulates a tiny build pipeline.
    Everything runs in milliseconds but still behaves like real steps.
    """

    def hello(self, name: str = "Devfile") -> None:
        greeting = f"Hello {name}"
        print(greeting)

    def build(self) -> None:
        """
        Simulate a build by producing a deterministic artifact value.
        """
        sources = ["core", "utils", "api"]
        artifact = "-".join(sources).upper()
        print(f"Build artifact: {artifact}")

    def test(self) -> None:
        """
        Simulate tests by validating a known invariant.
        """
        expected = 6
        actual = sum([1, 2, 3])
        if actual != expected:
            print("Tests failed")
            sys.exit(1)
        print("Tests passed")

    def lint(self) -> None:
        """
        Simulate linting by checking naming conventions.
        """
        names = ["build", "test", "lint", "hello"]
        invalid = [n for n in names if not n.islower()]
        if invalid:
            print(f"Lint failed: {invalid}")
            sys.exit(1)
        print("Lint clean")

    def multiline(self) -> None:
        """
        Entry point for testing shell line continuation.
        """
        print("Multiline execution OK")

    def semicolon(self) -> None:
        """
        Small step useful for semicolon chaining.
        """
        print("Semicolon step OK")

    def pipe(self) -> None:
        """
        Output structured text so pipes can do real filtering.
        """
        records = [
            "service=python status=ok",
            "service=node status=ok",
            "service=python status=warn",
        ]
        for r in records:
            print(r)

    def or_fail(self) -> None:
        """
        Fail deterministically for || demo.
        """
        print("Simulated failure")
        sys.exit(1)

    def windows_backslash(self) -> None:
        """
        Target for Windows-style \\ normalization demo.
        """
        print("Windows backslash normalization OK")


def main(argv: List[str]) -> None:
    demo = Demo()

    if len(argv) < 2:
        print("Usage: python demo.py <action> [args]")
        sys.exit(1)

    action = argv[1]
    args = argv[2:]

    if not hasattr(demo, action):
        print(f"Unknown action: {action}")
        sys.exit(1)

    method = getattr(demo, action)
    method(*args)


if __name__ == "__main__":
    main(sys.argv)
