from pathlib import Path
files = [f.name for f in Path('.').iterdir() if f.is_file()]
print(files)