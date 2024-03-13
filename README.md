# pyhashcat

`pyhashcat` is an updated Python C API binding to `libhashcat` for interfacing with hashcat version 6.2.6. This project builds upon the efforts of previous contributors @Rich5, @initiate6, and @f0cker, extending compatibility to Python 3.8 and beyond.

## Original Contributions:
- [@Rich5](https://github.com/Rich5/pyhashcat)
- [@initiate6](https://github.com/initiate6/pyhashcat)
- [@f0cker](https://github.com/f0cker/pyhashcat)

This repository serves as a working directory aimed at porting and fixing compatibility issues from Python 3.7 and hashcat 6.1.x to Python 3.8+ and hashcat 6.2.6.

### Prerequisites:
- hashcat 6.2.6
- Python 3.8+

### Installation Steps:

1. **Clone this repository:**
   ```sh
   git clone https://github.com/michael2to3/pyhashcat.git
   cd pyhashcat/pyhashcat
   ```

2. **Clone and prepare hashcat:**
   ```sh
   git clone https://github.com/hashcat/hashcat.git
   cd hashcat/
   git checkout tags/v6.2.6
   sudo make install_library
   sudo make install
   cd ..
   ```

3. **Build pyhashcat with specific directories:**
   Before proceeding with the build and installation of `pyhashcat`, ensure that the LZMA SDK is installed on your system, as it is required for successful compilation.
   
   Execute the following command, adjusting paths as necessary for your environment:
   ```sh
   HC_SOURCES_DIR='hashcat/' HC_LIB_DIR=/usr/lib python setup.py build_ext -I /usr/share/lzma-sdk/C/
   ```

4. **Install pyhashcat:**
   ```sh
   sudo python setup.py install
   ```

### Testing the Installation:

To verify that `pyhashcat` has been installed correctly and is functional, you can run a simple test script included in the repository:

```sh
python simple_mask.py
```

This script will execute a basic mask attack using `pyhashcat` and display the results.

### Environment Variables for Custom Paths

If `hashcat` or `python` was not found during installation, try setting the `HC_PATH` and `PY_PATH` environment variables to specify custom paths. For example:

- **For Arch Linux:**
  ```sh
  export HC_PATH='/usr/share/hashcat/' PY_PATH='/usr/bin/'
  ```

- **For Other (adjust paths as needed):**
  ```sh
  export HC_PATH='/path/to/hashcat' PY_PATH='/path/to/python'
  ```

These variables allow `pyhashcat` to locate your `hashcat` and `python` installations if they are not in standard locations.

### Additional Help:

For more information on using `pyhashcat`, including its API and functionalities, refer to the help documentation within Python:

```python
import pyhashcat
help(pyhashcat)
```
