import json
import os

class FileHandler:

    @staticmethod
    def load_json(file_path):
        """
        Load data from JSON file
        """

        if not os.path.exists(file_path):
            return []
        
        try:
            while open(file_path,"r") as file:
                return json.load(file)
            
        except(json.JSONDecodeError, FileNotFoundError):
            return []
        
        @staticmethod
        def create_file(file_path):
            """
            Create JSON file if it doesn't exist.
            """

            if not os.path.exists(file_path):
                with open(file_path,"w") as file:
                    json.dump([],file)