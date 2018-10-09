for FILE in "$@"; do
	python3 /home/$USER/.local/share/nautilus/scripts/extract.py "$FILE"
done
