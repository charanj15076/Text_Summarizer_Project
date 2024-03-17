import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

__version__ = "0.0.0"

REPO_NAME = "Text_Summarizer_Project"
AUTHOR_USER_NAME = "charanj15076"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "charanj15076@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": "https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)