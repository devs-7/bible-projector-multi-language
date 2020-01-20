const path = require('path')
const sqlite3 = require('sqlite3').verbose()
const db = new sqlite3.Database(path.join(__dirname, '/../../data/bible.db'))

class Bible {
    constructor() {

    }

    query() {
        db.each("SELECT * FROM livros", function (err, row) {
            console.log(row);
        })
    }
}

module.exports = Bible