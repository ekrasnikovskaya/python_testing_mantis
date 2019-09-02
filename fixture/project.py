class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Управление").click()
        wd.implicitly_wait(2)
        wd.find_element_by_link_text("Управление проектами").click()

    def create_new_project(self, name):
        wd = self.app.wd
        self.open_projects_page()
        wd.implicitly_wait(2)
        wd.find_element_by_xpath("//button[@type='submit']").click()
        wd.find_element_by_name("name").send_keys(name)
        wd.find_element_by_xpath("//input[@value='Добавить проект']").click()

    def delete_project(self, name):
        wd = self.app.wd
        self.open_projects_page()
        wd.implicitly_wait(2)
        wd.find_element_by_link_text(name).click()
        wd.find_element_by_xpath("//input[@value='Удалить проект']").click()
        wd.implicitly_wait(2)
        wd.find_element_by_xpath("//input[@value='Удалить проект']").click()