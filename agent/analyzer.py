import ast

def extract_functions(filepath):
    with open(filepath, "r") as f:
        tree = ast.parse(f.read())

    functions = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            source = ast.get_source_segment(open(filepath).read(), node)
            functions.append((node.name, source))
    return functions
