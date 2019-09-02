import random
import string


def test_add_project(app, db):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    old_projects = db.get_project_list()
    name = "".join([random.choice(string.ascii_letters) for i in range(10)])
    app.project.create_new_project(name)
    old_projects.append(name)
    new_projects = db.get_project_list()
    assert sorted(old_projects) == sorted(new_projects)

