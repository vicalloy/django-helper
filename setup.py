from setuptools import setup, find_packages

version = '0.8.1'

LONG_DESCRIPTION = """
"""

setup(
    name='django-helper',
    version=version,
    description="A set of useful function/tags/filter for Django.",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='helper,django',
    author='vicalloy',
    author_email='zbirder@gmail.com',
    url='https://github.com/vicalloy/django-helper/',
    license='BSD',
    packages=find_packages(),
    package_data = {
        'djangohelper': [
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
