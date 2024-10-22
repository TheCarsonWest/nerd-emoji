## [[Handling Binary Files]] in Python

### What is Binary [[File Handling]]?
Binary file handling involves working with files that contain non-textual data, such as images, videos, audio, or executable files. Unlike text files, binary files store data in raw binary form, consisting of sequences of 0s and 1s.

### How to Use Binary [[File Handling]]
Python provides the `open()` function for handling binary files. The `mode` parameter of `open()` should be set to 'rb' for reading binary files and 'wb' for writing binary files.

**Reading Binary Files:**

```python
with open("binary_file.bin", "rb") as f:
 data = f.read()
```

* The `open()` function takes the file name and mode as arguments.
* The `with` statement ensures the file is automatically closed after use.
* `f.read()` reads the entire contents of the binary file into a bytearray.

**Writing Binary Files:**

```python
with open("binary_file.bin", "wb") as f:
 f.write(data)
```

* The `open()` function takes the file name and mode as arguments.
* The `with` statement ensures the file is automatically closed after use.
* `f.write()` writes the data bytearray to the binary file.

### Code Examples
**Reading a Binary Image (JPEG):**

```python
with open("image.jpg", "rb") as f:
 image_data = f.read()
 # Process the image data using external libraries or display methods
```

**Writing a Binary Audio File (WAV):**

```python
import wave

# Create a WAV object
wav_file = wave.open("audio.wav", "wb")

# Set audio parameters
wav_file.setframerate(44100)
wav_file.setnchannels(2)
wav_file.setsampwidth(2)

# Write binary data to WAV file
wav_file.writeframes(audio_data)
wav_file.close()
```

### Related Python Concepts
- [[File Handling]]: Binary file handling is an extension of general file handling in Python.
- [[File IO Modes]]: The 'rb' and 'wb' modes are used specifically for binary file handling.
- [[Bytes and Bytearrays]]: Binary data is stored in bytearrays, which contain sequences of 0s and 1s.
- [[Streams]]: Binary file handling often involves working with streams of data as opposed to specific characters.
- [[Images, Videos, and Audio]]: Binary files commonly store data for these multimedia types.
# [[Python 1 Home]]