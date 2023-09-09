from flask import Flask, request, jsonify
import datetime as dt
import pytz

app= Flask(__name__)

@app.route("/get-info", methods =["GET"])
def get_info():
    slack_name= request.args.get("slack_name")
    track= request.args.get("track")
    day_of_the_week= dt.datetime.today().strftime("%A")
    utc_now = dt.datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    github_file_url = "https://github.com/username/repo/blob/main/file_name.ext"
    source_code_url = "https://github.com/your_username/your_repo"

    response ={
        "slack_name": slack_name,
        "current_day": day_of_the_week,
        "current_utc_time": utc_now,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": source_code_url,
        "status_code": 200


    }
    return jsonify(response)




if __name__=="__main__":
    app.run(debug=True)