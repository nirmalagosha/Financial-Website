from flask import Flask,render_template,redirect,url_for,request,logging
import csv
app=Flask('__name__')
@app.route('/')
def home():
    return render_template('index1.html')
@app.route('/results',methods=['GET','POST'])
def result():
    if request.method=='POST':
        query=str(request.form['Query'])
        print(query)
        query=query.lower()
        read='C:/Users/govardhan/Desktop/ThemeBased/'+query+".csv"
        df=open(read)
        df1=csv.reader(df)
        loss=query+"loss.png"
        profit=query+"profit.png"
        max1=query+"max.png"
         
        return render_template('show.html',show1=df1,tit=query,loss=loss,profit=profit,max1=max1)
    return render_template('index1.html')
if __name__=='__main__':
    app.run(debug=True)