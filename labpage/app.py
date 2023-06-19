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
