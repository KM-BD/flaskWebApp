from flask import Flask, request, render_template, redirect, url_for
import re
import bleach

app = Flask(__name__)

# OWASP Proactive Control C5: Validate All Inputs
def is_xss_attack(input_string):
    sanitized = bleach.clean(input_string, strip=True)
    return sanitized != input_string

def is_sql_injection(input_string):
    sql_injection_pattern = re.compile(r'(\bSELECT\b|\bINSERT\b|\bUPDATE\b|\bDELETE\b|\bDROP\b)', re.IGNORECASE)
    return sql_injection_pattern.search(input_string) is not None

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        search_term = request.form['search_term']
        if is_xss_attack(search_term):
            return render_template('index.html', error="XSS attack detected. Please enter a valid search term.")
        if is_sql_injection(search_term):
            return render_template('index.html', error="SQL injection detected. Please enter a valid search term.")
        sanitized_term = bleach.clean(search_term)
        return redirect(url_for('result', search_term=sanitized_term))
    return render_template('index.html')

@app.route('/result')
def result():
    search_term = request.args.get('search_term')
    return render_template('result.html', search_term=search_term)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
