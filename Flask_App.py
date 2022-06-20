from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
        "ID": 1,
        "Name": "Sanit Arya",
        "Contact": 8877665544,
        "Done": False
    },

    {
        "ID": 2,
        "Name": "Harshit Raj",
        "Contact": 8765432190,
        "Done": False
    }
]


@app.route('/')
def Welcome():
    return "Welcome to Flask."


@app.route("/add-data", methods=["POST"])
def Add_Task():
    if not request.json:
        return jsonify({
            "Status": "Error !!!",
            "Message": "Please provide us the data..."
        }, 400)

    task = {
        "ID": tasks[-1]["ID"] + 1,
        "Name": request.json["Name"],
        "Contact": request.json.get("Contact", ""),
        "Done": False
    }
    tasks.append(task)
    return jsonify({
        "Status": "Success.",
        "Message": "Task added successfully....."
    })


@app.route("/get-data")
def Get_Task():
    return jsonify({
        "Data": tasks
    })


if __name__ == "__main__":
    app.run(debug=True)
