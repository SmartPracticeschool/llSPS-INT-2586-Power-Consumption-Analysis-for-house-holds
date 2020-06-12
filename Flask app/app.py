


from flask import Flask,render_template,request
app=Flask(__name__)
import pickle
model=pickle.load(open('voltage.pkl','rb'))

@app.route('/')
def helloworld():
    return render_template("index.html")
@app.route('/login',methods = ['POST'])
def admin():
    p= request.form["ga"]
    q= request.form["gr"]
    r= request.form["vo"]
    s= request.form["gi"]
    t= request.form["sb1"]
    u= request.form["sb2"]
    v= request.form["sb3"]

    
    a=[[float(p),float(q),float(r),float(s),float(t),float(u),float(v)]]
    y=model.predict(a)
    return render_template("index.html",y="The power consumed till now:"+str(y[0][0]))
@app.route('/user')
def user():
    return "welcome user"
if __name__=='__main__':
   app.run(debug= True)