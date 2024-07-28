import importlib.util
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python script_runner.py <command>")
        return

    script_file = sys.argv[1]
    module_name = script_file.split(".")[0]  # Extract module name from filename
    print(script_file)

    try:
        spec = importlib.util.spec_from_file_location(module_name, script_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        module.main()  # Call the main function
    except (FileNotFoundError, AttributeError, ImportError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
