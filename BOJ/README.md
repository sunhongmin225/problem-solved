# Baekjoon Online Judge
https://www.acmicpc.net

## Input Handling

백준에서는 함수 인풋을 언어마다 따로 처리해야합니다. STDIN을 통해서 제출 결과물을 검증하기 때문인 것 같습니다. 

다음 예제 입력을 예시로 사용하겠습니다. 주로 첫번째 입력은 입력을 받아들이기 위한 iteration의 수가 나옵니다.

```txt
2
GCF
ACDEB
```

위 예제에서 GCF, ACDEB를 원소로하는 파이썬 list를 생성하기 위해서는 다음과 같이 처리할 수 있습니다.

```python
def get_bj_input():
	result = []
	n = int(input())

	for _ in range(n):
		result.append(str(input()))
	
	return result
```

더 복잡한 경우도 유사한 논리로 처리할 수 있습니다. 다음 예시에서는 첫번째 줄에 열과 행의 갯수가 나오며 그 아래에는 공백으로 구분된 행렬의 원소가 나열되어있습니다.

```txt
6 4  
0 0 0 0 0 0  
0 0 0 0 0 0  
0 0 0 0 0 0  
0 0 0 0 0 1  
```

이는 파이썬에서 `list[list]`로 다음과 같이 받아들일 수 있습니다. `map` 함수는 파이썬에서 iterable한 객체의 모든 원소들을 특정한 함수에 넣은 결과값들을 iterable한 `map object`를 반환합니다. `__next__()` 와 `__iter__()` 메소드가 있기 때문에 이를 `list()` 안에 넣으면 앞서 언급한 결과값들의 `list`를 반환받을 수 있습니다.

```python
def get_bj_input():
	matrix = []
	ncol, nrow = map(int, input().split())

	for _ in range(nrow):
		row = []
		row.append(map(int, input().split()))
		matrix.append(row)
	return result
```
