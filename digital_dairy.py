
import datetime

def add_entry():
    with open("diary.txt", "a") as file:
        date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        entry = input("Write your diary entry:\n")
        file.write("\n" + date + "\n")
        file.write(entry + "\n")
        file.write("-" * 40)
    print("✅ Diary entry saved successfully!")

def read_entries():
    try:
        with open("diary.txt", "r") as file:
            content = file.read()
            if content.strip() == "":
                print("📭 No diary entries found.")
            else:
                print("\n📖 Your Diary Entries:")
                print(content)
    except FileNotFoundError:
        print("❌ Diary file not found.")

def main():
    while True:
        print("\n===== DIGITAL DIARY =====")
        print("1. Add New Entry")
        print("2. Read Diary")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            read_entries()
        elif choice == "3":
            print("👋 Thank you for using Digital Diary!")
            break
        else:
            print("⚠️ Invalid choice! Please try again.")

main()
