import os
import csv



class Migration:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    def __init__(self):
        pass

    def create_table(self, db_file: str, model):
        if not self.is_valid_file_path(db_file) or self.is_file_empty(db_file):
            with open(db_file, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(model.table_header)

    def drop_table(self):
        pass

    def add_record(self, db_file: str, model, record: dict):
        self.create_table(db_file, model)
        next_id = self.generate_next_id(db_file)

        with open(db_file, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([next_id] + list(record.values()))

    def is_valid_file_path(self, db_file: str):
        return os.path.exists(os.path.join(self.BASE_DIR, "db", db_file))

    def is_file_empty(self, db_file: str):
        return os.stat(os.path.join(self.BASE_DIR, "db", db_file)).st_size == 0

    def generate_next_id(self, db_file: str):
        with open(db_file, 'r') as database:
            reader = csv.reader(database)
            next(reader, None)
            rows = list(reader)
            if rows:
                return int(rows[-1][0]) + 1
            else:
                return 1
