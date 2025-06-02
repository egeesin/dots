#!/bin/bash
# vim:set ft=sh

INPUTXML="/Volumes/ege-wd/audio/music/_library/Library.xml"
OUTPUTXML="$HOME/Desktop"

if [[ ! -f "$INPUTXML" ]]; then
	echo "Library.xml not found in current music library."
	echo "Please do this steps:"
	echo "File > Library > Export Library…"
	echo "then choose the library location. ex.(.../music/_library)"
	exit 0
fi

cp $INPUTXML "$OUTPUTXML"/Library.xml
sed -i -e 's/file\:\/\/\/Volumes\/ege-wd\/audio/file\:\/\/localhost\/C\:\/Users\/ege_e\/Music/g' "$OUTPUTXML"/Library.xml
rm "$OUTPUTXML"/Library.xml-e
# file://localhost/C:/Users/ege_e/Music
# file\:\/\/localhost\/C\:\/Users\/ege_e\/Music
