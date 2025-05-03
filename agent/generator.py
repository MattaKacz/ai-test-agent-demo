import subprocess

def generate_test(function_code: str) -> str:
    prompt = f"""
Generate a pytest unit test for the following Django function:

{function_code}

Requirements:
- Use pytest
- Mock the request if necessary
- Include comments using '#' syntax
- Return only valid Python code without any explanations, headers, or markdown formatting
"""

    result = subprocess.run(
        ["ollama", "run", "llama3", prompt],
        capture_output=True,
        text=True
    )

    return clean_code_output(result.stdout.strip())

def clean_code_output(output: str) -> str:
    lines = output.strip().splitlines()
    clean_lines = []
    for line in lines:
        stripped = line.strip()
        # Skip markdown code block indicators
        if stripped.startswith("```"):
            continue
        # Skip lines that are plain text explanations
        if not stripped or not (
            stripped.startswith("def ") or
            stripped.startswith("class ") or
            stripped.startswith("import ") or
            stripped.startswith("from ") or
            stripped.startswith("#") or
            stripped.startswith("@") or
            stripped.startswith("assert ") or
            stripped.startswith("return ") or
            stripped.startswith("with ") or
            stripped.startswith("for ") or
            stripped.startswith("if ") or
            stripped.startswith("elif ") or
            stripped.startswith("else:") or
            stripped.startswith("try:") or
            stripped.startswith("except ") or
            stripped.startswith("finally:")
        ):
            continue
        clean_lines.append(line)
    return "\n".join(clean_lines)
