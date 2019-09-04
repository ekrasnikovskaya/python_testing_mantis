import random


def test_del_project(app, db):
    app.session.login(app.config['webadmin']['username'], app.config['webadmin']['password'])
    assert app.session.is_logged_in_as("administrator")
    old_projects = db.get_project_list()
    if old_projects == []:
        app.project.create_new_project("Test")
    old_project_ids = []
    for item in old_projects:
        old_project_ids.append(db.get_project_id(item))
    project = random.choice(old_projects)
    app.project.delete_project(project)
    old_projects.remove(project)
    old_project_ids.remove(db.get_project_id(project))
    new_projects = db.get_project_list()
    new_project_ids = []
    for project in new_projects:
        id = app.soap.get_project_id(
            app, app.config['webadmin']['username'], app.config['webadmin']['password'], project)
        new_project_ids.append(id)
    assert sorted(old_project_ids) == sorted(new_project_ids)
    assert sorted(old_projects) == sorted(new_projects)