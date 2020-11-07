# Image Steganography

Encryption - hides an image in another image

Decryption - takes encrypted image to produce original images

## Dependencies

- Python OpenCV

```pip3 install opencv-python```

- Numpy

```pip3 install numpy```

## Usage

### Encryption

```
$: chmod +x encrypt.py

$: ./encrypt.py <file1> <file2> (<name>)
```

Where <file1> and <file2> are images in the source folder (img/)

Creates file ```<name>.png``` in destination folder (encrypt/). If name not given, default is ```output.png```

### Decryption

```
$: chmod +x decrypt.py

$: ./decrypt.py <filename> (<name>)
```

Where <filename> is an image in source folder (encrypt/)
  
Creates files ```<name>1.png``` and ```<name>2.png``` in destination folder (decrypt/) if name given.

If name not given, default is ```output1.png``` and ```output2.png```
