import importlib.util
from pathlib import Path

module_path = Path(__file__).with_name("08_15_printing_models.py")
spec = importlib.util.spec_from_file_location("printing_models", module_path)
printing_functions = importlib.util.module_from_spec(spec)
spec.loader.exec_module(printing_functions)

unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]

completed_models = []

printing_functions.print_models(
    unprinted_designs, completed_models
)

printing_functions.show_completed_models(completed_models)