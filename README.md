# IncognitoInteract

IncognitoInteract is a Flask-based web application that utilizes the Advanced Encryption Standard (AES) algorithm developed by the National Institute of Standards and Technology (NIST) for secure text encryption and decryption.
[Demo Link](https://incognitointeract.onrender.com/)

## How it Works

Users can input a plain text message and a password, which will be encrypted using AES. The resulting cipher text can then be shared with intended recipients. To decrypt the message, recipients input the cipher text along with the password provided by the sender.

## Requirements

Ensure you have Python 3.11 installed on your system. Install the required dependencies using:

` pip install -r requirements.txt `


## Usage

1. Clone the repository:

` git clone https://github.com/your-username/IncognitoInteract.git `


2. Navigate to the project directory:

` cd IncognitoInteract `


3. Create and activate a virtual environment:

` python3 -m venv venv `


- On Windows:

` venv\Scripts\activate `


- On macOS and Linux:

` source venv/bin/activate `


4. Run the Flask application:

` python app.py `


5. Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to access the application.

## Demo Screenshots
![image](https://github.com/Amar985/IncognitoInteract/assets/84828275/c1a0349c-38cc-4d93-b7d1-37fde2cb560e)



## About AES

AES (Advanced Encryption Standard) is a symmetric encryption algorithm adopted by NIST. It operates on fixed-size blocks of data and uses keys of 128, 192, or 256 bits. AES is widely used for secure communication and data protection due to its efficiency and robust security features.

## Disclaimer

While AES encryption offers strong security, it's important to note that the security of encrypted data also depends on the strength of the password used. Always use strong, unique passwords to ensure maximum security.

---

Feel free to contribute to this project by submitting pull requests or reporting any issues you encounter. For further assistance or inquiries, contact the project maintainers.
