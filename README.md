## noise-cli
This is a dead-simple, secure wrapper around the Noise protocol for secure E2E communication.
If you don't believe me, read the code (it's very short at 48 lines of code!).

```
❯ wc -l *.py
  23 initiator.py
  25 responder.py
  48 total
```

`noise-cli` supports emojis and most unicode (excluding certain whitespace characters, such as `\n`).

## Installing deps
```
pip install -r requirements.txt
```
or 
```
poetry install
```

## Usage
To initiate a message, just run: ```python initiator.py```
If you're recieving a message, run: ```python responder.py```
Follow the prompts to establish a secure channel over mediums like SMS and Discord.

## Example usage
Suppose you have the following conversation with someone:
```
me: scandalous secret message
other: wow we should keep this convo secret
me: haha yeah thank god we're using noise-cli
other: yep
```

With `noise-cli`, the conversation would look like (from the initiator's perspective):
```
❯ python initiator.py
Handshake (send this): NuNLd17tzFRj/ugNq/m4YejELXW70PdjCqjOMPCvb24=
Handshake response (enter here):  H5mqb3KCYSs3cjmaIuXmhsS0vEi+vls10XtB8m50b0z9i3Byb7/d7GmCB/ooyI9j
Secure channel established!

Message to encrypt (enter here): scandalous secret message
         Encrypted message (send this): TGPg++DVNIYyaeY/WJtNyYYBOim3WbQeIFAwxi2bXblkmONdux/5F+s=
         Response to decrypt: 0XzOnaGPcHtXacEtBM3Boytd6h/y14/Qq+L76qDFMVn2SJIsdY8hg7AyOPHx5mtwxsSdLg==
Received message: wow we should keep this convo secret
Message to encrypt (enter here): haha yeah thank god we're using noise-cli
         Encrypted message (send this): mmn6+ZuUoOeG0AizDH7/FX2QlMGrl0xmt8IxnDWpDahZSBibrrXXHIY/TX0VXZN2Qk/hyTcYRcz7
         Response to decrypt: GvI8fdLTVq89f7oIqUk1sh9dlw==
Received message: yep
```

From the responder's perspective, the conversation would look like:
```
❯ python responder.py
Received handshake (enter here): NuNLd17tzFRj/ugNq/m4YejELXW70PdjCqjOMPCvb24=
Handshake response (send this): H5mqb3KCYSs3cjmaIuXmhsS0vEi+vls10XtB8m50b0z9i3Byb7/d7GmCB/ooyI9j
Secure channel established (once you send the handshake response)!

         Message to decrypt (enter here): TGPg++DVNIYyaeY/WJtNyYYBOim3WbQeIFAwxi2bXblkmONdux/5F+s=
Received message: scandalous secret message
Response to encrypt: wow we should keep this convo secret
         Encrypted message (send this): 0XzOnaGPcHtXacEtBM3Boytd6h/y14/Qq+L76qDFMVn2SJIsdY8hg7AyOPHx5mtwxsSdLg==
         Message to decrypt (enter here):  mmn6+ZuUoOeG0AizDH7/FX2QlMGrl0xmt8IxnDWpDahZSBibrrXXHIY/TX0VXZN2Qk/hyTcYRcz7
Received message: haha yeah thank god we're using noise-cli
Response to encrypt: yep
         Encrypted message (send this): GvI8fdLTVq89f7oIqUk1sh9dlw==
```

From an eavesdropper's perspective, the exchange would look like:
```
initiator: NuNLd17tzFRj/ugNq/m4YejELXW70PdjCqjOMPCvb24=
responder: H5mqb3KCYSs3cjmaIuXmhsS0vEi+vls10XtB8m50b0z9i3Byb7/d7GmCB/ooyI9j
initiator: TGPg++DVNIYyaeY/WJtNyYYBOim3WbQeIFAwxi2bXblkmONdux/5F+s=
responder: 0XzOnaGPcHtXacEtBM3Boytd6h/y14/Qq+L76qDFMVn2SJIsdY8hg7AyOPHx5mtwxsSdLg==
initiator: mmn6+ZuUoOeG0AizDH7/FX2QlMGrl0xmt8IxnDWpDahZSBibrrXXHIY/TX0VXZN2Qk/hyTcYRcz7
responder: GvI8fdLTVq89f7oIqUk1sh9dlw==
```
(in other words, it'd look like properly encrypted gibberish!)
