# Batch-Add-Text-to-Images
Add Text to Images (Only work on Mac OS)

### Limitation:
+ Only work on Mac OS
+ Cannot add Chinese/Korean/Japanese charactors to images

### Features:
+ Add different text to the template (My purpose is to add names on certificates)
+ Generate new files and the filenames are the text

### Prerequisites：
+ Python3
  + opencv-python
  + os
  + time
  + json

### Tutorial:
1. Download the source code from GitHub
2. Install all requirements such like ```pip3 install -r requirements.txt```
3. Create ```namelist.txt``` file in the local directory with one text in one line
4. Run the Main.py such like ```python3 Main.py```
5. Input 1 to manually set the config in console, here are 2 confusing arguments:
    + font['bold'] thickness of the fonts
    + font['align] text align
      + 1=align left
      + 2=aligh center
      + 3=aligh right
      + 4=align center of the whole image
6. When you are in Preview.app, you can press ⬆️⬇️⬅️➡️ to edit the position of the text. "=" and "-" key are to control the size of the text. "+" and "_" are to control the thickness of the text. Press any other key to save the setting.
