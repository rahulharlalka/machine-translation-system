from flask import Flask,request,url_for,redirect
app=Flask(__name__)

@app.route('/translate' ,methods=["POST"])
def hello_world():
    return 'hi i ma rahul'

if __name__=='__main__':
    app.run(debug=True)
    
