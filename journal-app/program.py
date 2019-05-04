import journal


def main():
    print_header()
    run_event_loop()


def print_header():
    print("-------------------")
    print("     JOURNAL APP")
    print("-------------------")


def run_event_loop():
    print("What do you want to do with your journal?")

    selection = None
    # journal_data = list()
    name = 'journal_file'
    journal_file = journal.load(name)

    while selection != 'x':
        selection = input("[L]ist entries, [A]dd an entry, E[x]it: ").lower()
        if selection == 'l':
            journal.list_entries(journal_file)
        elif selection == 'a':
            journal.add_entry(journal_file)
        elif selection != 'x':
            print("Invalid selection. Try again!")
    print("Goodbye!")
    journal.save(name, journal_file)


# print(__file__)
# print(__name__)

if __name__ == '__main__':
    main()
