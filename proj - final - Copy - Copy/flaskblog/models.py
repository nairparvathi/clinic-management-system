from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


        db = SQLAlchemy(app)

class Patients(db.Model):
    pID = db.Column(db.Integer, primary_key=True,nullable= False)
    Fname = db.Column(db.Text, nullable=False)
    Lname = db.Column(db.Text, nullable=False)
    PhoneNo = db.Column(db.Numeric, nullable=False)
    sex = db.Column(db.Text, nullable=False)
    Age = db.Column(db.Numeric, nullable=False)
    


    def __repr__(self) -> str:
        return f"{self.pID} - {self.Fname} - {self.Lname} - {self.PhoneNo} - {self.sex} - {self.Age} "



class Staff(db.Model):
    sID = db.Column(db.Integer, primary_key=True,nullable= False)
    FirstName = db.Column(db.Text, nullable=False)
    LastName = db.Column(db.Text, nullable=False)
    Sex = db.Column(db.Text, nullable=False)
    Designation = db.Column(db.Text, nullable=False)
    Shift = db.Column(db.Text, nullable=False)
    Whours = db.Column(db.Numeric, nullable=False)

    def repr(self)->str:
        return f"Staff{self.sID} - {self.FirstName} - {self.LastName} - {self.Sex}- {self.Designation} - {self.Shift} - {self.Whours}"

class Medicine(db.Model):
    Mno = db.Column(db.Integer, primary_key=True,nullable= False)
    MName = db.Column(db.Text, nullable=False)
    MAvailability = db.Column(db.Text, nullable=False)
    MPrice = db.Column(db.Integer, nullable=False)
    Manufacturing_Date = db.Column(db.Numeric, nullable=False)
    Expiry_Date = db.Column(db.Numeric, nullable=False)


    def _repr_(self)->str:
        return f"Medicine{self.Mno}-{self.MName}-{self.MAvailability}-{self.MPrice}-{self.Manufacturing_Date}-{self.Expiry_Date}"

class Appointments(db.Model):
    ID = db.Column(db.Integer, primary_key=True,nullable=False)
    Name = db.Column(db.Text, nullable=False)
    Problem = db.Column(db.Text, nullable=False)
    Time = db.Column(db.Time, nullable=False)
    Doctor = db.Column(db.Text, nullable=False)


    def _repr_(self)->str:
        return f"Appointments{self.ID} - {self.Name} - {self.Problem} - {self.Time} - {self.Doctor}"