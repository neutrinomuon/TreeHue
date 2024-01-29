linux-32
linux-64
linux-aarch64
linux-armv6l
linux-armv7l
linux-ppc64
linux-ppc64le
linux-s390x
osx-64
osx-arm64
win-32
win-64
win-arm64


# Mac OS
shasum -a 256 file

# Linux
sha256sum /path/to/your/file

# Windows
Get-FileHash -Algorithm SHA256 "C:Path\To\Your\File" | Select-Object -ExpandProperty Hash

# Python script to find the sha256 code
import hashlib

filename = "/path/to/your/file"

with open(filename, "rb") as f:
    sha256_hash = hashlib.sha256()
    # Read and update hash string value in blocks of 4K
    for byte_block in iter(lambda: f.read(4096), b""):
        sha256_hash.update(byte_block)

print(sha256_hash.hexdigest())
