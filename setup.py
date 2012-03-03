from setuptools import setup, find_packages
setup(
    name = "django-liveserver",
    version = "0.1a",
    packages = find_packages(),

    install_requires = ['django>=1.3'],

    # package_data = {
    # },

    # metadata for upload to PyPI
    author = "Alec Koumjian",
    author_email = "akoumjian@gmail.com",
    description = "A backport of the Django 1.4 LiveServerTestCase for 1.3",
    keywords = "django live server selenium test testcase",
)
