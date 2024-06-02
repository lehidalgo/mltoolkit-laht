import argparse
import re


def get_current_version(file_path, pattern):
    with open(file_path, "r") as file:
        content = file.read()

    match = re.search(pattern, content)
    if match:
        return match.group(1)
    else:
        raise ValueError(f"Version pattern not found in {file_path}")


def update_version_in_script(file_path, old_version, new_version):
    with open(file_path, "r") as file:
        lines = file.readlines()

    with open(file_path, "w") as file:
        for line in lines:
            if line.strip().startswith("version="):
                line = line.replace(old_version, new_version)
            file.write(line)


def update_version_in_markdown(file_path, old_version, new_version):
    with open(file_path, "r") as file:
        lines = file.readlines()

    with open(file_path, "w") as file:
        for line in lines:
            if line.strip().startswith("# mltoolkit-laht"):
                line = line.replace(old_version, new_version)
            file.write(line)


def main():
    parser = argparse.ArgumentParser(description="Bump version in specified files.")
    parser.add_argument(
        "-set_version", type=str, required=True, help="The new version to set."
    )

    args = parser.parse_args()
    new_version = args.set_version

    script_path = "setup.py"
    markdown_path = "README.md"

    # Patterns to find the current version
    script_pattern = r'version="(\d+\.\d+\.\d+)"'
    markdown_pattern = r"# mltoolkit-laht (\d+\.\d+\.\d+)"

    # Get the current version from the script
    current_version_script = get_current_version(script_path, script_pattern)
    current_version_markdown = get_current_version(markdown_path, markdown_pattern)

    # Ensure versions in both files are the same before updating
    if current_version_script != current_version_markdown:
        raise ValueError("Version mismatch between script and markdown files.")

    # Update the version in both files
    update_version_in_script(script_path, current_version_script, new_version)
    update_version_in_markdown(markdown_path, current_version_markdown, new_version)

    print(
        f"Version updated from {current_version_script} to {new_version} in both files."
    )


if __name__ == "__main__":
    main()
