import csv
from collections import defaultdict

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_transactions(self):
        """
        Read the CSV using the standard library and groups items by (Member_number, Date).
        Return a list of lists, where each inner list is a transaction.
        Example: [['milk', 'bread'], ['soda'], ...]
        """
        # Dictionary to group items: 
        # Key = (Member_ID, Date), Value = [item1, item2...]
        grouped_data = defaultdict(list)

        try:
            with open(self.file_path, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                
                for row in reader:
                    # strip whitespace
                    member = row['Member_number'].strip()
                    date = row['Date'].strip()
                    item = row['itemDescription'].strip()
                    
                    # Create a unique key for this shopping trip
                    key = (member, date)
                    
                    # Add item to the specific transaction
                    grouped_data[key].append(item)
            
            return list(grouped_data.values())

        except FileNotFoundError:
            print(f"Error: File {self.file_path} not found.")
            return []
        except Exception as e:
            print(f"An error occurred loading data: {e}")
            return []