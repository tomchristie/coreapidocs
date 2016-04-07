from setuptools import find_packages, setup

setup(
    name='coreapidocs',
    version=__import__('coreapidocs').__version__,
    author="Emmanouil Konstantinidis",
    author_email="manos@iamemmanouil.com",
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/ekonstantinidis/coreapidocs",
    license='BSD',
    description="Document APIs with CoreAPI.",
    install_requires=[
        'Jinja2',
        'coreapi'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
)
