# -*- coding: utf-8 -*-

from dateutil.relativedelta import relativedelta

def cal_end_date(start_date, duration):
    end_date = start_date + relativedelta(years=duration["years"], months=duration["months"], days=duration["days"])
    return end_date
