from db import *
import unittest


class TestDB(unittest.TestCase):

    def setUp(self) -> None:
        self.db = EagleMonogoDB('pcentos.hujun.com', 27017, 'EagleEye')

    def test_is_trading_day(self):
        day = '2022-11-04'
        result = self.db.is_trading_day(day)
        assert result == True

        day = '2022-11-05'
        result = self.db.is_trading_day(day)
        assert result == False

    """
        def test_query_user_password(self):
        username = 'hujun'
        password, uid = self.db.query_user_password(username)
        print(password, uid)
    """

    def test_insert_user_info(self):
        user_info_dict = {'username': 'sanqiyanxishe@163.com', 'password': 'todayGood123', "valid_days": 30}
        a = self.db.insert_user_info(user_info_dict)
        assert a == True

    def test_now_is_trading_time(self):
        result = self.db.now_is_trading_time()
        assert result == False

    def test_user_is_in_valid_period(self):
        user_info_dict = {'username': 'sanqiyanxishe@163.com', "register_at": '2021-10-29 08:00:00', "valid_days": 30}

        a = user_is_in_valid_period(user_info_dict)
        assert a == False

        user_info_dict = {'username': 'sanqiyanxishe@163.com', "register_at": '2022-10-29 08:00:00', "valid_days": 30}

        b = user_is_in_valid_period(user_info_dict)
        assert b == True

    def test_create_warn_table(self):

        self.db.create_warn_table('sanqiyanxishe@163.com')