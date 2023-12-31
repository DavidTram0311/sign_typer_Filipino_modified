# Generated by Django 3.0.7 on 2020-08-13 06:51

from django.db import migrations


class Migration(migrations.Migration):

	dependencies = [
		('inventory', '0013_auto_20200807_1805'),
	]

operations = [
	migrations.RenameField(
		model_name='sign',
		old_name='twohanded',
		new_name='twoHanded',
	),
	migrations.RenameField(
		model_name='sign',
		old_name='hs',
		new_name='rightHandshape',
	),
	migrations.RenameField(
		model_name='sign',
		old_name='efd',
		new_name='rightFingerDirection',
	),
	migrations.RenameField(
		model_name='sign',
		old_name='ori',
		new_name='rightPalmOrientation',
	),
	migrations.RenameField(
		model_name='sign',
		old_name='lhs',
		new_name='leftHandshape',
	),
	migrations.RenameField(
		model_name='sign',
		old_name='lefd',
		new_name='leftFingerDirection',
	),
	migrations.RenameField(
		model_name='sign',
		old_name='lori',
		new_name='leftPalmOrientation',
	),
	migrations.RenameField(
		model_name='sign',
		old_name='loctype',
		new_name='locationType',
	),
	migrations.RenameField(
		model_name='sign',
		old_name='loc',
		new_name='rightLocation',
	),
	migrations.RenameField(
		model_name='sign',
		old_name='side',
		new_name='rightLocationSide',
	),
	migrations.RenameField(
		model_name='sign',
		old_name='contact',
		new_name='rightLocationContact',
	),
	migrations.RenameField(
		model_name='sign',
		old_name='lloc',
		new_name='leftLocation',
	),
	migrations.RenameField(
		model_name='sign',
		old_name='lside',
		new_name='leftLocationSide',
	),
	migrations.RenameField(
		model_name='sign',
		old_name='lcontact',
		new_name='leftLocationContact',
	),
]
