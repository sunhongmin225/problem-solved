# Baekjoon Online Judge
https://www.acmicpc.net

## Testing

`./BOJ/boj_testing.py` 를 통해 standard 또는 custom case를 쉽게 테스트할 수 있다. 동작원리는 간단한다. `TestSet`에 `Case`들을 추가한 뒤 `TestSet`의 `run()` 메소드를 호출하는 것이다.`Case` 객체를 정의하기 위해서는 웹사이트에서 복사한 case를 저장한 multiline string과 그에 상응하는 정답이 필요하다. 그리고 해당 `Case`를 `TestSet`에 넣기 위해서는 `t = TestSet()` 과 같이 원소가 없는 `TestSet`을 생성한 뒤 이에 추가하면 된다. 다음 두가지 방법을 지원한다.

`TestSet.run()` 메소드는 솔루션 함수를 단일입력으로 받고 각 케이스의 `Case.meta_line`과 나머지 `Case.lines`를 `Case.answer`와 비교하여 테스트를 진행한다. 

*Method 1*
```python
t = TestSet() # initiate empty set
raw = '''
4 6
101111
101010
101011
111011
'''
Case(raw, 15).add_to_test(t)


def your_solution(meta_data, lines):
	...

if __name__=="__main__":
	t.run(your_solution) 
```

*Method 2*
```python
t = TestSet()
raw = '''
4 6
101111
101010
101011
111011
'''
t.add(Case(raw, 15))


def your_solution(meta_data, lines):
	...

if __name__=="__main__":
	t.run(your_solution) 
```

`./2178_maze/DOS.py` 를 실행하면 결과물은 다음과 같다.
```bash
$ /usr/local/bin/python3.9 /Users/dongookson/Code/problem-solved/BOJ/2178_maze/DOS.py
```

```txt
Start Test
😁 [0.0] Passed Case(answer:13, meta:['7', '7'],lines:['1011111', '1110001', '1000001', '1000001', '1000001', '1000001', '1111111'])
😁 [0.0] Passed Case(answer:38, meta:['2', '25'],lines:['1011101110111011101110111', '1110111011101110111011101'])
😁 [0.0] Passed Case(answer:15, meta:['4', '6'],lines:['101111', '101010', '101011', '111011'])
End of Test. Elapsed time: 0.0001571178436279297
```

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
