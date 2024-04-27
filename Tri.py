from pathlib import Path

dirs = {
	# Images
	".png": "Images",
	".jpeg": "Images",
	".jpg": "Images",
	".gif": "Images",
	# Vidéos
	".mp4": "Videos",
	".mov": "Videos",
	# Archives
	".zip": "Archives",
	# Documents
	".pdf": "Documents",
	".txt": "Documents",
	".json": "Documents",
	#Musiques
	".mp3": "Musiques",
	".wav": "Musiques",
}

tri_dir = Path.home() / "Tri"
files = [f fof f in tri_dir.iterdir() if .isfile()]
for f in files:
	output_dir = tri_dir / dirs.get(f.suffix, "Autres")
	output_dir.mkdir(exist_ok=True)
	f.rename(output_dir / f.name)