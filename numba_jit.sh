export CYTHON=0 TYPED=0 && \
echo "$(. ./$1/env.sh && python numba_jit.py $1)" >> ./$1/numba_jit.log
