students = {}

while True:
    print("\n=== Student Grade Calculator ===")
    print("1. Add a student")
    print("2. Show student report")
    print("3. Show class average")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        name = input("Enter student name: ")
        scores = []

        print("Enter scores one at a time.")
        print("Type 'done' when finished.")

        while True:
            score = input("Score: ")

            if score.lower() == "done":
                break

            try:
                score = float(score)

                if score < 0 or score > 100:
                    print("Please enter a score between 0 and 100.")
                else:
                    scores.append(score)

            except ValueError:
                print("Please enter a valid number.")

        if len(scores) == 0:
            print("No scores were entered.")
        else:
            average = sum(scores) / len(scores)

            if average >= 90:
                letter = "A"
            elif average >= 80:
                letter = "B"
            elif average >= 70:
                letter = "C"
            elif average >= 60:
                letter = "D"
            else:
                letter = "F"

            students[name] = {
                "scores": scores,
                "average": average,
                "letter": letter
            }

            print(f"\n{name}'s average: {average:.2f}")
            print(f"Letter grade: {letter}")

    elif choice == "2":
        if len(students) == 0:
            print("No students have been added yet.")
        else:
            print("\n=== Student Report ===")

            for name, information in students.items():
                print(f"{name}: Average = {information['average']:.2f}, Grade = {information['letter']}")

    elif choice == "3":
        if len(students) == 0:
            print("No students have been added yet.")
        else:
            total = 0

            for information in students.values():
                total += information["average"]

            class_average = total / len(students)

            print(f"\nClass average: {class_average:.2f}")

    elif choice == "4":
        print("Thanks for using the Student Grade Calculator!")
        break

    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")
