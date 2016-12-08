# -*- coding:utf-8 -*-
from setuptools import find_packages
from setuptools import setup

version = '1.0a1'
description = 'SMDU Barra de identidade visual.'
long_description = (
    open('README.rst').read() + '\n' +
    open('CONTRIBUTORS.rst').read() + '\n' +
    open('CHANGES.rst').read()
)

setup(
    name='smdu.identidadevisual',
    version=version,
    description=description,
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Framework :: Plone :: 4.3',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='smdu',
    author='Héctor Velarde',
    author_email='hector.velarde@gmail.com',
    url='https://github.com/hvelarde/smdu.identidadevisual',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['smdu'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'plone.app.layout',
        'plone.app.registry',
        'plone.autoform',
        'plone.registry',
        'plone.supermodel',
        'Products.CMFCore',
        'Products.CMFPlone >=4.3',
        'Products.CMFQuickInstallerTool >=3.0.9',  # use uninstall profile
        'Products.GenericSetup',
        'setuptools',
        'zope.component',
        'zope.i18nmessageid',
        'zope.interface',
        'zope.schema',
    ],
    extras_require={
        'test': [
            'AccessControl',
            'plone.api',
            'plone.app.robotframework',
            'plone.app.testing [robot]',
            'plone.browserlayer',
            'plone.registry',
            'plone.testing',
            'robotsuite',
            'zope.component',
            'zope.viewlet',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
    )
