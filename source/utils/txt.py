def save_txt(text: str, folder_name: str, file_name: str):
    with open(f"data/{folder_name}/{file_name}.txt", "w") as file:
        file.write(text)


def read_txt(folder_name: str, file_name: str):
    with open(f"data/{folder_name}/{file_name}.txt", "r") as file:
        return file.read()
