from setuptools import setup, find_packages

setup(
    name="mbot",
    packages=find_packages(where="src"),
    package_dir={"":"src"},
    version="0.1",
    py_modules=['mbot'],
    entry_points='''
        [console_scripts]
        mbot=mbot:main
    ''',
    install_requires=[
      "python-telegram-bot",
    ],
)
