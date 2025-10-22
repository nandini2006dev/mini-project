# Class Timetable Generator (User-defined)
def generate_timetable():
    print("📘 CLASS TIMETABLE GENERATOR 📘")
    print("----------------------------------")

    # Get basic info
    days = int(input("Enter number of working days in a week: "))
    periods = int(input("Enter number of periods per day: "))

    day_names = []
    for i in range(days):
        name = input(f"Enter name of day {i+1}: ")
        day_names.append(name.capitalize())

    # Get subjects
    subject_count = int(input("\nEnter number of subjects: "))
    subjects = []
    for i in range(subject_count):
        sub = input(f"Enter subject {i+1} name: ")
        subjects.append(sub.title())

    print("\nNow, let's assign subjects for each day and period.\n")

    timetable = {}

    for day in day_names:
        print(f"\n--- {day} ---")
        timetable[day] = []
        for p in range(periods):
            print(f"Available subjects: {', '.join(subjects)}")
            subject = input(f"Enter subject for Period {p+1}: ")
            timetable[day].append(subject.title())

    # Display timetable
    print("\n📅 FINAL CLASS TIMETABLE 📅")
    print("-" * (15 + periods * 15))
    print(f"{'Day':<15}", end="")
    for p in range(periods):
        print(f"Period {p+1:<10}", end="")
    print()
    print("-" * (15 + periods * 15))

    for day in day_names:
        print(f"{day:<15}", end="")
        for sub in timetable[day]:
            print(f"{sub:<15}", end="")
        print()
    print("-" * (15 + periods * 15))


# Run program
generate_timetable()