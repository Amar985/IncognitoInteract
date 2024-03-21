from flask import Flask, render_template, request, send_from_directory


from encryption_decryption import encrypt, decrypt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

@app.route('/encrypt', methods=['POST'])
def encrypt_text():
    try:
        input_text = request.form['input_text']
        password = request.form['password']
        encrypted_text = encrypt(input_text, password)
        return encrypted_text.decode()
    except Exception as e:
        return "Sorry! Invalid Input"


@app.route('/decrypt', methods=['POST'])
def decrypt_text():
    try:
        input_text = request.form['input_text']
        password = request.form['password']
        decrypted_text = decrypt(input_text.encode(), password)
        return decrypted_text
    except Exception as e:
        return "Sorry! Invalid Input"

if __name__ == '__main__':
    app.run(debug=False)
