from flask import Flask, render_template, request
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/", defaults={'fileName': "file1.txt"}, methods=["GET"])
@app.route("/<fileName>",methods=["GET"])
def getText(fileName):
    try:
        if request.method == 'GET':
            if fileName != 'file4.txt':
                text_file = open("assets/documents/"+fileName, "r")
                lines = (text_file.read().replace('\t', ' ')).split('\n')
                
                startLine = request.args.get('start', default = None, type = int)
                endLine = request.args.get('end', default = None, type = int)
                lines1 = []
                if (isinstance(startLine, int) == True and startLine != None) and (isinstance(endLine, int) == True and endLine != None):
                    lines1 = lines[startLine:endLine+1]
                elif (isinstance(startLine, int) == True and startLine != None) and (isinstance(endLine, int) == False and endLine == None):
                    lines1 = lines[startLine:]
                elif (isinstance(startLine, int) == False and startLine == None) and (isinstance(endLine, int) == True and endLine != None):
                    lines1 = lines[:endLine+1]
                else:
                    lines1 = lines
                return render_template("display.html", filename = fileName, textLines1 = lines1, isStatic = False)
            else:
                text_file1 = open("assets/documents/"+fileName, "r", encoding="utf-16")
                text = text_file1.read()
                soup = BeautifulSoup(text, features="html.parser")
                return render_template("display.html", filename = fileName, textLines1 = soup.get_text(), isStatic = True)
        else:
            return render_template("404.html")
    except Exception as e:
        return render_template("500.html", error = str(e))

if __name__ == "__main__":
    app.run(debug=True)