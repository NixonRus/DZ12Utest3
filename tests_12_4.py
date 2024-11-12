import logging
import unittest
from unittest import TestCase
from rt_with_exceptions import Runner


class RunnerTest(TestCase):
    is_frozen = False

    def test_walk(self):
        try:
            run = Runner('Ted', speed=-5)
            logging.info('"test_walk" выполнен успешно')
            for i in range(10):
                run.walk()
            return self.assertEqual(run.distance, 50)
        except ValueError:
            logging.warning('Неверная скорость для объекта Runner')

    def test_run(self):
        try:
            run = Runner(56)
            logging.info('"test_run" выполнен успешно')
            for i in range(10):
                run.run()
            return self.assertEqual(run.distance, 100)
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner')

    def test_challenge(self):
        run1 = Runner('Ted')
        run2 = Runner('Bil')
        for i in range(10):
            run1.run()
            run2.walk()
        return self.assertNotEqual(run1.distance, run2.distance)


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                    format='%(asctime)s | %(levelname)s |  %(funcName)s: %(lineno)d | %(message)s')
