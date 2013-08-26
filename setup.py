
import os
import sys

import mailclient

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'mailclient',
]

requires = ['python-magic']

setup(
    name='mailclient',
    version=mailclient.__version__,
    description='Simplified use of smtplib for Python. Easy email sending.',
    long_description='Use smtplib without problems. It\'s a wrapper to '
                     'easily work with the standard library.'
                     'It supports email sending (of course!), '
                     'and attaching file without '
                     'worrying about the mime type. You can check '
                     'the source code and examples at http://www.github'
                     '.com/aesptux/mailclient',
    author='Adrian Espinosa',
    author_email='aespinosamoreno@gmail.com',
    url='http://www.adrianespinosa.com',
    packages=packages,
    include_package_data=True,
    install_requires=requires,
    license='Apache 2.0',
    zip_safe=False,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',

    ),
    )