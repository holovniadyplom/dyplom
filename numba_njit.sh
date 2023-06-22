export CYTHON=0 TYPED=0 && \
echo "$(. ./$1/env.sh && python numba_njit.py $1)" >> ./$1/numba_njit.log
