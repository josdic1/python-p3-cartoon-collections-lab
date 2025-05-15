import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

WATCH_PATH = "./lib"

class WatchHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print(f"\n🔁 File changed: {event.src_path}")
            subprocess.run(["clear"])
            subprocess.run(["pytest", "-x"])

if __name__ == "__main__":
    print(f"👀 Watching {WATCH_PATH} for changes...")
    event_handler = WatchHandler()
    observer = Observer()
    observer.schedule(event_handler, path=WATCH_PATH, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n🛑 Stopped watching.")

    observer.join()
