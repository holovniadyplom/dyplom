cd cython_
export MODULE=$1 TYPED=0 && python setup.py build_ext --inplace
cd ..