import os
import re
from setuptools import find_packages, setup


def read(f):
    return open(f, 'r', encoding='utf-8').read()


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version('read_log')


setup(
    name='django-read-log',
    version=version,
    url='https://www.django-rest-framework.org/',
    license='MIT',
    description='Read log audit for django ',
    long_description=read('README.rst'),
    long_description_content_type='text/x-rst',
    author='Mikkel Aleister Clausen',
    author_email='mac@magenta.dk',
    packages=find_packages(exclude=['test_read_log']),
    include_package_data=True,
    install_requires=["django>=2.2"],
    python_requires=">=3.5",
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
    ],
    project_urls={
        'Source': 'https://github.com/magenta-aps/django-read-log',
        'Company': 'https://www.magenta.dk/'
    },
)