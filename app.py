from flask import Flask, request, render_template
from stories import story

app=Flask(__name__)

@app.route('/')
def index():
    prompts=story.prompts
    return render_template('form.html',prompts=prompts)

@app.route('/story', methods=['POST'])
def display_story():
    story_text=story.generate(request.form)
    return render_template('story.html',story=story_text)

if __name__ == '__main__':
    app.run(debug=True)