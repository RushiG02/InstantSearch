
from flask import Flask, jsonify, request
import pickle
import time
app = Flask(__name__)



@app.route('/process_search')
def gen_search_json():
    try:
        namesData = open('./processData/namesData.pkl', 'rb')
        prefix_data = pickle.load(namesData)
        st_time = time.time()
        query = request.args.get("q", '').strip().lower()
        if not query or len(query) < 3:
            resp = jsonify({"message": "Invalid Query parameter", "results": []}), 400 
        else:
            matched_terms = prefix_data.get(query, [])
            if len(matched_terms) == 0:
                resp = jsonify({"message":"No results found", "results":[]}),404
            else:
                res = sorted(matched_terms, key=lambda x: len(x))
                results = [{"name": name} for name in res[:10]] 
                resp = jsonify({"message": "Data found","results": results}), 200      

        time_taken = (time.time() - st_time)
        print(time_taken)
        resp[0].headers['Access-Control-Allow-Origin'] = '*'
        return resp
    except Exception as e:
        resp = jsonify({"message": "error: "+str(e),"results":[]}),500
        resp[0].headers['Access-Control-Allow-Origin'] = '*'
        return resp

if __name__ == "__main__":
    app.run(port=8080, debug=True)