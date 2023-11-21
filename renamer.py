import os

def rename_files(source_folder, base_name, start_number=1, change_formats=False, new_format=".txt"):
    # Get a list of all files in the source folder
    files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

    # Rename files
    for i, file_name in enumerate(files, start=start_number):
        _, old_format = os.path.splitext(file_name)

        new_name = f"{base_name}_{i}{new_format}" if change_formats else f"{base_name}_{i}{old_format}"
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(source_folder, new_name)

        os.rename(source_path, destination_path)
        print(f"Renamed '{file_name}' to '{new_name}'.")

if __name__ == "__main__":
    # Specify the path to the folder you want to rename files in
    source_folder = "C:\\Users\\chaud\\Desktop\\random"

    # Specify the base name for the files
    base_name = "faraxel"

    # Specify the starting number for the files (optional, default is 1)
    start_number = 1

    # Specify whether to change the formats of the files (optional, default is False)
    change_formats = True

    # Specify the new format for the files (optional, used only if change_formats is True)
    new_format = ".csv"

    # Call the rename_files function
    rename_files(source_folder, base_name, start_number, change_formats, new_format)
