def filterBible(scripture, book, chapter):
    return [script for script in scripture if  book == script[0:2] and chapter == script[2:5]]
