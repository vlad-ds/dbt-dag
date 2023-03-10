from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='dbt-dag',
      version='0.1',
      description='Expose the dbt DAG as a NetworkX graph',
      url='https://github.com/vlad-ds/dbt-dag',
      author='Vlad Gheorghe',
      author_email='vlad.datapro@gmail.com',
      license='MIT',
      packages=['dbt_dag'],
      scripts=[],
      install_requires=required,
      include_package_data=True,
      zip_safe=False)
