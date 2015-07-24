from cfg import WORKSPACE_PATH, RESOURCES_PATH
import os
from manager import Manager


manager = Manager()


@manager.command
def create_flask_web_project(project_name):
    """
    This will create a flask project named <project_name>-web in the workspace.

    Comes with
    - requirements
    - virtualenv
    - .gitignore
    - folder structure
    - js/css/media files
        - bootstrap
        - jquery
        - main.coffee
        - main.sass
    - WATCHER.sh (coffeescript/shpaml)
    - run.py
    - initial git commit
    """
    folder_name = "%s-web" % (project_name)
    project_path = os.path.join(WORKSPACE_PATH, folder_name)
    project_module_path = os.path.join(project_path, project_name)
    template_run_py_path = os.path.join(RESOURCES_PATH, "run.py")
    template_app_py_path = os.path.join(RESOURCES_PATH, "app.py")
    template_web_py_path = os.path.join(RESOURCES_PATH, "web.py")
    destination_run_py_path = os.path.join(project_path, "run.py")
    destination_web_py_path = os.path.join(project_module_path, "web.py")
    destination_watcher_path = os.path.join(project_path, "WATCHER.sh")
    action_module_path = os.path.join(project_module_path, "action")

    vars = {
        "name": project_name,
        "folder_name": folder_name,
        "project_path": project_path,
        "project_module_path": project_module_path,
        "action_folder": action_module_path,
        "media_folder": os.path.join(RESOURCES_PATH, "media"),
        "run_py": template_run_py_path,
        "app_py": template_app_py_path,
        "web_py": template_web_py_path,
        "watcher_sh": os.path.join(RESOURCES_PATH, "WATCHER.sh"),
        "requirements_txt": os.path.join(RESOURCES_PATH, "requirements.txt"),
        "action_module_init": os.path.join(action_module_path, "__init__.py"),
        "project_module_init": os.path.join(project_module_path, "__init__.py"),
    }

    commands = [
        "mkdir -p %(action_folder)s" % vars,
        "cd %(project_path)s" % vars,
        "virtualenv v_env",
        "cp -R %(media_folder)s %(project_module_path)s" % vars,
        "touch %(action_module_init)s" % vars,
        "touch %(project_module_init)s" % vars,

        # add in project files
        "cp -R %(app_py)s %(project_module_path)s" % vars,
        "cp -R %(web_py)s %(project_module_path)s" % vars,
        "cp -R %(run_py)s %(project_path)s" % vars,
        "cp -R %(watcher_sh)s %(project_path)s" % vars,
        "cp -R %(requirements_txt)s %(project_path)s" % vars,

        "source v_env/bin/activate",
        "PATH=/opt/local/lib/postgresql94/bin:$PATH pip install psycopg2",
        "pip install -r requirements.txt",

        # init git
        "git init",
        "git add . -A",
        "git commit -m \"virgin\"",
    ]
    _run_cmd_lis(commands)

    _replace_line_in_file(destination_run_py_path,
                          "from {{MODULE_NAME}}.web import app",
                          "from %s.web import app" % project_name)

    _replace_line_in_file(destination_web_py_path,
                          "from {{MODULE_NAME}}.app import app",
                          "from %s.app import app" % project_name)

    _replace_line_in_file(destination_watcher_path,
                          "python /Users/nubela/Workspace/transcompiler-watcher/src/watch.py <REPLACEME>",
                          "python /Users/nubela/Workspace/transcompiler-watcher/src/watch.py %s" % project_name)



def _replace_line_in_file(file_path, orig_line, new_line):
    new_line = "%s\n" % (new_line)
    f = open(file_path, "r")
    all_lines = f.readlines()
    for n, line in enumerate(all_lines):
        if line.replace("\n", "") == orig_line:
            all_lines[n] = new_line

    f = open(file_path, "w")
    f.writelines(all_lines)
    f.close()


def _run_cmd_lis(cmd_lis):
    """
    Runs a list of commands (string) on the system
    :param cmd_lis:
    :return:
    """
    full_cmd = " && ".join(cmd_lis)
    os.system(full_cmd)


if __name__ == '__main__':
    manager.main()
