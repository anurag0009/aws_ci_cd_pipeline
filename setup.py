from setuptools import find_packages,setup
from typing import List
#nas
HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    this fuction will return the lsit of requirements
    '''
    requirements = []
    with open(file_path) as  file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n" ,"") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements



setup(

name = 'AWS_CLI_CI_CD_PIPELINE',
version = '0.0.1', 
author = "Anurag Singh",
author_email = "anuragsingh775489@gamil.com",
packages=find_packages(),
install_requires = get_requirements('requirements.txt')
)
