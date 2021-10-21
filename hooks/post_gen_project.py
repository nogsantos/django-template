import os
import shutil


def remove_heroku_files():
    __remove_files(["Procfile", "heroku.yml"])


def remove_dottravisyml_file():
    os.remove(".travis.yml")


def remove_dotgitlatciyml_file():
    os.remove(".gitlab-ci.yml")


def remove_graphql_files():
    os.remove("core/schema.py")


def remove_nameko_files():
    __remove_files(["config.yaml"])
    shutil.rmtree("services")


def remove_scheduler_files():
    os.remove("config/scheduler.py")


def remove_open_source_files():
    __remove_files(["CONTRIBUTORS.txt", "LICENSE"])


def copy_env_file():
    shutil.copyfile("contrib/.env.sample", "./.env")


def __remove_files(files_name):
    for file_name in files_name:
        os.remove(file_name)


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

    if "{{ cookiecutter.use_scheduler }}".lower() == "n":
        remove_scheduler_files()

    if "{{ cookiecutter.open_source_license }}" == "Not open source":
        remove_open_source_files()

    copy_env_file()


if __name__ == "__main__":
    main()
