import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        self.runner_1 = Runner('runner_1')
        for i in range(10):
            self.runner_1.walk()
        self.assertEqual(self.runner_1.distance, 50)

    # При изменении значения 50 на 20: AssertionError: 50 != 20
    # 20 != 50
    # Expected :50
    # Actual   :20

    def test_run(self):
        self.runner_2 = Runner('runner_2')
        for i in range(10):
            self.runner_2.run()
        self.assertEqual(self.runner_2.distance, 100)

    # При изменении значения 100 на 110: AssertionError: 100 != 110
    # 110 != 100
    # Expected :100
    # Actual   :110

    def test_challenge(self):
        self.runner_3 = Runner('runner_3')
        self.runner_4 = Runner('runner_4')
        for i in range(10):
            self.runner_3.run()
            self.runner_4.walk()
        self.assertNotEqual(self.runner_3.distance, self.runner_4.distance)


# Если в цикле For вызвать self.runner_4.walk() два раза чтобы дистанции были равны: AssertionError: 100 == 100


if __name__ == '__main__':
    unittest.main()
