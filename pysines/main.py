"""
    The main script file to launch the pysines application
"""
import sys
import argparse

import os
import numpy as np
import matplotlib.pyplot as plt

def check_options(options):
    """
    Check that the options are sane and restricted to the project specs
    :param options: An `argparse.Namespace` object
    :return:
    """

def create_parser():
    """
    Create the Argument Parser for this script
    :return:  An `argparse.ArgumentParser` instance
    """
    parser = argparse.ArgumentParser('pysines', description="")
    parser.add_argument('-f', '--file', help="A file to save")
    
    return parser

def parse_args(args):
    """
    Perform the actual argument parsing, useful for testing the parser
    :param args: The list of arguments to parse, something like `sys.argv`
    :return: An `argparse.Namespace` object
    """
    parser = create_parser()
    return parser.parse_args(args)

def run(options):
    """
    Run the actual script
    :param options: An `argparse.Namespace` object
    :return:
    """

    # Do some additional check on the options
    check_options(options)
   
    num = options.num
    filename = options.file
    
    time = np.linspace(0, 6 * np.pi)
    data = np.empty([num,len(time)])    
    
    for x in range(num):
        data[x,:] = (x+1)*np.sin(time+x)
        plt.plot(time, data[x])
    
    plt.xlabel('Time')
    plt.ylabel('Data')

    if filename:
        plt.savefig(os.path.join(os.getcwd(), filename))

    pass

if __name__ == '__main__':
    # Script has been launched

    parser = create_parser()
    options = parser.parse_args()
    run(options)