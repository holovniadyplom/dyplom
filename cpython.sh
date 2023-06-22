export CYTHON=0 TYPED=0 && \
echo "$(. ./$1/env.sh && python cpython.py $1)" >> ./$1/cpython.log
