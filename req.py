import requests

r = requests.get('http://localhost:5551/api/leaderboard', json={
"class_id": 2, 
"student_id": 1
})

students = r.json()
for student in students:
    if student.get('points') > 10:
        print(student.get('name'))