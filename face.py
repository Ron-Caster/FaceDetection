from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html>
    <head>
        <title>Drag and Drop File</title>
        <style>
            #dropzone {
                width: 300px;
                height: 200px;
                border: 2px dashed #ccc;
                text-align: center;
                padding: 50px;
                font-size: 20px;
            }
        </style>
    </head>
    <body>
        <div id="dropzone">Drop files here</div>

        <script>
            var dropzone = document.getElementById('dropzone');

            dropzone.addEventListener('dragover', function(e) {
                e.preventDefault();
                dropzone.style.backgroundColor = 'lightblue';
            });

            dropzone.addEventListener('dragleave', function(e) {
                e.preventDefault();
                dropzone.style.backgroundColor = '';
            });

            dropzone.addEventListener('drop', function(e) {
                e.preventDefault();
                dropzone.style.backgroundColor = '';

                var file = e.dataTransfer.files[0];
                var formData = new FormData();
                formData.append('file', file);

                var xhr = new XMLHttpRequest();
                xhr.open('POST', '/upload', true);
                xhr.onload = function() {
                    if (xhr.status === 200) {
                        console.log('File uploaded successfully.');
                    } else {
                        console.log('Error uploading file.');
                    }
                };
                xhr.send(formData);
            });
        </script>
    </body>
    </html>
    '''

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save(os.path.join(os.getcwd(), file.filename))
    return 'File uploaded successfully.'

if __name__ == '__main__':
    app.run()
