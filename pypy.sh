export CYTHON=0 TYPED=0 && \
echo "$(. ./$1/env.sh && ./pypy3.9-v7.3.11/bin/pypy3 pypy.py $1)" >> ./$1/pypy.log
