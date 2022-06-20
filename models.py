#!interpreter [optional-arg]
# -*- coding: utf-8 -*-
#
"""
models.py: All Models
"""

#Built-ins/Generic
import datetime

#Libs
from sqlalchemy import (
	Table, Column, Integer, String, MetaData, ForeignKey, Boolean
	)
from sqlalchemy.orm import relationship

#fur datum
from sqlalchemy.sql import func
from sqlalchemy import DateTime, Date
#Modules
from flask_app import db
from flask_login import UserMixin

	
class Item(db.Model):

	__tablename__ = "items"

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(200), nullable=False)
	description = db.Column(db.String(200), nullable=True)
	
	vertex_shader = db.Column(db.Text, nullable=True)
	fragment_shader = db.Column(db.Text, nullable=True)
	link_url = db.Column(db.String(500), nullable=True)
	image_url = db.Column(db.String(200), nullable=True)
	
	