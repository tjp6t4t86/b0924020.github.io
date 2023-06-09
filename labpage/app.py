from flask import Flask, request, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def process_form():
    form_data = {
        'fname': request.form.get('fname'),
        'lname': request.form.get('lname'),
        'comment': request.form.get('comment'),
        'method': request.form.get('method'),
    }
    
    # Save form data as JSON
    with open('form_data.json', 'w') as file:
        json.dump(form_data, file)
    
    # Save cropped image
    if 'croppedImage' in request.files:
        cropped_image = request.files['croppedImage']
        cropped_image.save('cropped_image.jpg')
    
    return json.dumps({'status': 'success'})

if __name__ == '__main__':
    app.run()
