from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT="-e"

def get_requirements(file_path:str)-> List[str]:
    """
    returns the list of requirments.
    """

    requirements=[]
    with open(file_path) as file_ojb:
        requirements=file_ojb.readline()
        requirements=[requirement.replace("\n", " ") for requirement in requirements]

        if HYPEN_E_DOT in requirements:
            requirements=requirements.remove(HYPEN_E_DOT)



setup(
    name="mlproject",
    version='0.0.1',
    author='Pramod',
    author_email='pramodthebe2@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
    
    

)