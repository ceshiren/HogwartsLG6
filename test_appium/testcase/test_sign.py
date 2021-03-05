from test_appium.pages.app import App


class TestSign:
    def setup(self):
        self.app = App()

    def test_sign(self):
        self.app.goto_main().goto_work_page().goto_sign_page().sign()
