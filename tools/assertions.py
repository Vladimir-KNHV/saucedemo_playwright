import allure

class Assertions:

    @staticmethod
    def assert_sorted(values: list, reverse: bool = False):
        with allure.step(f'Asserting items is sorted (reverse={reverse})'):
            assert values == sorted(values, reverse=reverse)