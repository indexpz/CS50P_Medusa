from project import show_average_per_day, get_file_name, get_max_min_usage
import pytest
from io import StringIO


def test_function_1():
	d = [({'date': '2015-12-01', 'meter': 318.0, 'new_meter': True, 'usage_per_day': 7.645161290322581, 'units': 'kWh', 'days_between': 31.0, 'meter_diff': 237.0}),({'date': '2016-01-01', 'meter': 555.0, 'new_meter': False, 'usage_per_day': 7.67741935483871, 'units': 'kWh', 'days_between': 31.0, 'meter_diff': 238.0}),({'date': '2016-02-01', 'meter': 793.0, 'new_meter': False, 'usage_per_day': 8.285714285714286, 'units': 'kWh', 'days_between': 28.0, 'meter_diff': 232.0})]
	assert show_average_per_day(d) == 7.869431643625194


def test_function_2():
	d = [({'date': '2015-12-01', 'meter': 318.0, 'new_meter': True, 'usage_per_day': 7.645161290322581, 'units': 'kWh', 'days_between': 31.0, 'meter_diff': 237.0}),({'date': '2016-01-01', 'meter': 555.0, 'new_meter': False, 'usage_per_day': 7.67741935483871, 'units': 'kWh', 'days_between': 31.0, 'meter_diff': 238.0}),({'date': '2016-02-01', 'meter': 793.0, 'new_meter': False, 'usage_per_day': 8.285714285714286, 'units': 'kWh', 'days_between': 28.0, 'meter_diff': 232.0})]
	assert get_max_min_usage(d, "max") == (8.285714285714286, 2)


def test_function_3(monkeypatch):
	file_name = StringIO('aaa.csv\n')
	monkeypatch.setattr('sys.stdin', file_name)
	assert get_file_name() == "aaa.csv"


