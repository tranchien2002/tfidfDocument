{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from pymongo import MongoClient\n",
    "import pdb\n",
    "client = MongoClient('localhost', 27017)\n",
    "db = client.test_15\n",
    "\n",
    "\n",
    "\n",
    "def single_insert(colection, document):\n",
    "    col = db[colection]\n",
    "    col.insert_one(document)\n",
    "\n",
    "def bulk_insert(colection, documents):\n",
    "    col = db[colection]\n",
    "    col.insert_many(documents)\n",
    "\n",
    "def get_colection(colection):\n",
    "    return db[colection]\n",
    "\n",
    "def find_by_ids(colection, ids):\n",
    "    col = db[colection]\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
