from main import main

def testing():
    assert main("25 de agosto de 2023", "31 de dezembro de 2025") == 856
    assert main("10 de janeiro de 2024", "15 de fevereiro de 2024") == 36
