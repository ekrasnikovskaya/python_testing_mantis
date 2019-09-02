import random


def test_del_project(app, db):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    old_projects = db.get_project_list()
    if old_projects == []:
        app.project.create_new_project("Test")
    project = random.choice(old_projects)
    app.project.delete_project(project)
    old_projects.remove(project)
    new_projects = db.get_project_list()
    assert sorted(old_projects) == sorted(new_projects)