import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        self.runner_1 = Runner('runner_1')
        for i in range(10):
            self.runner_1.walk()
        self.assertEqual(self.runner_1.distance, 50)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        self.runner_2 = Runner('runner_2')
        for i in range(10):
            self.runner_2.run()
        self.assertEqual(self.runner_2.distance, 100)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        self.runner_3 = Runner('runner_3')
        self.runner_4 = Runner('runner_4')
        for i in range(10):
            self.runner_3.run()
            self.runner_4.walk()
        self.assertNotEqual(self.runner_3.distance, self.runner_4.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for value in cls.all_results.values():
            print(value)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run_1(self):
        self.tournament = Tournament(90, self.runner_1, self.runner_3)
        self.res = self.tournament.start()
        k = 'test_run_1'
        v = self.res
        self.all_results['test_run_1'] = self.res
        self.assertTrue(self.res[max(self.res)] == 'Ник')

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run_2(self):
        self.tournament = Tournament(90, self.runner_2, self.runner_3)
        self.res = self.tournament.start()
        k = 'test_run_2'
        v = self.res
        self.all_results['test_run_2'] = self.res
        self.assertTrue(self.res[max(self.res)] == 'Ник')

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run_3(self):
        self.tournament = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.res = self.tournament.start()
        k = 'test_run_3'
        v = self.res
        self.all_results['test_run_3'] = self.res
        self.assertTrue(self.res[max(self.res)] == 'Ник')


if __name__ == '__main__':
    unittest.main()
