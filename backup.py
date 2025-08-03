import os
import shutil
import json
import logging
from datetime import datetime

CONFIG_FILE = 'config.json'

def load_config():
    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)

def setup_logging(log_path):
    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s'
    )

def create_backup_folder(base_path):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = os.path.join(base_path, f"backup_{timestamp}")
    os.makedirs(backup_path, exist_ok=True)
    return backup_path

def perform_backup(source_dirs, backup_path):
    for src in source_dirs:
        if not os.path.exists(src):
            logging.error(f"Source directory does not exist: {src}")
            continue
        try:
            folder_name = os.path.basename(os.path.normpath(src))
            dst = os.path.join(backup_path, folder_name)
            shutil.copytree(src, dst)
            logging.info(f"Backed up {src} to {dst}")
        except Exception as e:
            logging.error(f"Error backing up {src}: {e}")

def manage_old_backups(backup_dir, max_backups):
    backups = sorted(
        [os.path.join(backup_dir, d) for d in os.listdir(backup_dir) if d.startswith("backup_")],
        key=os.path.getctime
    )
    while len(backups) > max_backups:
        oldest = backups.pop(0)
        try:
            shutil.rmtree(oldest)
            logging.info(f"Deleted old backup: {oldest}")
        except Exception as e:
            logging.error(f"Failed to delete old backup {oldest}: {e}")

def main():
    config = load_config()
    source_dirs = config['source_dirs']
    backup_dir = config['backup_dir']
    max_backups = config.get('max_backups', 5)

    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    log_path = os.path.join(backup_dir, 'backup.log')
    setup_logging(log_path)

    logging.info("Starting backup process.")
    backup_path = create_backup_folder(backup_dir)
    perform_backup(source_dirs, backup_path)
    manage_old_backups(backup_dir, max_backups)
    logging.info("Backup process completed.")

if __name__ == '__main__':
    main()
