# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2021/4/28 11:03

from setuptools import setup, find_packages

from flask_openapi3 import __version__

long_description = open('README.md', 'r', encoding='utf-8').read()

setup(
    name="flask-openapi3",
    version=__version__,
    url='https://github.com/luolingchun/flask-openapi3',
    description='Generate RESTful API and OpenAPI document for your Flask project.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    license_files='LICENSE.rst',
    author='llc',
    author_email='luolingchun@outlook.com',
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.7",
    zip_safe=False,
    platforms='any',
    install_requires=["Flask>=1.0", "pydantic>=1.2"],
    classifiers=[
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha    ',
        # 'Development Status :: 4 - Beta',
        'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ]
)
