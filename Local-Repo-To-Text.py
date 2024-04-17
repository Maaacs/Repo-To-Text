import os
import sys

def build_directory_tree(path, indent=0, file_paths=[]):
    tree_str = ""
    for item in sorted(os.listdir(path)):
        if (item == 'node_modules' or item == 'package-lock.json' or item == 'main.css' 
        or item == 'access.log' or item == '.next' or item == '.git' or item == 'tsconfig.tsbuildinfo'
        or item== '.next' or item== 'build'):
            continue

        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            tree_str += '    ' * indent + f"[{item}/]\n"
            tree_str += build_directory_tree(item_path, indent + 1, file_paths)[0]
        else:
            tree_str += '    ' * indent + f"{item}\n"
            file_paths.append((indent, item_path))
    return tree_str, file_paths



def retrieve_local_repo_info(path):
    directory_tree, file_paths = build_directory_tree(path)

    formatted_string = f"Directory Structure:\n{directory_tree}\n"

    for indent, file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()
                formatted_string += '\n' + '    ' * indent + f"{file_path}:\n" + '    ' * indent + '```\n' + file_content + '\n' + '    ' * indent + '```\n'
        except Exception as e:
            formatted_string += '\n' + '    ' * indent + f"{file_path}: Error reading file\n"

    return formatted_string

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 localrepoText.py path-to-repo")
    else:
        repo_path = sys.argv[1]
        output_file_name = "local-repo-formatted.txt"

        formatted_repo_info = retrieve_local_repo_info(repo_path)
        with open(output_file_name, 'w', encoding='utf-8') as file:
            file.write(formatted_repo_info)

        print(f"Repository information has been saved to {output_file_name}")
