import json

class DataMigrator:
    def __init__(self, config_file):
        self.config = self.load_config(config_file)

    def load_config(self, config_file):
        with open(config_file, 'r') as f:
            return json.load(f)

    def extract(self):
        # Logique pour extraire des données des systèmes hérités
        pass

    def transform(self, data):
        # Logique pour transformer les données
        pass

    def load(self, data):
        # Logique pour charger les données dans la nouvelle base de données
        pass

    def migrate(self):
        data = self.extract()
        transformed_data = self.transform(data)
        self.load(transformed_data)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python migrate.py <config_file>")
        sys.exit(1)
    
    config_file = sys.argv[1]
    migrator = DataMigrator(config_file)
    migrator.migrate()