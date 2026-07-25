import importlib
import pkgutil

# Automatically import all submodules in the current package directory
for _, module_name, _ in pkgutil.walk_packages(__path__):
    importlib.import_module(f"{__name__}.{module_name}")
