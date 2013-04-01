#-*- coding: UTF-8 -*-

from flask import render_template, request, redirect, url_for, json

from xichuangzhu import app

from xichuangzhu.models.collection_model import Collection
from xichuangzhu.models.work_model import Work
from xichuangzhu.models.author_model import Author

from xichuangzhu.utils import content_clean

# page - single collection
#--------------------------------------------------

@app.route('/collection/<int:collectionID>')
def single_collection(collectionID):
	collection = Collection.get_collection(collectionID)
	works      = Work.get_works_by_collection(collectionID)
	for work in works:
		work['Content'] = content_clean(work['Content'])
	return render_template('single_collection.html', collection=collection, works=works)

# page - add collection
#--------------------------------------------------

@app.route('/collection/add', methods=['POST', 'GET'])
def add_collection():
	if request.method == 'GET':
		return render_template('add_collection.html')
	elif request.method == 'POST':
		collection   = request.form['collection']
		authorID     = int(request.form['authorID'])
		introduction = request.form['introduction']
		newCollectionID = Collection.add_collection(collection, authorID, introduction)
		return redirect(url_for('single_collection', collectionID = newCollectionID))

# page - edit collection
#--------------------------------------------------

@app.route('/collection/edit/<int:collectionID>', methods=['POST', 'GET'])
def edit_collection(collectionID):
	if request.method == 'GET':
		collection = Collection.get_collection(collectionID)
		return render_template('edit_collection.html', collection=collection)
	elif request.method == 'POST':
		collection   = request.form['collection']
		authorID     = int(request.form['authorID'])
		introduction = request.form['introduction']
		Collection.edit_collection(collection, authorID, introduction, collectionID)
		return redirect(url_for('single_collection', collectionID=collectionID))

# helper - search authors in page add & edit collection
#--------------------------------------------------

@app.route('/collection/search_author', methods=['POST'])
def search_author_in_collection():
	name = request.form['author']
	authors = Author.get_authors_by_name(name)
	return json.dumps(authors)