#-*- coding: UTF-8 -*-
import datetime
from flask import g
from xichuangzhu import db

class CollectWork(db.Model):
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    user = db.relationship('User', backref=db.backref('collect_works'))

    work_id = db.Column(db.Integer, db.ForeignKey('work.id'), primary_key=True)
    work = db.relationship('Work', backref=db.backref('collectors', lazy='dynamic'))

    def __repr__(self):
        return '<User %d collect Work %d>' % (self.user_id, self.work_id)

class CollectWorkImage(db.Model):
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    user = db.relationship('User', backref=db.backref('collect_work_images'))

    work_image_id = db.Column(db.Integer, db.ForeignKey('work_image.id'), primary_key=True)
    work_image = db.relationship('WorkImage', backref=db.backref('collectors', lazy='dynamic'))

    def __repr__(self):
        return '<User %d collect WorkImage %d>' % (self.user_id, self.work_image_id)