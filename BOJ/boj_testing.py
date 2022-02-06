from time import time

class Case:

    def __init__(self, raw_input: str, answer) -> None:
        '''
        params:
            raw_input: str, multiline string of raw input 
            answer: associated answer to the raw_input
        '''
        self.meta_line = []
        self.lines = []
        self.answer = answer
        self.raw_input = raw_input
        self.parse_raw_input(self.raw_input)

    def __repr__(self) -> str:
        return f"Case(answer:{self.answer}, meta:{self.meta_line},lines:{self.lines})"

    def add_to_test(self, test):
        '''
        Params:
            test: Test object
        '''
        assert isinstance(test, TestSet), f"{test} is not a instance of TestSet"
        test.add(self)

    def parse_raw_input(self, raw, sep=None, is_meta_firstline=True):
        '''
        parses raw input into "meta_line" and "lines".
        "lines" are just lines of input therefore additional type converision or splitting must be done in some other part of your code.
        Typically "meta_line" is the first line of BOJ test cases which usually describes
        the cardinality(dimension) of input data.
        '''
        for i, line in enumerate(raw.splitlines()):
            if line != '':
                splitted_line_args = line.split(sep=sep)
                for arg in splitted_line_args:
                    if i == is_meta_firstline:
                        self.meta_line.append(arg)
                    else:
                        self.lines.append(arg)


class TestSet(set):
    def add(self, item:Case):
        if not isinstance(item, Case):
            raise TypeError
        super(TestSet, self).add(item)

    def remove(self, item:Case):
        if not isinstance(item, Case):
            raise TypeError
        super(TestSet, self).remove(item)

    def run(self, fn):
        print(f"Start Test")
        total_start_time = time()
        for case in super().__iter__():
            case_start_time = time()
            if fn(case.meta_line, case.lines) == case.answer:
                print("\N{grinning face with smiling eyes}", f"[{round(time() - case_start_time,3)}]",f"Passed {case}")
            else:
                print("\N{nauseated face}", f"Failed {case}")
        print("End of Test.", f"Elapsed time: {time() - total_start_time}")
