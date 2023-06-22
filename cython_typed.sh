export CYTHON=0 TYPED=0 && \
. ./cython_typed_build.sh && \
echo "$(. ./$1/env.sh && export CYTHON=1 MODULE=$1 TYPED=1 && python cython.py $1)" >> ./$1/cython_typed.log
