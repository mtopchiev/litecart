from fixture.application import Application
import pytest

def test_login_and_close(app):
    #self.app = Application()
    app.login_admin()
    app.driver.quit()