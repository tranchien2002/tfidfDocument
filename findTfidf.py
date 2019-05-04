# -*- coding: utf-8 -*-
import Mongodb as mongo
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from document2json import pickle_json, cosine_json
from bson.objectid import ObjectId
import pdb
docs_col = mongo.get_colection("documents")
test_col = mongo.get_colection("tfidfTest")

def compute_tfidf(a, b):
    tf = TfidfVectorizer(analyzer='word', ngram_range=(1,1), min_df = 1, stop_words = 'english')
    tfidf_matrix = tf.fit_transform([a,b])
    matrix_vectors = tfidf_matrix.todense()
    return cosine_similarity(matrix_vectors[0], matrix_vectors[1])

def get_list_similarity(doc, docs):
    compared_docs = []
    for item in docs:
        compared_docs.append(cosine_json(item['_id'], compute_tfidf(doc, item['content'])))
    return compared_docs

def sort_by_similarity(list_docs):
    sorted_list = sorted(list_docs, key= lambda x: float(x['similarity']), reverse=True)
    return sorted_list

def get_topn_similarity(doc, docs, n):
    results = get_list_similarity(doc, docs)
    sorted_results = sort_by_similarity(results)
    return sorted_results[:n]

def get_detail_docs(list_ids):
    list_docs = []
    for item in list_ids:
        doc = docs_col.find_one({"_id": ObjectId(str(item['id']))})
        doc['similarity'] = item['similarity']
        doc.pop('_id', None)
        list_docs.append(doc)
    return list_docs

if __name__ == '__main__':
    test_trans = test_col.find({})
    for item in test_trans:
        print(item['title'])
        docs_en = docs_col.find({"lang": "english"})
        list_computed = get_topn_similarity(item['content'], docs_en, 3)
        list_details = get_detail_docs(list_computed)
        for i in list_details:
            print(i['title'])
        print("=======================================")