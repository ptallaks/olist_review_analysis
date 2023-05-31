import os
import pandas as pd
##"/Users/dhelq/code/ptallaks/data-context-and-setup/data/csv"

class Olist:
    def get_data(self):
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrames loaded from csv files
        """
        # Hints 1: Build csv_path as "absolute path" in order to call this method from anywhere.
            # Do not hardcode your path as it only works on your machine ('Users/username/code...')
            # Use __file__ instead as an absolute path anchor independant of your usename
            # Make extensive use of `breakpoint()` to investigate what `__file__` variable is really
        # Hint 2: Use os.path library to construct path independent of Mac vs. Unix vs. Windows specificities
        print(__file__)
        folder = os.path.split(__file__)[0]
        folder2 = os.path.split(folder)[0]
        #folder3 = os.join(folder2 ,'data', 'csv')

        csv_path = os.path.join(folder2, "data", 'csv')
        filedir = os.listdir(csv_path)
        file_names = []
        for file in filedir:
            if file.endswith('csv'):
                file_names.append(file)
            else:
                pass

        key_names = []


        for index in range(len(file_names)):
            key_names.append(file_names[index].replace("_dataset.csv", "").replace("olist_","").replace(".csv", ""))
        data = {}

        for name, file  in zip(key_names, file_names):
            data[name] = pd.read_csv(os.path.join(csv_path,(file)))
        return data

    def ping(self):
        """
        You call ping I print pong.
        """
        print("pong")
