Django LiveServer
==================

A simple backport/extraction of the Django 1.4a LiveServerTestCase. Use selenium, splinter, or other browser clients for advanced functional testing. Credit goes to the Django core developers and extracted code comes from https://gist.github.com/1685139.

Quick Start
-----------
First install using pip or setup.py:

`pip install django-liveserver`

Install selenium or another browser testing framework:

`pip install selenium`

Create your own test case. Here is an example:


```python
from django_liveserver.testcases import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


class MySeleniumTests(LiveServerTestCase):
    fixtures = ['test-data.json']

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(MySeleniumTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(MySeleniumTests, cls).tearDownClass()
        cls.selenium.quit()

    def test_hello(self):
        self.selenium.get(self.live_server_url)
        self.assertIn("Hello World", self.selenium.title)
```

Notes
-----

Since this code extraction, the 1.4 code has changed and this version might not include some useful improvements.