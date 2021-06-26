# 언패킹시 특정 값 무시
x, _, y = (1, 2, 3)

print(x, y)

# 여러개의 값 무시

x, *_, y = (1, 2, 3, 4, 5, 6, 7, 8, 9)

print(x, y)

# 인덱스 무시
for _ in range(10):
    print("foobar")

# private 변수를 명시할 때
_some_name = "blahblah"
print(_some_name)
