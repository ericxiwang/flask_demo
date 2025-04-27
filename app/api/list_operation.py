class list_operation:
    def __init__(self):
        pass
    @staticmethod
    def sequential_array(list_len):
        return [x for x in range(0,list_len + 1)]

    @staticmethod
    def list_comprehension(list_len):
        new_list = [i ** 2 for i in range(1, list_len) if i * (i - 2) % 3 == 0]
        return new_list

    @staticmethod
    def fib_array_loop(array_len):
        fib_array = []
        if array_len <= 1:
            return fib_array.append(array_len)
        a, b = 1, 1
        for i in range(2, array_len + 1):
            a, b = b, a + b
            fib_array.append(a)
            fib_array.append(b)
        return sorted(list(set(fib_array)))

    def fib_recursion_1(prev1, prev2, count):
        for each_count in range(0, count):
            newFibo = prev1 + prev2
            prev2 = prev1
            prev1 = newFibo
            count += 1
            fib_recursion_1(prev1, prev2, count)
            return newFibo
        else:
            return
    @classmethod
    def list_generator(cls,list_len):
        user_limit = list_len
        cls.sample_list = []
        for i in range(1, user_limit):
            if i * (i - 2) % 3 == 0:
                cls.sample_list.append(i ** 2)
        return cls.sample_list
    def list_output(self,input_list):
        return input_list,input_list[::-1]

if __name__ == "__main__":
    a = list_operation()

    print(a.sequential_array(10))

    print(a.list_output(a.sequential_array(10)))
    print(a.fib_array_loop(10))
    print(a.list_output(a.fib_array_loop(10)))
    print(a.list_output(a.list_comprehension(10)))

