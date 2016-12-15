from flask import Flask, render_template, request
import geocoder

app = Flask('wtf')
app.config['GEOPOSITION_GOOGLE_MAPS_API_KEY'] = "AIzaSyDpSuC8-WknSvKKTSVGXhvmguMXOR4HnaY"


def geocode(endereco):
    g = geocoder.google(endereco)
    print(endereco)
    print(g.latlng)


@app.route("/", methods=['GET','POST'])
def hello_world():
    if request.method == 'POST':
        result = request.form['addressInput']
        geocode(result)
        return render_template("maplocation.html", endereco=result)


app.run(debug=True)
