import time
import importlib.util
spec = importlib.util.spec_from_file_location("module.name", "main.py")
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)

foo.start()
foo.symmetry()

while True:
    print("Wow, multithreading is great !!!')
