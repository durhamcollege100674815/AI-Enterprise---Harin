from flask import Flask
from flask_restful import Resource, Api, reqparse
app = Flask(__name__)
api = Api(app)

STUDENTS = {
  '1': {'first_name': 'harin','last_name': 'shah', 'amount_due': 2300, 'DOB': '28-08-1992'},
  '2': {'first_name': 'sidd','last_name': 'Shah', 'amount_due': 2500, 'DOB': '28-3-1990'},
  '3': {'first_name': 'raj','last_name': 'Patel', 'amount_due': 4000, 'DOB': '23-11-1992'},
}
parser = reqparse.RequestParser()

class StudentsList(Resource):
    def get(self):
        return STUDENTS

    def post(self):
        parser.add_argument("first_name")
        parser.add_argument("last_name")
        parser.add_argument("amount_due")
        parser.add_argument("DOB")
        args = parser.parse_args()
        student_id = int(max(STUDENTS.keys())) + 1
        student_id = '%i' % student_id
        STUDENTS[student_id] = {
            "first_name": args["first_name"],
            "last_name": args["last_name"],
            "amount_due": args["amount_due"],
            "DOB": args["DOB"],
        }
        return STUDENTS[student_id], 201

class Student(Resource):
    def get(self, student_id):
        if student_id not in STUDENTS:
            return "Not found", 404
        else:
            return STUDENTS[student_id]

    def put(self, student_id):
        parser.add_argument("first_name")
        parser.add_argument("last_name")
        parser.add_argument("amount_due")
        parser.add_argument("DOB")
        args = parser.parse_args()
        if student_id not in STUDENTS:
            return "Record not found", 404
        else:
            student = STUDENTS[student_id]
            student["first_name"] = args["first_name"] if args["first_name"] is not None else student["first_name"]
            student["last_name"] = args["last_name"] if args["last_name"] is not None else student["last_name"]
            student["amount_due"] = args["amount_due"] if args["amount_due"] is not None else student["amount_due"]
            student["DOB"] = args["DOB"] if args["DOB"] is not None else student["DOB"]
            return student, 200
        
    def delete(self, student_id):
        if student_id not in STUDENTS:
            return "Not found", 404
        else:
            del STUDENTS[student_id]
        
        return '', 204

api.add_resource(StudentsList, '/students/')
api.add_resource(Student, '/students/<student_id>')
if __name__ == "_main_":
    app.run(debug=False)