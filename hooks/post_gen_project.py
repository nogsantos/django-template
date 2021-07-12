import os
from shutil import copyfile


def remove_heroku_files():
    file_names = ["Procfile", "heroku.yml"]
    for file_name in file_names:
        os.remove(file_name)


def remove_dottravisyml_file():
    os.remove(".travis.yml")


def remove_dotgitlatciyml_file():
    os.remove(".gitlab-ci.yml")


def remove_graphql_files():
    os.remove("core/schema.py")


def remove_nameko_files():
    file_names = ["core/sync.py", "config.yaml"]
    for file_name in file_names:
        os.remove(file_name)


def remove_open_source_files():
    file_names = ["CONTRIBUTORS.txt", "LICENSE"]
    for file_name in file_names:
        os.remove(file_name)


def copy_env_file():
    copyfile("contrib/.env.sample", "./.env")


def main():
    if "{{ cookiecutter.ci_tool }}".lower() != "travis":
        remove_dottravisyml_file()

    if "{{ cookiecutter.ci_tool }}".lower() != "gitlab":
        remove_dotgitlatciyml_file()

    if "{{ cookiecutter.use_heroku }}".lower() == "n":
        remove_heroku_files()

    if "{{ cookiecutter.use_graphql }}".lower() == "n":
        remove_graphql_files()

    if "{{ cookiecutter.use_nameko }}".lower() == "n":
        remove_nameko_files()

    if "{{ cookiecutter.open_source_license }}" == "Not open source":
        remove_open_source_files()

    copy_env_file()


if __name__ == "__main__":
    main()
