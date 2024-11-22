from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)



    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active":self.is_active
            # do not serialize the password, its a security breach
        }
    
class Planet(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200))
    population = db.Column(db.Integer)
    weather = db.Column(db.String(50),nullable=False)

    
    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "weather": self.weather,
            # do not serialize the password, its a security breach
        }
    
class People(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200))
    age = db.Column(db.Integer)
    zodiac = db.Column(db.String(100))
   

   
    def __repr__(self):
        return '<People %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "zodiac": self.zodiac
        }

class Favorite(db.Model):
 

    id = db.Column(db.Integer,primary_key=True)
    people_id = db.Column(db.Integer,db.ForeignKey('people.id'))
    people = db.relationship(People)

    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    user = db.relationship(User)

    planet_id = db.Column(db.Integer,db.ForeignKey('planet.id'))
    planet = db.relationship(Planet)


    def __repr__(self):
        return '<Favorite %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user.serialize() if self.user != None else " ",
            "people": self.people.serialize() if self.people != None else " ",
            "planet": self.planet.serialize() if self.planet != None else " "
            
        }
            # do not serialize the password, its a security breach
        


