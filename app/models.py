from datetime import datetime
from app import db 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login, admin
from flask_admin.contrib.sqla import ModelView

class user(UserMixin ,db.Model):
    user_id = db.Column(db.String(64), primary_key = True) 
    username = db.Column(db.String(20), index=True, unique = True)
    user_type = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return (self.user_id)

@login.user_loader 
def load_user(id):
    return user.query.get(id)


class pharm_plant(db.Model):
    pp_id = db.Column(db.String(8), primary_key=True)
    pp_name = db.Column(db.String(64))
    pp_address = db.Column(db.String(64))
    pp_city = db.Column(db.String(64))
    pp_state = db.Column(db.String(64))
    pp_zipcode = db.Column(db.String(64))

    def __repr__(self):
        return '<Plant {}>'.format(self.pp_name)

class medicine(db.Model):
    m_id = db.Column(db.String(5), primary_key=True)
    category = db.Column(db.String(64))
    m_medicine = db.Column(db.String(64))
    ingredient = db.Column(db.String(100))

    def __repr__(self):
        return '<Medicine {}>'.format(self.m_medicine)


class plant_inven(db.Model):
    m_id = db.Column(db.String(5), db.ForeignKey("medicine.m_id"), primary_key = True)
    pp_id = db.Column(db.String(8), db.ForeignKey("pharm_plant.pp_id"), primary_key = True) 
    stock_quant = db.Column(db.Integer)
    unit_price = db.Column(db.Float)

    def __repr__(self):
        return '<plant inventory {}>'.format(self.pp_id)


class shipments(db.Model):
    s_id = db.Column(db.String(9), primary_key=True)
    pp_id = db.Column(db.String(8),db.ForeignKey("pharm_plant.pp_id"))
    m_id = db.Column(db.String(5),db.ForeignKey("medicine.m_id"))
    pc_id = db.Column(db.String(8),db.ForeignKey("pharm.pc_id"))
    s_Quant = db.Column(db.Integer)
    TotalCost = db.Column(db.Float) 
    s_order_date = db.Column(db.Date) 
    s_ship_date = db.Column(db.Date) 
    s_status = db.Column(db.String(64))


    def __repr__(self):
        return '<Shipment {}>'.format(self.s_id)


class pharm(db.Model):
    pc_id = db.Column(db.String(8), primary_key=True)
    pc_name = db.Column(db.String(64))
    pc_address = db.Column(db.String(64))
    pc_city = db.Column(db.String(64))
    pc_state = db.Column(db.String(64))
    pc_zipcode = db.Column(db.String(64))

    def __repr__(self):
        return '<Pharmacy {}>'.format(self.pc_name)


class pharm_inven(db.Model):
    pc_id = db.Column(db.String(8), db.ForeignKey("pharm.pc_id"), primary_key= True) #prim key
    m_id = db.Column(db.String(5), db.ForeignKey("medicine.m_id"), primary_key= True) #prim key
    quant = db.Column(db.Integer)
    price = db.Column(db.Float) 

    def __repr__(self):
        return '<Pharmacy Inventory {}>'.format(self.pc_id)

class prescription_order(db.Model):
    order_id = db.Column(db.String(9), primary_key=True)
    order_status = db.Column(db.String(64))
    order_date = db.Column(db.Date) 
    pat_id = db.Column(db.String(9),db.ForeignKey("patient.pat_id"))
    doc_id = db.Column(db.String(12),db.ForeignKey("doctor.doc_id"))
    m_id = db.Column(db.String(5),db.ForeignKey("medicine.m_id"))
    pc_id = db.Column(db.String(8))
    Quantity = db.Column(db.Integer)
    order_price = db.Column(db.Float) 
    pc_id = db.Column(db.String(8), db.ForeignKey("pharm.pc_id"))

    def __repr__(self):
        return '<prescription order {}>'.format(self.order_id)


class patient(db.Model):
    pat_id = db.Column(db.String(9), primary_key=True)
    doc_id = db.Column(db.String(12),db.ForeignKey("doctor.doc_id"))
    pat_first_name = db.Column(db.String(64))
    pat_last_name = db.Column(db.String(64))
    pat_gender = db.Column(db.String(1))
    pat_ethnicity = db.Column(db.String(64))
    dob = db.Column(db.Date) 
    pat_address = db.Column(db.String(64))
    pat_city = db.Column(db.String(64))
    pat_state = db.Column(db.String(64))
    pat_zipcode = db.Column(db.Integer)
    pat_first_visit_date = db.Column(db.Date) 

    def __repr__(self):
        return '<Patient {}>'.format(self.pat_last_name)

class appointment(db.Model):
    apt_id = db.Column(db.Integer, primary_key=True)
    pat_id = db.Column(db.Integer, db.ForeignKey('patient.pat_id'))
    doc_id = db.Column(db.Integer, db.ForeignKey('doctor.doc_id'))
    scedule_day = db.Column(db.Date) 
    apt_date = db.Column(db.Date) 
    apt_time = db.Column(db.Time) 

    def __repr__(self):
        return '<Doctor number {} on {} at {} >'.format(self.doc_id, self.apt_date, self.apt_time)


class doctor(db.Model):
    doc_id = db.Column(db.String(12), primary_key=True)
    doc_first_name = db.Column(db.String(64))
    doc_last_name = db.Column(db.String(64))
    doc_speciality = db.Column(db.String(64))
    doc_address = db.Column(db.String(64))
    doc_city = db.Column(db.String(64))
    doc_state = db.Column(db.String(64))
    doc_zipcode = db.Column(db.String(64))

    def __repr__(self):
        return '<Dr. {}>'.format(self.doc_last_name)


admin.add_view(ModelView(user, db.session))
admin.add_view(ModelView(pharm_plant, db.session))
admin.add_view(ModelView(plant_inven, db.session))
admin.add_view(ModelView(shipments, db.session))
admin.add_view(ModelView(pharm, db.session))
admin.add_view(ModelView(pharm_inven, db.session))
admin.add_view(ModelView(prescription_order, db.session))
admin.add_view(ModelView(patient, db.session))
admin.add_view(ModelView(appointment, db.session))
admin.add_view(ModelView(doctor, db.session))