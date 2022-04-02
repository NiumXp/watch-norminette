from setuptools import setup

version = "0.0.4"

with open("./README.md") as file:
    readme = file.read()

setup(
    name="watch-norminette",
    author="NiumXp",
    url="https://github.com/NiumXp/watch-norminette",
    version=version,
    packages=[
        "wn",
    ],
    license="GNU General Public License v3.0",
    description="Um script em Python que fica observando uma pasta e rodando o norminette nos arquivos quando forem salvos",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    python_requires=">=3.7.0",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Natural Language :: Portuguese (Brazilian)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Utilities",
    ],
    entry_points = {
        "console_scripts": [
            "wn=wn.__main__:main",
            "watch-norminette=wn.__main__:main",
        ],
    }
)
