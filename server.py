from flask import Flask,request,render_template
import pickle
file=open("./Diamond_Price_Prediction_model.pkl",'rb')
model=pickle.load(file)
print()
app = Flask(__name__,template_folder="./htmls")

@app.route("/", methods=["GET"])
def root():
    return render_template('Index.html')

@app.route("/predict", methods=["POST"])
def predict_salary():
    try:
        # ['Ideal' 'Premium' 'Good' 'Very Good' 'Fair']
        # ['E' 'I' 'J' 'H' 'F' 'G' 'D']
        # ['SI2' 'SI1' 'VS1' 'VS2' 'VVS2' 'VVS1' 'I1' 'IF']
        carat=request.form.get("Carat")
        color = request.form.get("Color")
        cut = request.form.get("Cut")
        clarity = request.form.get("Clarity")
        depth = request.form.get("Depth")
        table = request.form.get("Table")
        x = request.form.get("X")
        y = request.form.get("Y")
        z = request.form.get("Z")
        price = model.predict([[carat, cut, color, clarity, depth, table, x, y, z]])[0]
        price=round(price)
    except:
        return render_template("error.html")
    return render_template("predict.html",price=price,cut=['Ideal', 'Premium' ,'Good' ,'Very Good' ,'Fair'][int(cut)],carat=carat,color=['E' ,'I' ,'J' ,'H' ,'F' ,'G' ,'D'][int(color)],clarity=['SI2' ,'SI1' ,'VS1' ,'VS2' ,'VVS2' ,'VVS1' ,'I1' ,'IF'][int(clarity)],depth=depth,table=table,x=x,y=y,z=z)

app.run(host="0.0.0.0")
