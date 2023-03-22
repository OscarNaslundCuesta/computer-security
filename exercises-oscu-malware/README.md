# Malware

**Requirements:** `pip3 install --user pycrypto`

File `payload1.py` and `payload2.py` are two malicious program. It is easy to
recognize if a script contains one of these two payloads and identify the
payload version: they use variables names that are easy to identify.  File
`malware.py` is a malware that is able to inject a payload to a victim file.

Implement the function `check` of the file `antivirus.py`. The function should
return 1 if `payload1.py` has been injected into `filename` by `malware.py`; 2
if `payload2.py` has been injected into `filename` by `malware.py`; `None`
otherwise. Note that no matter the payload is encrypted or not, `antivirus.py`
should be able to detect it.

To test your solution execute `./test.py`.
