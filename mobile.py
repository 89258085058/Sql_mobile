from mobile_query import SqlMobile


class Mobile():

    def mobile_start(self):
        SqlMobile.create_table()

        SqlMobile.insert_users(('User1', 10000, 2, 'Yes'))
        SqlMobile.insert_users(('User2', 10000, 3, 'Yes'))
        SqlMobile.insert_users(('User3', 10000, 1, 'Yes'))

        SqlMobile.insert_tariff(('Standard', 500))
        SqlMobile.insert_tariff(('VIP', 1000))
        SqlMobile.insert_tariff(('Premium', 1500))

    def tariff_withdraw(self):
        SqlMobile.active_user()
        period = input('\nВведите количество месяцев: ')
        SqlMobile.withdraw_money(period)


mb = Mobile()
mb.mobile_start()
mb.tariff_withdraw()
