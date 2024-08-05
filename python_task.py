records = [
    "Андрей 9",
    "Василий 11",
    "Роман 7",
    "X Æ A-12 45",
    "Иван Петров 3",
    "Андрей 6",
    "Роман 11"
]


def calculate_statistics(records):
    statistics = {}
    for record in records:
        person, _, worktime = record.rpartition(" ")
        if person in statistics:
            person_worktime, worktime_sum = statistics[person]
            statistics[person] = (f"{person_worktime}, {worktime}", worktime_sum + int(worktime))
            continue
        statistics[person] = (worktime, int(worktime))
    for key, value in statistics.items():
        worktime, worktime_sum = value
        print(f"{key}: {worktime}; Сумма часов: {worktime_sum}")


calculate_statistics(records)
