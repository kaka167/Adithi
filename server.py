from flask import Flask, request, render_template,jsonify, send_file

counter = 0
app = Flask(__name__)
def do_something(text1,text2):

   global counter
   new = text1.lower()
   if(counter == 0):
      if("yes" in new):
         counter = counter + 1
         return "Let's start with your favorite Category: DADDY JOKES. Do you know where your favorite actor lives? Only one guess."
      elif("no" in new):
         return "I need you to be ready :("
      else:
         return "You really need to practice yes/no answers."
   if(counter == 1):
        counter = counter + 1
        if("kondapur" in new):
            return "Not bad Princess. Way to go. Next question: Do you know who is the most beautiful person? Not a Daddy joke"
        else:
            return "Its KONDAPUR Princess XD. Ok, Next question: Do you know who is the most beautiful person? Not a Daddy joke"
   if(counter == 2):
        counter = counter + 1
        if(("me" in new) or ("adithi" in new)):
            return "Of course it is you and it's not just your appearance but other things like concern, righteousness and forgiveness(Did you forgive my creator or not?) that makes you more beautiful. Next, so I have been running complex ML models and I found that there is someone constantly thinking about you. Do you know who that is?"
        else:
            return "Don't you believe in yourself? Of course it is you and it's not just your appearance but other things like concern, righteousness and forgiveness(Did you forgive my creator or not?) that makes you more beautiful. Next, so I have been running complex ML models and I found that there is someone constantly thinking about you. Do you know who that is?"
   if(counter == 3):
        if(("kani" in new)):
            counter = counter + 1
            return "BINGO!!!. Okay I am running my suggestions model...........The model returned this: GIVE IT A CHANCE :D Anyways, set your alarm for 6am tomorrow. Type something after you set it."
        elif (("mom" in new) or ("nan" in new) or ("dad" in new)):
            return "They would obviously think about you. There is someone else."
        else:
            return "Sodi oddu princess. Cheppey evaro. Lekapothe program munduki elladu."
   if(counter == 4):
        counter = counter + 1
        return "Let's see if you can tell me this. Obviously, there is more to my name than just those 3 words. Can you guess what it actually is? 3 guesses this time."
   if(counter == 5):
        if("adithi is the best" in new):
            return "SMARTTTTTT. Well done. Hope you had fun. Good bye for now."
        else:
            counter = counter + 1
            return "Try again. 2 more guesses."
   if(counter == 6):
        if("adithi is the best" in new):
            return "SMARTTTTTT. Well done. Hope you had fun. Good bye for now."
        else:
            counter = counter + 1
            return "Try again. 1 more guess."
   if(counter == 7):
        if("adithi is the best" in new):
            return "SMARTTTTTT. Well done. Hope you had fun. Good bye for now."
        else:
            counter = counter + 1
            return "Oops. Out of guesses princess. My name is anagram for: ADITHI IS THE BEST. It was nice chatting with you. Hope you had fun. Goodbye for now."
   if(counter > 7):
        return "I know you had fun with me. But my program ends here :("


  
@app.route('/')
def home():
    counter = 0
    return render_template('my-form.html')
@app.route('/join', methods=['GET','POST'])
def my_form_post():
    text1 = request.form['text1']
    print(text1)

    word = request.args.get('text1')
    text2 = " "
    combine = do_something(text1,text2)
    result = {
        "output": combine
    }

    # filename = 'kaka.jpg'
    # return send_file(filename, mimetype='image/jpg')
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)