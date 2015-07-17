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
    if options.filename and os.path.exists(options.filename):
        print "The file {} already exists, overwriting...".format(options.filename)

def create_parser():
    """
    Create the Argument Parser for this script
    :return:  An `argparse.ArgumentParser` instance
    """
    parser = argparse.ArgumentParser('pysines', description="")
    parser.add_argument('-n', '--num', type=int, default=1, help="(Optional) The number of sines to plot.  Must be an integer")
    parser.add_argument('-f', '--file', dest='filename', help="(Optional) A file to save the figure")
    return parser

def run(options):
    """
    Run the actual script
    :param options: An `argparse.Namespace` object
    :return:
    """

    # Do some additional check on the options
    check_options(options)
   
    num = options.num
    filename = options.filename
    
    time = np.linspace(0, 6 * np.pi, 500)

    data = np.zeros([num,len(time)])    
    
    for x in range(num):
        data[x,:] = (x+1)*np.sin(time+x)
        plt.plot(time, data[x])
    
    plt.xlabel('Time')
    plt.ylabel('Data')
    plt.title('PySines')
    if filename:
        plt.savefig(os.path.join(os.getcwd(), filename))

    plt.show()

if __name__ == '__main__':
    # Script has been launched

    parser = create_parser()
    options = parser.parse_args()
    run(options)