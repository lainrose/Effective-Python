import sys

# 16쪽. 사용 중인 파이썬의 버전을 알자.
# 2016/09월 02일 작성.

"""
어떻게 사용 중인 파이썬의 버전을 알 수 있을까? 방법은 여러 가지가 있다.
"""

"""
1. 커맨드 창에서 버젼 알아보기.
일반 커맨드 창에서 'python'이라고만 입력해서 파이썬 인터프리터를 많이 실행할 것이다.
그런데 일반 커맨드 창에서처럼 python에도 옵션을 줄 수 있는데 이것을 통해 버젼을 확인할 수 있다.
"""

# python --version
# python -V

# 이와 같은 과정으로 현재 설치된 파이썬의 버젼을 알 수 있다. -V가 대문자임을 유의하자. 소문자로 쓸 경우
# verbose 모드가 적용된다. 궁금하면 한 번 해보기 바란다. ㅋㅋ


"""
2. sys 모듈을 통해서 버젼 알아보기.
내장 모듈로 sys모듈이 있다. import해서 알아보자.
"""
print(sys.version)
print(sys.version_info)

# 확인해보면 둘의 결과가 조금 다름을 알 수 있다.
# sys.version은 요약된 정보를 보여준다.
# sys.version_info 는 info라는 단어에서 알 수 있듯이 3.5.1의 버젼 정보를 잘라서 정확히 보여준다.
# 무슨  차이가 있겠냐마는, 물론 나도 정확히는 모르겠다.

# 참고로 버젼이 3.5.1일때 3이 major, 5가 minor, 1이 micro 단위이다. 참고하자!