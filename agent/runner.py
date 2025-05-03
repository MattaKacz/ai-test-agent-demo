import subprocess
from pathlib import Path

def run_tests():
    result = subprocess.run(
        ["pytest", "--tb=short", "--maxfail=3", "tests/"],
        capture_output=True,
        text=True
    )
    print(result.stdout)
