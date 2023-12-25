from src.simple_fun import say_hello


class TestSimpleFun:
    """
    Test class to test simple_fun() functionality.
    """

    def test_friend_set_to_stranger_if_param_not_set(self):
        # SETUP
        expected = '\nHello there, stranger!\n'

        # CALL
        result = say_hello()

        # ASSERT
        assert(result == expected)
