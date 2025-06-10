from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.task import Task
from models.user import User
from models import db
import urllib.parse

# 1️⃣ SQLite Source DB
sqlite_engine = create_engine('sqlite:///instance/database.db')
SQLiteSession = sessionmaker(bind=sqlite_engine)
sqlite_session = SQLiteSession()

# 2️⃣ MySQL Target DB
mysql_engine = create_engine("mysql+pymysql://iTAC:SmartAccess%402025@localhost:3306/taskmanager1")
MySQLSession = sessionmaker(bind=mysql_engine)
mysql_session = MySQLSession()

# 3️⃣ ดึงข้อมูลจาก SQLite
sqlite_tasks = sqlite_session.query(Task).all()
sqlite_users = sqlite_session.query(User).all()

# 4️⃣ Clone objects แบบปลอดภัย
new_users = [User(username=u.username, password=u.password) for u in sqlite_users]
new_tasks = [Task(title=t.title, status=t.status) for t in sqlite_tasks]

# 5️⃣ ใส่เข้า MySQL
mysql_session.add_all(new_users)
mysql_session.add_all(new_tasks)
mysql_session.commit()

print("✅ Data migrated successfully from SQLite to MySQL!")
