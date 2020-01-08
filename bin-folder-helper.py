import os

home_dir = os.environ['HOME']
bin_dir = home_dir + '/.bin'
string = 'PATH=$PATH:' + bin_dir

# check to see if folder $HOME/.bin exists, if not, create one
if os.path.isdir(bin_dir):
    print(bin_dir + ' exists!')
else:
    try:
        os.mkdir(bin_dir)
    except OSError:
        print(bin_dir + ' does not exist and cannot be created.  There was an error.')
    else:
        print(bin_dir + ' was created because it did not already exist.')

# check to see if the bin_dir is added to $PATH via adding it in .bashrc
# if it is not it will ask if you would like to add it.
with open(home_dir + '/.bashrc') as f:
    if string in f.read():
        print(bin_dir + ' is added to $PATH in .bashrc')
    else:
        answer = input(bin_dir + ' has not been added to $PATH. Would you like to add it? y/n\n')
        if answer == 'y' or 'Y':
            with open(home_dir + '/.bashrc', 'a') as bashrc_file:
                bashrc_file.write(string)
        else:
            pass
