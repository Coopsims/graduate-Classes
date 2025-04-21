# main.py
import argparse
import pandas as pd
import numpy as np
from program.autompg import AutoMPGData

def my_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("log", type=str,
                        help="Name of log file my_log.log (folder path)")
    parser.add_argument("save", type=str,
                        help="Store output in data folder path")
    parser.add_argument("-y", "--year", action="store_true",
                        help="Sort data by model_year")
    parser.add_argument("-m", "--mpg", action="store_true",
                        help="Sort data by mpg")
    return parser

if __name__ == "__main__":
    parser = my_parser()
    args = parser.parse_args()

    # Create AutoMPGData object (with logging folder path, sorting booleans)
    auto_data = AutoMPGData(
        sort_year=args.year,
        sort_mpg=args.mpg,
        log_path=args.log
    )

    # Sort the data, if needed
    auto_data.sort_data()

    # Save the data file appropriately
    auto_data.save_data(args.save)