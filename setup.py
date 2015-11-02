"""`Domain models` setup script."""

import os
import re

from setuptools import setup
from setuptools import Command

SHORT_DESCRIPTION = 'Domain models framework for Python projects'


# Getting description:
with open('README.rst') as readme_file:
    description = readme_file.read()

    # Removing duplicated short description.
    description = description.replace(SHORT_DESCRIPTION, '')

# Getting requirements:
# with open('requirements.txt') as version:
#     requirements = version.readlines()

# Getting version:
with open('domain_models/__init__.py') as init_file:
    version = re.search('VERSION = \'(.*?)\'', init_file.read()).group(1)


class PublishCommand(Command):
    """Setuptools `publish` command."""

    description = "Publish current distribution to PyPi and create tag"
    user_options = []

    def initialize_options(self):
        """Init options."""

    def finalize_options(self):
        """Finalize options."""

    def run(self):
        """Command execution."""
        self.run_command('sdist')
        self.run_command('upload')
        os.system('git tag -a {0} -m \'version {0}\''.format(version))
        os.system('git push --tags')


setup(name='domain_models',
      version=version,
      description=SHORT_DESCRIPTION,
      long_description=SHORT_DESCRIPTION,
      author='Roman Mogilatov',
      author_email='rmogilatov@gmail.com',
      maintainer='Roman Mogilatov',
      maintainer_email='rmogilatov@gmail.com',
      url='https://github.com/rmk135/domain_models',
      license='BSD New',
      packages=['domain_models'],
      zip_safe=True,
      # install_requires=requirements,
      cmdclass={
          'publish': PublishCommand,
      },
      keywords=[
          #'Dependency injection',
          #'Dependency injection framework',
          #'Dependency injection container',
          #'Dependency injector',
          #'Dependency management',
          #'DI',
          #'DI Container',
          #'Inversion of Control',
          #'Inversion of Control container',
          #'IoC',
          #'IoC container',
      ],
      classifiers=[
          'Development Status :: 1 - Planning',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          #'Programming Language :: Python :: 2',
          #'Programming Language :: Python :: 2.6',
          #'Programming Language :: Python :: 2.7',
          #'Programming Language :: Python :: 3',
          #'Programming Language :: Python :: 3.2',
          #'Programming Language :: Python :: 3.3',
          #'Programming Language :: Python :: 3.4',
          #'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: Implementation :: CPython',
          #'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: Software Development',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ])
