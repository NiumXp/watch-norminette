from setuptools import setup

version = "0.0.1"


setup(
    name="watch-norminette",
    author="NiumXp",
    url="https://github.com/NiumXp/watch-norminette",
    version=version,
    packages=[
        "wn",
    ],
    include_package_data=True,
    python_requires=">=3.7.0",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Utilities",
    ],
    entry_points = {
        "console_scripts": [
            "wn=wn.__main__:main",
            "watch-norminette=wn.__main__:main",
        ],
    }
)
