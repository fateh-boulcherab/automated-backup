# 📦 Automated Server Backup Script

This script allows system administrators to automate server or workstation directory backups. It supports configurable source directories, backup retention, logging, and works on both **Linux** and **Windows** systems.

---

## 📁 Files

| File         | Description                             |
|--------------|-----------------------------------------|
| `backup.py`  | Main Python script to perform backups   |
| `config.json`| Configuration file (paths and limits)   |
| `README.md`  | This documentation                      |

---

## 📥 Cloning the Project

1. **Clone the project into your server or local machine**  
   Open terminal (or Git Bash / PowerShell on Windows), and run:

   ```bash
   git clone git@github.com:fateh-boulcherab/automated-backup.git
   cd automated-backup
   ```

---

## ⚙️ Configuration (`config.json`)

Edit the `config.json` file to specify your source directories, backup destination, and the maximum number of backup folders to retain.

### 📝 Example:

#### ✅ **Linux**
```json
{
  "source_dirs": ["/etc", "/var/log"],
  "backup_dir": "/home/username/backups",
  "max_backups": 5
}
```

#### ✅ **Windows**
```json
{
  "source_dirs": ["C:/Users/YourName/Documents", "D:/Projects"],
  "backup_dir": "C:/Backups",
  "max_backups": 3
}
```

### 🧩 Fields:
- `source_dirs`: List of full absolute paths to folders you want to back up.
- `backup_dir`: Destination folder where backups will be stored.
- `max_backups`: Maximum number of backup folders to keep. Older ones are deleted automatically.

---

## 🚀 How to Run

Open a terminal or command prompt and run:

```bash
python backup.py
```

The script will:
- Create a timestamped backup folder
- Copy specified directories
- Log the process to `backup.log`
- Prune old backups beyond `max_backups`

---

## 🗓 Scheduling the Script

### 🪟 Windows (Using Task Scheduler)

1. Open **Task Scheduler**
2. Click **Create Basic Task**
3. Name your task (e.g., "DailyBackup")
4. Choose a trigger (e.g., Daily, Weekly)
5. Select **Start a program**
6. Program/script:  
   ```
   python
   ```
   Add arguments:  
   ```
   C:\path\to\backup.py
   ```
   Start in (optional):  
   ```
   C:\path\to\
   ```
7. Finish and test the task.

> ✅ Ensure Python is added to your system PATH.

---

### 🐧 Linux (Using cron)

1. Open crontab:
   ```bash
   crontab -e
   ```

2. Add this line to run the backup daily at 2 AM:
   ```
   0 2 * * * /usr/bin/python3 /path/to/backup.py
   ```

> Replace `/usr/bin/python3` with the output of `which python3`, and `/path/to/backup.py` with the actual path to your script.

---

## 📝 Logs

Logs are saved to:
```
<backup_dir>/backup.log
```

Each run includes:
- Success and error messages
- Deleted backups
- Timestamp of operation

---

## 🔒 Permissions

Ensure the user running the script has **read access** to all `source_dirs` and **write access** to the `backup_dir`.

---

## 💡 Tips

- Run the script manually first to verify configuration.
- Test with small folders before production use.
- Use absolute paths in `config.json` to avoid issues.
