from datetime import timedelta, datetime
import re
import sys


class Gauge:
	def __init__(self, c_list, args):
		self.c_list = self.create_list_of_dictionary(c_list, args)
		self.args = args

	def __str__(self) -> str:
		text = ""
		for row in self.c_list:
			text += f"{row}\n"
		return text

	@classmethod
	def meter_diff(cls, meter_s, meter_e) -> float:
		"""Returns difference between two meter records"""
		return float(meter_e) - float(meter_s)

	@classmethod
	def days(cls, day_s, day_e) -> float:
		"""Returns difference between time period records"""
		yyyy_s, mm_s, dd_s = day_s.strip().split("-")
		date_s = datetime(int(yyyy_s), int(mm_s), int(dd_s), 0, 0, 0, 0)

		yyyy_e, mm_e, dd_e = day_e.strip().split("-")
		date_e = datetime(int(yyyy_e), int(mm_e), int(dd_e), 0, 0, 0, 0)

		diff = date_e - date_s
		return diff / timedelta(days=1)

	@classmethod
	def usage_per_day(cls, meter_diff, days) -> float:
		"""Returns usage per day"""
		return float(meter_diff) / float(days)

	@classmethod
	def new_meter(cls, meter_s, meter_e) -> bool:
		"""Returns info about changing meter gauge on new"""
		if float(meter_s) <= float(meter_e):
			return False
		elif float(meter_s) > float(meter_e):
			return True

	@classmethod
	def get_units(cls, args) -> str:
		"""Returns info about units by prompt user and regex answer"""
		global units
		units = "m3"
		if len(args) == 1:
			while True:
				units = input("Units: ")
				if units == "exit" or units == "q":
					sys.exit("Bye bye")
				elif _ := re.search(r"^[a-zA-Z0-9]{1,10}$", units.strip()):
					return units
		elif len(args) == 2:
			if _ := re.search(r"__", args[1].strip()):
				units = args[1].strip().split("__")
				units = units[1].replace(".csv", "")
				return units
			else:
				while True:
					units = input("Units: ")
					if units == "exit" or units == "q":
						sys.exit("Bye bye")
					elif _ := re.search(r"^[a-zA-Z0-9]{1,10}$", units.strip()):
						return units

	@classmethod
	def create_list_of_dictionary(cls, c_list, args) -> list:
		"""Returns dictionary with calculate data"""
		global new_meter_info
		final_counter_list = []
		units = cls.get_units(args)
		for i in range(len(c_list)):
			if i < len(c_list) - 1:
				if i == 0:
					new_meter_info = True
				elif i != 0:
					new_meter_info = cls.new_meter(c_list[i]["meter"], c_list[i + 1]["meter"])

				if new_meter_info and i != 0:
					meter_diff = c_list[i + 1]["meter"]
					days = 1
				else:
					meter_diff = cls.meter_diff(c_list[i]["meter"], c_list[i + 1]["meter"])
					days = cls.days(c_list[i]["date"], c_list[i + 1]["date"])

				final_counter_list.append(
					{
						"date": c_list[i]["date"],
						"meter": float(c_list[i]["meter"]),
						"new_meter": new_meter_info,
						"usage_per_day": cls.usage_per_day(meter_diff, days),
						"units": units,
						"days_between": days,
						"meter_diff": meter_diff,
					}
				)
		return final_counter_list
