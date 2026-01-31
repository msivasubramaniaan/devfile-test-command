import os
import sys
import json
from pathlib import Path

DATA = Path("data.json")


class Demo:
    """
    Minimal but real functionality:
      - generate    → create real data
      - validate    → validate data, can fail
      - transform   → mutate data
      - status      → show current state
      - pipe        → structured output for | grep | wc
      - fail        → controlled failure for ||
      - windows_backslash → verify \\ normalization
      - argv        → show how multiline (\ and \\) are joined
    """

    def generate(self):
        payload = {
            "service": "python",
            "version": 1,
            "status": "ok"
        }
        DATA.write_text(json.dumps(payload, indent=2))
        print("Data generated")

    def validate(self):
        if not DATA.exists():
            print("No data to validate")
            sys.exit(1)

        data = json.loads(DATA.read_text())
        if data.get("status") != "ok":
            print("Validation failed")
            sys.exit(1)

        print("Validation passed")

    def transform(self):
        if not DATA.exists():
            print("No data to transform")
            sys.exit(1)

        data = json.loads(DATA.read_text())
        data["transformed"] = True
        DATA.write_text(json.dumps(data, indent=2))
        print("Data transformed")

    def status(self):
        if DATA.exists():
            print(DATA.read_text())
        else:
            print("No data available")

    def pipe(self):
        print("service=python status=ok")
        print("service=node status=warn")
        print("service=python status=error")

    def fail(self):
        print("Intentional failure")
        sys.exit(1)

    def windows_backslash(self):
        print("Windows-style backslash normalization works")

    def argv(self):
        print("ARGV:", sys.argv[1:])
    
    def component_signal(self):
    
        if not self.component:
            print("ERROR: component_signal requires --component <name>")
            sys.exit(1)

        import time

        start_ts = time.time()
        print(f"[component_signal][START] component={self.component}")

        # Small delay to expose parallel behavior without flakiness
        time.sleep(1)

        payload = {
            "component": self.component,
            "start": start_ts,
            "end": time.time(),
            "pid": os.getpid(),
            "cwd": os.getcwd(),
        }

        out = Path(f"component-signal.{self.component}.json")
        out.write_text(json.dumps(payload, indent=2))

        print(f"[component_signal][END] component={self.component}")
        print(f"[component_signal] wrote {out.name}")




def main():
    demo = Demo()

    if len(sys.argv) < 2:
        print("Usage: python demo.py <command>")
        sys.exit(1)

    cmd = sys.argv[1]
    if not hasattr(demo, cmd):
        print(f"Unknown command: {cmd}")
        sys.exit(1)

    getattr(demo, cmd)()


if __name__ == "__main__":
    main()
