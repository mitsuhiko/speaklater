import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def get_docs():
    result = []
    in_docs = False
    f = open(os.path.join(os.path.dirname(__file__), 'speaklater.py'))
    try:
        for line in f:
            if in_docs:
                if line.lstrip().startswith(':copyright:'):
                    break
                result.append(line[4:].rstrip())
            elif line.strip() == 'r"""':
                in_docs = True
    finally:
        f.close()
    return '\n'.join(result)

setup(
    name='speaklater',
    author='Armin Ronacher',
    author_email='armin.ronacher@active-4.com',
    version='1.2',
    url='http://dev.pocoo.org/hg/speaklater-main',
    py_modules=['speaklater'],
    description='implements a lazy string for python useful for use with gettext',
    long_description=get_docs(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Internationalization',
        'Programming Language :: Python'
    ]
)
