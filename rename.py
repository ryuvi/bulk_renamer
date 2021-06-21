#!/usr/bin/env python3

# Imports
import os
import glob
import re
import PySimpleGUI as psg

# Script Body

theme = 'Black'

# Variables
themes_list = psg.theme_list()
numbers = re.compile(r'(\d+)') # Regex to get the index of the file?
themes_layout = [
    [psg.Text("Choose a theme")],
    [psg.Listbox(values=psg.theme_list(),size=(20,12),key='-list-',enable_events=True)],
    [psg.Button('OK')]
]
layout = [
    [psg.Button('Themes')],
    [psg.Radio('Common', '-options-', key='-commom-', default=True), psg.Radio('Regex', '-options-', key='-regex-',default=False)],
    [psg.Text('Path to files')],
    [psg.Input(key="-folder_browse-", change_submits=True), psg.FolderBrowse()],
    [psg.Text('Common name for the files')],
    [psg.Input(key="-common_name-")],
    [psg.Text('Extension of the files')],
    [psg.Input("", key="-extension-")],
    [psg.Text("RegEx")],
    [psg.Input("Expression", key="-expression-"), psg.Input("Substituable", key="-subs-")],
    [psg.Button('Rename'), psg.Button('Cancel')],
    [psg.Output(size = (50, 5), key="-output-")]
]

# What the script does

def numericalSort(value): # Some function that i take from StackOverflow
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

def common_rename(path, common_name, extension):
    if extension != '' and common_name != '':
        for i, f in enumerate(sorted(os.listdir(path), key=numericalSort)): # For each file from the folder in the path
            index = '000'
            if i < 10:
                index = '00{}'.format(i)
            elif i >= 10 and i < 100:
                index = '0{}'.format(i)
            else:
                index = i
            f_new = '{0}-{1}.{2}'.format(common_name, index, extension) # New name of the file
            os.rename(path + '/' + f, path + '/' + f_new) # Rename the file to the new name
            print('{0}. {1} -> {2}'.format(i, f, f_new)) # Print the result in a beauty way
    
    elif extension == '' and common_name != '':
        for i, f in enumerate(sorted(os.listdir(path), key=numericalSort)): # For each file from the folder in the path
            actual_extension = f
            index = '000'
            if i < 10:
                index = '00{}'.format(i)
            elif i >= 10 and i < 100:
                index = '0{}'.format(i)
            else:
                index = i
            f_new = '{0}-{1}{2}'.format(common_name, index, re.sub('.+(?=\.)', '', actual_extension)) # New name of the file
            os.rename(path + '/' + f, path + '/' + f_new) # Rename the file to the new name
            print('{0}. {1} -> {2}'.format(i, f, f_new)) # Print the result in a beauty way
    
    else:
        for i, f in enumerate(sorted(os.listdir(path), key=numericalSort)): # For each file from the folder in the path
            actual_name = f
            f_new = '{0}.{1}'.format(re.sub('\.[^.]*$', '', actual_name), extension) # New name of the file
            os.rename(path + '/' + f, path + '/' + f_new) # Rename the file to the new name
            print('{0}. {1} -> {2}'.format(i, f, f_new)) # Print the result in a beauty way

def regex_rename(path, expression, substituable):
    for i, f in enumerate(sorted(os.listdir(path), key=numericalSort)):
        actual_extension = re.sub('.+(?=\.)', '', f)
        actual_name = re.sub('\.[^.]*$', '', f)
        f_new = '{0}.{1}'.format(re.sub(expression, substituable, actual_name), actual_extension)

window = psg.Window('Bulk Rename', layout, resizable=True)
theme_window = psg.Window('Themes', themes_layout)

_ = False

while True:
    psg.theme(theme)
    
    event,values = window.read()
    if event == psg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'Rename':
        if window['-commom-']:
            common_rename(values['-folder_browse-'], values['-common_name-'], values['-extension-'])
        elif window['-regex-']:
            regex_rename(values['-folder_browse-'], values['-expression-'], values['-subs-'])
        print('{0} {1} {0}'.format('='*10, 'END'))
    if event == 'Themes':
        _ = True

    while _:
        e,v = theme_window.read()

        if e == psg.WIN_CLOSED:
            break
        if e == 'OK':
            theme = v['-list-'][0]
            _ = False


window.close()

print(psg.Output())
