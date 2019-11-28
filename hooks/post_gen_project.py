import os


def remove_graphql_files():
    if "{{ cookiecutter.use_graphql }}".lower() == "n":
        os.remove("core/schema.py")


def remove_nameko_files():
    if "{{ cookiecutter.use_nameko }}".lower() == "n":
        os.remove("core/sync.py")


def main():
    remove_graphql_files()
    remove_nameko_files()


if __name__ == "__main__":
    main()
