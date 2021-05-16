# Batch-Add-Text-to-Images
Add Text to Images (Only work on Mac OS)

### Limitation:
+ Only work on Mac OS (Preview.app)
+ Cannot add Chinese/Korean/Japanese charactors to images

### Prerequisites：
+ Python3
  + opencv-python
  + os
  + time
  + json

### Tutorial:
1. Download the source code from GitHub
2. Install all requirements such like ```pip3 install -r requirements.txt```
3. Run the Main.py such like ```python3 Main.py```
4. Input 1 to manually set the config in console, here are 2 confusing arguments:
    + font['bold'] thickness of the fonts
    + font['align] text align
      + 1=align left
      + 2=aligh center
      + 3=aligh right
      + 4=align center of the whole image
5. When you are in Preview.app, you can press ⬆️⬇️⬅️➡️ to edit the position of the text. "=" and "-" key are to control the size of the text. "+" and "_" are to control the thickness of the text. Press any other key to save the setting.
