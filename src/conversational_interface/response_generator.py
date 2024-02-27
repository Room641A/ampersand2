import ipywidgets as widgets
from IPython.display import display
from src.data_analytics import input_preprocessing

def accept_spreadsheet_ui():
    file_path_input = widgets.Text(placeholder='Enter file path')
    process_button = widgets.Button(description='Process')

    def on_process_button_click(b):
        file_path = file_path_input.value
        input_preprocessing.process_spreadsheet(file_path)  # Call backend function

    process_button.on_click(on_process_button_click)

    display(file_path_input, process_button)
