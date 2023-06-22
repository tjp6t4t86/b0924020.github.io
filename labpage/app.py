from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/store_photo', methods=['POST'])
def store_photo():
    photo_data = request.json.get('photoData')

    # 处理照片数据，存储为文件等
    # 这里的示例将照片数据存储为 JPEG 文件
    with open('photo.jpg', 'wb') as file:
        file.write(photo_data)

    return '照片已成功存储'

if __name__ == '__main__':
    app.run()





from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/action_page.php', methods=['POST'])
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
