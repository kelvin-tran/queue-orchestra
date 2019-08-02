import re
from setuptools import setup, find_packages


__requires__ = ['pipenv']
version_file = "queue_orchestra/version.py"
ver_str_line = open(version_file, "rt").read()
vs_re = r"^__version__ = ['\"]([^'\"]*)['\"]"
match = re.search(vs_re, ver_str_line, re.M)
if match:
    ver_str = match.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (version_file,))


if __name__ == '__main__':
    name = 'queue-orchestra'
    description = """
    Orchestrate running of processes at scale using Google PubSub 
    queue infrastructure.
    """
    setup(
        name=name,
        author='Kelvin Tran',
        author_email='mrkelvintran@gmail.com',
        version=ver_str,
        packages=find_packages(),
        description=description,
        url='https://github.com/kelvin-tran/queue-orchestra',
        classifiers=[
            'Programming Language :: Python :: 3.7',
            'Operating System :: Unix',
            'Operating System :: MacOS',
        ],
        setup_requires=[
            'setuptools>=3.4.4',
        ],
    )
