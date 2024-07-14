#setup.py file is responsible for creating machine learning applications into a package

from setuptools import find_packages, setup


def get_requirements(file_path: str) -> list[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() #readlines reads each line ond by one
        requirements = [req.replace("\n", "") for req in requirements]


setup(
name = 'mlproject',
version = '0.0.1',
author = 'Ahmed',
author_email = 'ahmednaeem786@hotmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)