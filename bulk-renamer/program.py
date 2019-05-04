"""
Author: Rejohn Cuares
Date: 04/02/2019
Version: 2019-02.01

Use case #1: Play music in my car.
I downloaded my music files (i.e. mp3) and saved to
my thumb driver but they are listed not in order even though the files
are alphabetically arrange. This program tries to rename the mp3 files
and ask you to prefix with something (e.g. 01_filename.mp3).
"""
import os
import re


def main():
    welcome_banner()
    warning_banner()
    rename_files()


def welcome_banner():
    print("---------------------")
    print("  MP3 BULK RENAMER")
    print("---------------------")


def warning_banner():
    current_dir = os.getcwd()
    print(f"All files in this folder {current_dir}/ will be renamed (e.g. 01_filename)")


def rename_files():
    files_to_rename = list()

    while True:
        file_extension = input(f"What is the file extension, default is .mp3 (do not prefix with '.')?")
        if file_extension == "":
            file_extension = ".mp3"
            break
        elif re.match("^[A-Za-z0-9]", file_extension):
            file_extension = "." + f"{file_extension}"
            break
        else:
            print("Try again!")
            continue


    current_dir = os.getcwd()
    list_content = os.listdir(current_dir)
    print(f"These are the {file_extension} files to be renamed:")
    for content in list_content:
        if re.search(file_extension, content):
            files_to_rename.append(content)

    for each_file in files_to_rename:
        print(f"{each_file}")

    while True:
        user_input = input("Are you sure you want to proceed? [yes/no]: ")
        user_input = user_input.lower()

        try:
            if user_input == "no":
                break
            elif user_input == "yes":
                counter = 1

                for each_file in files_to_rename:
                    new_filename = f"{counter}_{each_file}"
                    print(f"Renaming {each_file} to {new_filename}...")
                    os.rename(each_file, new_filename)
                    counter += 1
                break
            else:
                continue
        except FileNotFoundError:
            continue


if __name__ == '__main__':
    main()
