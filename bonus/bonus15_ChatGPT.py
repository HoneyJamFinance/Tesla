import PySimpleGUI as sg
import zipfile

# Create the layout for the GUI
layout = [[sg.Text('Select the file to zip:'), sg.FileBrowse()],
          [sg.Text('Enter the name of the zip file:'), sg.InputText()],
          [sg.Text('Select the destination for the zip file:'), sg.FolderBrowse()],
          [sg.Button('Create Zip'), sg.Button('Cancel')]]

# Create the window
window = sg.Window('Zip File Creator', layout)

# Run the event loop to process events and get the values of the inputs
while True:
    event, values = window.read()

    # If the 'Create Zip' button is clicked, create the zip file
    if event == 'Create Zip':
        with zipfile.ZipFile(values[2] + '/' + values[1], 'w') as myzip:
            myzip.write(values[0])
        sg.popup('Zip file created successfully!')
        break

    # If the 'Cancel' button is clicked or the window is closed, exit the event loop
    if event in (None, 'Cancel'):
        break

# Close the window
window.close()
