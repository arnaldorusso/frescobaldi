import os
import sys
from distutils.core import setup
from frescobaldi_app import info

def packagelist(directory):
    """Returns a sorted list with package names for all packages under the given directory."""
    return list(sorted(root.replace('/', '.')
        for root, dirs, files in os.walk(directory)
        if '__init__.py' in files))

scripts = ['frescobaldi']
if sys.platform.startswith('win'):
	scripts.append('frescobaldi-postinstall.py')

packages = packagelist('frescobaldi_app')
package_dir = dict((p, p.replace('.', os.sep)) for p in packages)
package_data = {
	'frescobaldi_app.hyphdicts': ['*.dic'],
	'frescobaldi_app.icons': [
		'*.svg', '*x*/.png',
		'tango/*.svg', 'tango/*x*/*.png',
		],
	'frescobaldi_app.po': ['*.mo'],
	'frescobaldi_app.symbols': ['*.svg'],
	'frescobaldi_app.postinstall': ['*.ico'],
}
data_files = [
	('share/icons/hicolor/scalable/apps', ['frescobaldi_app/icons/frescobaldi.svg']),
	('share/applications', ['frescobaldi.desktop']),
]
classifiers = [
	'Development Status :: 3 - Alpha',
	'Intended Audience :: End Users/Desktop',
	'License :: OSI Approved :: GNU General Public License (GPL)',
	'Operating System :: MacOS :: MacOS X',
	'Operating System :: Microsoft :: Windows',
	'Operating System :: POSIX',
	'Programming Language :: Python',
	'Topic :: Multimedia :: Sound/Audio',
	'Topic :: Multimedia :: Graphics',
]

setup(
    name = info.name,
    version = info.version,
    description = info.description,
    long_description = info.long_description,
    maintainer = info.maintainer,
    maintainer_email = info.maintainer_email,
    url = info.url,
    license = info.license,
    
	scripts = scripts,
	packages = packages,
	package_dir = package_dir,
	package_data = package_data,
	data_files = data_files,
	classifiers = classifiers,
)

