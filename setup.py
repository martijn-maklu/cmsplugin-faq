from setuptools import setup, find_packages
import os
import cmsplugin_faq
media_files = []

for dirpath, dirnames, filenames in os.walk('cmsplugin_faq'):
    media_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])

setup(
    author="tehfink",
    name='cmsplugin-faq',
    version=cmsplugin_faq.__version__,
    description='creates, links, and lists FAQ entries for Django CMS',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.txt')).read(),
    url='http://bitbucket.org/tehfink/cmsplugin-faq/',
    license='BSD License',
    platforms=['OS Independent'],
    requires=[
        'django (>1.1.0)',
        'cms (>2.0.0)',
    ],
    
    packages=find_packages(),
    package_dir={
        'cmsplugin_faq': 'cmsplugin_faq',
    },
    data_files = media_files,
    package_data = {
        'cmsplugin_faq': [
            'templates/plugins/cmsplugin_faq/*.html',
        ],
    },
    zip_safe = False
)
