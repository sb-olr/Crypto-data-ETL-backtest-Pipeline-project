CONFIG = {
    'data_dir': 'data/',
    'csv_dir': 'data/csv/',
    'processed_dir': 'data/csv/processed/',
    'logs_dir': 'data/logs/',
    'db_file': 'TEST-crypto-db.sqlite3',
    'table_name': 'exchange_rates',
    'table_fields': ('cur_id TEXT', 'name TEXT', 'unit TEXT',
                     'value REAL', 'type TEXT', 'date TEXT'),
    'headers': ('cur_id', 'name', 'unit', 'value', 'type', 'date_dl'),
    'url': 'https://api.coingecko.com/api/v3/exchange_rates',
    'local_base_url': 'http://0.0.0.0:5000/api/view/',
    'local_json_file': 'demo.json'
}
