"""
This is a journal module.
"""
import os


def list_entries(journal_data):
    print("Listing your journal entries...")
    reverse_entry = reversed(journal_data)
    for index, entry in enumerate(reverse_entry):
        print(f'[{index + 1}] {entry}')


def add_entry(journal_data):
    add_entry_to_journal = input("Type your entry, <enter> to exit: ")
    journal_data.append(add_entry_to_journal)
    print("Adding...")


def load(name):
    """
    This method creates and loads a new journal.

    :param name: The base name of the journal to load.
    :return: A new journal data structure populated with the file data.
    """
    data = list()
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as file_input:
            for entry in file_input.readlines():
                data.append(entry.rstrip())

    return data


def get_full_pathname(name):
    filename = os.path.abspath(os.path.join('journal/', name + '.jrl'))
    return filename


def save(name, journal_data):
    filename = get_full_pathname(name)
    print(f'Saving to: {filename}')

    with open(filename, 'w') as file_output:
        for entry in journal_data:
            file_output.write(entry + '\n')
