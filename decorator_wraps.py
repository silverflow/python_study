import logging as logger
import functools

"""
functools를 import 안하면 wrapped가 정의되어있지 않다고 쓸 수 없다.
데코레이터에서 wraps 데코레이터를 통해서 쓰는 것을 권장하는 이유는 개별 함수를 확인하거나 docstring이
데코레이터에 의해 덮어써지기 때문에 디버깅이 난해해지기 때문이다.
"""


def trace_decorator(function):
    @functools.wraps(function)
    def wrapped(*args, **kwargs):
        logger.info("%s 실행", function.__qualname__)
        return function(*args, **kwargs)

    return wrapped


@trace_decorator
def process_account(account_id):
    """
    id별 계정 처리 로그를 보기 위함
    """
    logger.info("%s 계정 처리", account_id)


print(process_account.__qualname__)
