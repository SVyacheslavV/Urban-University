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


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        # cls.all_results = [] # если сохранять в список

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        # for el in cls.all_results: # если cls.all_results список
        #     print(el)

        for value in cls.all_results.values():
            print(value)

    def test_run_1(self):
        self.tournament = Tournament(90, self.runner_1, self.runner_3)
        self.res = self.tournament.start()
        k = 'test_run_1'
        v = self.res
        self.all_results['test_run_1'] = self.res
        # self.all_results.append(self.res) # если сохраняем в список
        self.assertTrue(self.res[max(self.res)] == 'Ник')

    def test_run_2(self):
        self.tournament = Tournament(90, self.runner_2, self.runner_3)
        self.res = self.tournament.start()
        k = 'test_run_2'
        v = self.res
        self.all_results['test_run_2'] = self.res
        # self.all_results.append(self.res) # если сохраняем в список
        self.assertTrue(self.res[max(self.res)] == 'Ник')

    def test_run_3(self):
        self.tournament = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.res = self.tournament.start()
        k = 'test_run_3'
        v = self.res
        self.all_results['test_run_3'] = self.res
        # self.all_results.append(self.res) # если сохраняем в список
        self.assertTrue(self.res[max(self.res)] == 'Ник')


if __name__ == '__main__':
    unittest.main()
