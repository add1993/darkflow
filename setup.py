from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize
import numpy
import os
import imp

VERSION = imp.load_source('version', os.path.join('.', 'darkflow_v2', 'version.py'))
VERSION = VERSION.__version__

if os.name =='nt' :
    ext_modules=[
        Extension("darkflow_v2.cython_utils.nms",
            sources=["darkflow_v2/cython_utils/nms.pyx"],
            #libraries=["m"] # Unix-like specific
            include_dirs=[numpy.get_include()]
        ),        
        Extension("darkflow_v2.cython_utils.cy_yolo2_findboxes",
            sources=["darkflow_v2/cython_utils/cy_yolo2_findboxes.pyx"],
            #libraries=["m"] # Unix-like specific
            include_dirs=[numpy.get_include()]
        ),
        Extension("darkflow_v2.cython_utils.cy_yolo_findboxes",
            sources=["darkflow_v2/cython_utils/cy_yolo_findboxes.pyx"],
            #libraries=["m"] # Unix-like specific
            include_dirs=[numpy.get_include()]
        )
    ]

elif os.name =='posix' :
    ext_modules=[
        Extension("darkflow_v2.cython_utils.nms",
            sources=["darkflow_v2/cython_utils/nms.pyx"],
            libraries=["m"], # Unix-like specific
            include_dirs=[numpy.get_include()]
        ),        
        Extension("darkflow_v2.cython_utils.cy_yolo2_findboxes",
            sources=["darkflow_v2/cython_utils/cy_yolo2_findboxes.pyx"],
            libraries=["m"], # Unix-like specific
            include_dirs=[numpy.get_include()]
        ),
        Extension("darkflow_v2.cython_utils.cy_yolo_findboxes",
            sources=["darkflow_v2/cython_utils/cy_yolo_findboxes.pyx"],
            libraries=["m"], # Unix-like specific
            include_dirs=[numpy.get_include()]
        )
    ]

else :
    ext_modules=[
        Extension("darkflow_v2.cython_utils.nms",
            sources=["darkflow_v2/cython_utils/nms.pyx"],
            libraries=["m"] # Unix-like specific
        ),        
        Extension("darkflow_v2.cython_utils.cy_yolo2_findboxes",
            sources=["darkflow_v2/cython_utils/cy_yolo2_findboxes.pyx"],
            libraries=["m"] # Unix-like specific
        ),
        Extension("darkflow_v2.cython_utils.cy_yolo_findboxes",
            sources=["darkflow_v2/cython_utils/cy_yolo_findboxes.pyx"],
            libraries=["m"] # Unix-like specific
        )
    ]

setup(
    version=VERSION,
	name='darkflow_v2',
    description='Darkflow',
    license='GPLv3',
    url='https://github.com/thtrieu/darkflow_v2',
    packages = find_packages(),
	scripts = ['flow_v2'],
    ext_modules = cythonize(ext_modules)
)
