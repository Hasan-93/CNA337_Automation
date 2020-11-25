# This is the template code for the CNA337 Final Project
# Zachary Rubin, zrubin@rtc.edu
# CNA 337 Fall 2020

from Server import Server
def print_program_info():

    print("Server Automator v0.1 by Hasan")

if __name__ == '__main__':
    print_program_info()

    EC2server = Server('3.12.129.47')

    print(EC2server.ping())