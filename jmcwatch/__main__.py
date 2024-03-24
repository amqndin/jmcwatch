import time
import click
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

jmc_files = ['.jmc', '.hjmc', 'jmc.txt', 'jmc_config.json']

class JMCWatchdog(FileSystemEventHandler):

	def __init__(self):
		self.compilation_needed = False

	def on_any_event(self, event):
		if not self.compilation_needed and any(jmc_file in event.src_path for jmc_file in jmc_files):
			compile_result = subprocess.run('jmc compile',capture_output=True,text=True,shell=True)
			print(compile_result.stdout)
			self.compilation_needed = True


@click.command()
def main():
	"""Look for changes in jmc related files and compile them.\n
	To use simply type `jmcwatch` in the directory of your JMC project\n
	JMCWatch is made by amandin. (discord handle)"""
	event_handler = JMCWatchdog()
	observer = Observer()
	observer.schedule(event_handler, ".", recursive=True)
	observer.start()
	try:
		while True:
			time.sleep(1)
			event_handler.compilation_needed = False
	except KeyboardInterrupt:
		observer.stop()
	observer.join()


if __name__ == "__main__":
	main()
