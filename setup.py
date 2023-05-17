
from pip._internal.req import parse_requirements        
from setuptools import setup, find_packages

def load_requirements(fname):
    reqs = parse_requirements(fname, session=False)
    try:
        requirements = [str(ir.requirement) for ir in reqs]
    except AttributeError:
        requirements = [str(ir.req) for ir in reqs]
    return requirements

setup(
    name='htmldocx',
    version='0.0.6',
    packages=find_packages(),
    install_requires=load_requirements("requirements.txt")
)