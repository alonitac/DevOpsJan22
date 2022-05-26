def sudoku_solver():
    pass


class Singleton:

    _instance = None

    @staticmethod
    def get_instance():
        if Singleton._instance is not None:
            return Singleton._instance

        return Singleton()

    def __init__(self):
        if Singleton._instance is not None:
            raise RuntimeError('Class Singleton can be instantiated only once')

        Singleton._instance = self


# my_singleton2 = Singleton.get_instance()
# my_singleton = Singleton()


def binary_search():
    pass


def psutils():
    pass  # https://github.com/giampaolo/psutil


def mailer():
    pass  # https://github.com/kootenpv/yagmail


def run_config_env_var():
    pass


def logger():
    pass


def geo():
    pass


def pyjwt_demo():
    pass


def pyaudio():
    pass


