cd cython_
export MODULE=$1 TYPED=1 && python setup.py build_ext --inplace
cd ..