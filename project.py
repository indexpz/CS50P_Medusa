import sys
import csv
from datetime import date
from tabulate import tabulate
import re
import matplotlib.pyplot as plt

from gauge import Gauge


def main():
	args = sys.argv
	list_from_csv = get_csv_file(args)
	gauge = Gauge(list_from_csv, args)
	print(gauge)
	nav_menu(gauge.c_list)


def get_file_name():
	"""Prompt user about file name"""
	while True:
		file = input("File name: ")
		if file == "exit":
			sys.exit("Bye bye")
		elif _ := re.match(r"^[.a-zA-Z0-9 _/]+(\.csv)$", file.strip()):
			print(file)
			return file


def get_csv_file(args) -> list:
	"""Read csv file
		if prompt line have 1 argument -> file name run program
		if not have any arguments prompt user about file name
		check csv data before convert"""
	counter_list = []
	global file_name
	if len(args) == 1:
		file_name = get_file_name().strip()
	elif len(args) == 2:
		file_name = args[1].strip()
	elif len(args) > 2:
		sys.exit("Too many command-line arguments")
	try:
		with open(file_name) as file:
			reader = csv.DictReader(file)
			for row in reader:
				try:
					if date.fromisoformat(row["date"]) and float(row["meter"]):
						counter_list.append({"date": row["date"], "meter": row["meter"]})
				except ValueError:
					print(f'\n-------------------------------\nError in row: {row["date"]}, {row["meter"]}',
						  end="\n-------------------------------\n")
					pass
	except FileNotFoundError:
		sys.exit("Invalid input file.")
	return counter_list


def render_table(dictionary):
	"""Render coveted table"""
	headers = {"date": "Date",
			   "meter": "Meter",
			   "new_meter": "Gauge replaced",
			   "usage_per_day": "Usage per day",
			   "units": "Units",
			   "days_between": "Days between",
			   "meter_diff": "Usage between dates"}
	print(tabulate(dictionary, headers=headers, tablefmt="grid"))


def render_line_graph(dictionary):
	"""Render line graph"""
	input_date = []
	input_usage_per_day = []
	for row in dictionary:
		if row["new_meter"]:
			input_date.append("")
			input_usage_per_day.append(0)
		else:
			input_date.append(row["date"])
			input_usage_per_day.append(row["usage_per_day"])
	plt.style.use("classic")
	fig, ax = plt.subplots()
	ax.scatter(input_date, input_usage_per_day, s=1)
	ax.plot(input_date, input_usage_per_day, linewidth=4)

	# Zdefiniowanie tytułu wykresu i etykiet osi.
	ax.set_title("Meter – usage per day", fontsize=14)
	ax.set_xlabel("Date", fontsize=14)
	ax.set_ylabel("Usage per day", fontsize=14)
	# Zdefiniowanie wielkości etykiet.
	ax.tick_params(axis="both", which="major", labelsize=10)
	plt.show()


def get_max_min_usage(dictionary, max_min):
	l = []
	value = 0
	for i in range(len(dictionary)):
		l.append(dictionary[i]["usage_per_day"])
	if max_min == "max":
		value = max(l)
	else:
		value = min(l)
	index = l.index(value)
	return value, index


def show_max_min_usage(dictionary, max_min):
	value, index = get_max_min_usage(dictionary, max_min)
	r = dictionary[index]
	print(f"{max_min.title()} usage: {value}\n{r}")


def show_average_per_day(dictionary):
	total = 0
	for i in range(len(dictionary)):
		total += dictionary[i]["usage_per_day"]
	return total / len(dictionary)


def nav_menu(dictionary):
	"""Show nav menu"""
	print("\n"
		  "---------------------------------\n"
		  "Hello, use 1, 2, ... or exit, q\n"
		  "---------------------------------")
	while True:
		print("1. Show records table.\n"
			  "2. Show line graph.\n"
			  "3. Show max usage.\n"
			  "4. Show min usage.\n"
			  "5. Show average usage per day.\n"
			  'q. Or to quit type "exit"\n')
		user_input = input("> ")
		if _ := re.search(r"^(1|2|3|4|5|exit|q)$", user_input.strip()):
			if user_input == "1":
				render_table(dictionary)
				nav_menu(dictionary)
				break
			elif user_input == "2":
				render_line_graph(dictionary)
				nav_menu(dictionary)
				break
			elif user_input == "3":
				show_max_min_usage(dictionary, "max")
				nav_menu(dictionary)
				break
			elif user_input == "4":
				show_max_min_usage(dictionary, "min")
				nav_menu(dictionary)
				break
			elif user_input == "5":
				print(f"Average usage per day: {show_average_per_day(dictionary):.3f} {dictionary[0]['units']}")
				nav_menu(dictionary)
				break
			elif user_input == "exit" or user_input == "q":
				sys.exit("Bye bye")


if __name__ == "__main__":
	main()
