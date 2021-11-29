from noise.connection import NoiseConnection
import typer
import base64

def main(protocol_name: str = "Noise_NN_25519_ChaChaPoly_SHA256"):
    proto = NoiseConnection.from_name(protocol_name.encode())
    proto.set_as_responder()
    proto.start_handshake()

    handshake = input("Received handshake (enter here): ").strip()
    proto.read_message(base64.b64decode(handshake.encode()))

    print("Handshake response (send this):", base64.b64encode(proto.write_message()).decode())

    while True:
        encrypted_message = input("\t Message to decrypt (enter here): ").strip()
        print("Received message:", proto.decrypt(base64.b64decode(encrypted_message.encode())).decode())

        plaintext_message = input("Message to encrypt: ").strip()
        print("\t Encrypted message (send this):", base64.b64encode(proto.encrypt(plaintext_message.encode())).decode())


if __name__ == "__main__":
    typer.run(main)

