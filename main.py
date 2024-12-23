from flask import Flask, render_template, request, jsonify, redirect,url_for,flash,session
import pyrebase
from config import config


app = Flask(__name__)
app.secret_key = "Addyourownsecretkey"


firebase = pyrebase.initialize_app(config)

auth = firebase.auth()


@app.route("/login", methods =['POST','GET'])
def loginUser():
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
    
    try:
      user = auth.sign_in_with_email_and_password(email,password)
      id_token = auth.get_account_info(user['idToken'])
      session['id_token'] = id_token
      print(id_token)
      
      flash('User logged in',"success")
      return render_template("home.html")
    
    except Exception as e:
      error_message = str(e)
      if "INVALID_LOGIN_CREDENTIALS" in error_message:  # Firebase error code for email in use
        flash("Invalid credentia", "error")
      else:
        flash("An error occurred during registration: " + error_message, "error")
    
  
  return render_template("login.html")
  
@app.route("/register", methods=['POST', 'GET'])
def addUser():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password == confirm_password:
            try:
                # Attempt to create a new user
                user = auth.create_user_with_email_and_password(email, password)
                print(user)
            
            except Exception as e:
                # Handle the specific case of email already in use
                error_message = str(e)
                if "EMAIL_EXISTS" in error_message:  # Firebase error code for email in use
                    flash("This email is already registered", "error")
                else:
                    flash("An error occurred during registration: " + error_message, "error")
        else:
            flash("Passwords don't match. Please try again.", "error")
    
    return render_template("register.html")  # Ensure you have a registration page template


@app.route('/resetPassword', methods = ['POST','GET'])
def resetPassword():
  id_token = session.get('id_token')
  email = id_token['users'][0]['email'] # accesses first user in the list and the attribute email
  print(email)

  auth.send_password_reset_email(email)
  
  return render_template("home.html")

@app.route('/logout')
def logout():
  session.pop('id_token', None)  # Remove the ID token or session data
  return redirect(url_for('loginUser'))

if __name__ == "__main__":
  app.run(debug=True)
