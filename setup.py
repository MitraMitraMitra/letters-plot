from distutils.core import setup
setup(
  name = 'letters-plot',
  packages = ['letters-plot'],
  version = '0.1',
  license = 'MIT',
  description = 'This library can be used to generate points that, when plotted, form letters. The height and spacing can be set.',
  author = 'Jean-Paul Mitra',
  author_email = 'jeanmitra77@gmail.com',
  url = 'https://github.com/MitraMitraMitra/letters-plot-generator',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['plotting', 'letters'],
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers = [
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: hobbyists, memelords',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)