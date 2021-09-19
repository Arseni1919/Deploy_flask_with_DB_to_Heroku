from app import db

result = db.session.execute('select * from feedback;')

for index, item in enumerate(result):
    print(f'{index} - (id: {item.id}) {item.customer}: {item.comments}')