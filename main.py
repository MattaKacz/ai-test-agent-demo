from agent.analyzer import extract_functions
from agent.generator import generate_test
from agent.runner import run_tests
from pathlib import Path

def main():
    filepath = "example/views.py"
    functions = extract_functions(filepath)

    for name, code in functions:
        print(f"\n🔍 Function: {name}")
        print("➡ Generating test...")
        test_code = generate_test(code)

        test_path = Path(f"tests/test_{name}.py")
        test_path.write_text(test_code)
        print(f"✅ Saved: {test_path}")

    print("\n🏃 Running tests...")
    run_tests()

if __name__ == "__main__":
    main()
