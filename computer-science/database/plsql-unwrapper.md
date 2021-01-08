### reference
- https://github.com/DarkAngelStrike/UnwrapperPLSQL check the release note
- http://blog.teusink.net/2010/04/unwrapping-oracle-plsql-with-unwrappy.html
- https://www.salvis.com/blog/2015/05/17/introducing-plsql-unwrapper-for-sql-developer/

### code
```python
#!/usr/bin/python
#
# This script unwraps Oracle wrapped plb packages, does not support 9g
# Contact: niels at teusink net / blog.teusink.net
#
# License: Public domain
#
import re
import base64
import zlib
import sys

# simple substitution table
charmap = [0x3d, 0x65, 0x85, 0xb3, 0x18, 0xdb, 0xe2, 0x87, 0xf1, 0x52, 0xab, 0x63, 0x4b, 0xb5, 0xa0, 0x5f, 0x7d, 0x68, 0x7b, 0x9b, 0x24, 0xc2, 0x28, 0x67, 0x8a, 0xde, 0xa4, 0x26, 0x1e, 0x03, 0xeb, 0x17, 0x6f, 0x34, 0x3e, 0x7a, 0x3f, 0xd2, 0xa9, 0x6a, 0x0f, 0xe9, 0x35, 0x56, 0x1f, 0xb1, 0x4d, 0x10, 0x78, 0xd9, 0x75, 0xf6, 0xbc, 0x41, 0x04, 0x81, 0x61, 0x06, 0xf9, 0xad, 0xd6, 0xd5, 0x29, 0x7e, 0x86, 0x9e, 0x79, 0xe5, 0x05, 0xba, 0x84, 0xcc, 0x6e, 0x27, 0x8e, 0xb0, 0x5d, 0xa8, 0xf3, 0x9f, 0xd0, 0xa2, 0x71, 0xb8, 0x58, 0xdd, 0x2c, 0x38, 0x99, 0x4c, 0x48, 0x07, 0x55, 0xe4, 0x53, 0x8c, 0x46, 0xb6, 0x2d, 0xa5, 0xaf, 0x32, 0x22, 0x40, 0xdc, 0x50, 0xc3, 0xa1, 0x25, 0x8b, 0x9c, 0x16, 0x60, 0x5c, 0xcf, 0xfd, 0x0c, 0x98, 0x1c, 0xd4, 0x37, 0x6d, 0x3c, 0x3a, 0x30, 0xe8, 0x6c, 0x31, 0x47, 0xf5, 0x33, 0xda, 0x43, 0xc8, 0xe3, 0x5e, 0x19, 0x94, 0xec, 0xe6, 0xa3, 0x95, 0x14, 0xe0, 0x9d, 0x64, 0xfa, 0x59, 0x15, 0xc5, 0x2f, 0xca, 0xbb, 0x0b, 0xdf, 0xf2, 0x97, 0xbf, 0x0a, 0x76, 0xb4, 0x49, 0x44, 0x5a, 0x1d, 0xf0, 0x00, 0x96, 0x21, 0x80, 0x7f, 0x1a, 0x82, 0x39, 0x4f, 0xc1, 0xa7, 0xd7, 0x0d, 0xd1, 0xd8, 0xff, 0x13, 0x93, 0x70, 0xee, 0x5b, 0xef, 0xbe, 0x09, 0xb9, 0x77, 0x72, 0xe7, 0xb2, 0x54, 0xb7, 0x2a, 0xc7, 0x73, 0x90, 0x66, 0x20, 0x0e, 0x51, 0xed, 0xf8, 0x7c, 0x8f, 0x2e, 0xf4, 0x12, 0xc6, 0x2b, 0x83, 0xcd, 0xac, 0xcb, 0x3b, 0xc4, 0x4e, 0xc0, 0x69, 0x36, 0x62, 0x02, 0xae, 0x88, 0xfc, 0xaa, 0x42, 0x08, 0xa6, 0x45, 0x57, 0xd3, 0x9a, 0xbd, 0xe1, 0x23, 0x8d, 0x92, 0x4a, 0x11, 0x89, 0x74, 0x6b, 0x91, 0xfb, 0xfe, 0xc9, 0x01, 0xea, 0x1b, 0xf7, 0xce]

def decode_base64_package(base64str):
    base64dec = base64.decodestring(base64str)[20:] # we strip the first 20 chars (SHA1 hash, I don't bother checking it at the moment)
    decoded = ''
    for byte in range(0, len(base64dec)):
        decoded += chr(charmap[ord(base64dec[byte])])
    return zlib.decompress(decoded)


sys.stderr.write("=== Oracle 10g/11g PL/SQL unwrapper 0.2 - by Niels Teusink - blog.teusink.net ===\n\n" )
if len(sys.argv) < 2:
    sys.stderr.write("Usage: %s infile.plb [outfile]\n" % sys.argv[0])
    sys.exit(1)

infile = open(sys.argv[1])
outfile = None
if len(sys.argv) == 3:
    outfile = open(sys.argv[2], 'w')

lines = infile.readlines()
for i in range(0, len(lines)):
    # this is really naive parsing, but works on every package I've thrown at it
    matches = re.compile(r"^[0-9a-f]+ ([0-9a-f]+)$").match(lines[i])
    if matches:
        base64len = int(matches.groups()[0], 16)
        base64str = ''
        j = 0
        while len(base64str) < base64len:
            j+=1
            base64str += lines[i+j]
        base64str = base64str.replace("\n","")
        if outfile:
            # 注意需要转为utf8
            outfile.write(decode_base64_package(base64str) + "\n")
        else:
            print decode_base64_package(base64str).decode('utf=8', 'ignore')
```
#### java version
```java
import java.io.IOException;
import java.security.NoSuchAlgorithmException;
import java.util.Arrays;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.zip.DataFormatException;

public class Unwrapper {
  private static int[] charmap = new int[]{61, 101, 133, 179, 24, 219, 226, 135, 241, 82, 171, 99, 75, 181, 160, 95, 125, 104, 123, 155, 36, 194, 40, 103, 138, 222, 164, 38, 30, 3, 235, 23, 111, 52, 62, 122, 63, 210, 169, 106, 15, 233, 53, 86, 31, 177, 77, 16, 120, 217, 117, 246, 188, 65, 4, 129, 97, 6, 249, 173, 214, 213, 41, 126, 134, 158, 121, 229, 5, 186, 132, 204, 110, 39, 142, 176, 93, 168, 243, 159, 208, 162, 113, 184, 88, 221, 44, 56, 153, 76, 72, 7, 85, 228, 83, 140, 70, 182, 45, 165, 175, 50, 34, 64, 220, 80, 195, 161, 37, 139, 156, 22, 96, 92, 207, 253, 12, 152, 28, 212, 55, 109, 60, 58, 48, 232, 108, 49, 71, 245, 51, 218, 67, 200, 227, 94, 25, 148, 236, 230, 163, 149, 20, 224, 157, 100, 250, 89, 21, 197, 47, 202, 187, 11, 223, 242, 151, 191, 10, 118, 180, 73, 68, 90, 29, 240, 0, 150, 33, 128, 127, 26, 130, 57, 79, 193, 167, 215, 13, 209, 216, 255, 19, 147, 112, 238, 91, 239, 190, 9, 185, 119, 114, 231, 178, 84, 183, 42, 199, 115, 144, 102, 32, 14, 81, 237, 248, 124, 143, 46, 244, 18, 198, 43, 131, 205, 172, 203, 59, 196, 78, 192, 105, 54, 98, 2, 174, 136, 252, 170, 66, 8, 166, 69, 87, 211, 154, 189, 225, 35, 141, 146, 74, 17, 137, 116, 107, 145, 251, 254, 201, 1, 234, 27, 247, 206};

  public static String unwrap(String wrapped) throws DataFormatException, IOException, NoSuchAlgorithmException {
    String wrappedUnix = wrapped.replace("\r\n", "\n");
    Pattern lengthPattern = Pattern.compile("([\n][0-9a-f]+[ ])([0-9a-f]+[\n])");
    Matcher m = lengthPattern.matcher(wrappedUnix);
    if (!m.find(0)) {
      throw new RuntimeException("Could not unwrap this code. Most probably it was not wrapped with the Oracle 10g, 11g or 12c wrap utility.");
    } else {
      int encodedCodeLength = Integer.parseInt(m.group(2).trim(), 16);
      int expectedLength = m.end() + encodedCodeLength;
      if (expectedLength > wrappedUnix.length()) {
        throw new RuntimeException("Wrapped code seems to be truncated. Expected length of " + expectedLength + " characters but got only " + wrappedUnix.length() + ".");
      } else {
        String encoded = wrappedUnix.substring(m.end(), expectedLength);
        byte[] decoded = Base64Coder.decodeLines(encoded);
        byte[] remapped = new byte[decoded.length];

        for(int i = 0; i < decoded.length; ++i) {
          int unsignedInteger = decoded[i] & 255;
          remapped[i] = (byte)charmap[unsignedInteger];
        }

        byte[] hash = Arrays.copyOfRange(remapped, 0, 20);
        byte[] zipped = Arrays.copyOfRange(remapped, 20, remapped.length);
        byte[] calculatedHash = HashCalculator.getSHA1(zipped);
        if (!Arrays.equals(hash, calculatedHash)) {
          throw new RuntimeException("SHA-1 hash values do not match. Expected '" + HashCalculator.bytesToHex(hash) + "' but got '" + HashCalculator.bytesToHex(calculatedHash) + "'. Cannot unwrap code.");
        } else {
          byte[] unzipped = Unzipper.unzip(zipped);

          int size;
          for(size = unzipped.length; size > 0 && unzipped[size - 1] == 0; --size) {
          }

          return new String(unzipped, 0, size);
        }
      }
    }
  }
}
```

