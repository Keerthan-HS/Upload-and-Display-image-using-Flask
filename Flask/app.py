import os
from flask import Flask,render_template,request,send_from_directory

app = Flask(__name__)  

app_route = os.path.dirname(os.path.abspath(__file__))   #Gives the path of current directory 

@app.route('/')   #Index root
def index():
    return render_template('index.html')

@app.route('/upload',methods=['POST'])  #Post route to upload image
def upload():
    target = os.path.join(app_route,"images/")   #Makes the path to insert new uploads
    # print(target+'12377')

    if not os.path.isdir(target):
        os.mkdir(target)   #If there is no image directory it creates one

    for file in request.files.getlist('files'):    
        # print(file)
        filename = file.filename    #gets the filename of uploaded image
        destination = ''.join([target,filename])     #Joins the filename with the path eg: D:\Python\images\pic.jpg
        # print(destination)
        file.save(destination)   #Saves the image to the directory 
        return render_template('image.html',image_name=filename)   #renders the filename to the html file
        # return destination


@app.route('/upload/<filename>')
def send_image(filename):   #Kind of a middleware to send image to the html file
    return send_from_directory('images',filename)

if __name__ == "__main__":
    app.run(debug=True)
