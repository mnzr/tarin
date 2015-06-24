import os
import stat
import tarfile
import click
import subprocess


# :-1 because by default returns of
# shell commands had a new line
user = subprocess.check_output(['whoami'])
homebin = "/home/" + user[:-1] + "/bin/"


def extract(app):
    """Simple function to extract files
    :param app: The name of the file to be extracted
    :rtype : str
    """
    if app.endswith("tar.bz2"):
        tar = tarfile.open(app)
        tar.extractall(homebin)
        tar.close()
        print("Extracted in" + homebin + app.split(".")[0])
    else:
        print(app + " is not a tar file -_-")
    return 1


def executable(app):
    """
    TO find out the executable file in the extracted folder
    """
    address = homebin + app.split(".")[0].replace(' ', "\ ")
    exe = stat.S_IEXEC
    for filename in os.listdir(address):
        st = os.stat(filename)
        mode = st.st_mode
        if mode & exe and os.path.isfile(filename):
            print filename


@click.command()
@click.option('--app', help='Name of your app without tar.gz or tar.bz2 file.')
def main(app):
    """


    :return:
    """
    # print(subprocess.check_output(['whoami'], shell=True))
    # app = app.replace(' ', "\ ")
    # print(app)
    extract(app)
    executable(app)

    return 0


if __name__ == '__main__':
    main()
