## rohde-schwarz-tools
simple tools for linux users to control r&amp;s

## extract.py - .set - png extractor

R&S spectrum anaylzer like FSH4 / FSH8 can save settings and screenshot's in .set files.
extract.py is a simple python3 script to extract the png's.
Extracting the settings is in progress..

## Requirements
* python3 notify2

## Installation

	sudo pip3 install notify2

## RSconvert.sh

	use it as a nautilus script and convert .set files with right click!
	* copy the script to </home/$USER/.local/share/nautilus/scripts/>
	* chmod +x /home/$USER/.local/share/nautilus/scripts/RSconvert.sh
