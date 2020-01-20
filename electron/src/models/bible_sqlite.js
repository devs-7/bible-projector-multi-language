const path = require('path')
const sqlite3 = require('sqlite3').verbose()
const db = new sqlite3.Database(path.join(__dirname, '/../../data/bible.db'))
const strings = require('../helper/strings')

class Bible {
    constructor() {
        this.livro = undefined
        this.capitulo = undefined
        this.versiculo = undefined
        this.texto = undefined
        this.versao = undefined
    }

    query(q, versao, callback) {
        this.versao = versao
        q = q.replace(/:/g, ' ').replace(/  /g, ' ')
        q = strings.normalizar(q)
        let livCapVer = q.split(" ")

        let ver = livCapVer.pop()
        let cap = livCapVer.pop()
        let liv = livCapVer.join(' ')

        const sql = `
            SELECT versoes.versao as versao, livros.nome as livro, textos.capitulo, textos.versiculo, textos.texto
            FROM textos
            JOIN livros on textos.id_livro = livros.id
            JOIN versoes on textos.id_versao = versoes.id
            WHERE 
            versao = '${versao}' AND
            livros._sigla LIKE '${liv}' AND
            textos.capitulo = ${cap} AND
            textos.versiculo = ${ver}
        `
        db.each(sql, (err, row) => {
            if (!err) {
                this.livro = row.livro
                this.capitulo = row.capitulo
                this.versiculo = row.versiculo
                this.texto = row.texto
                callback()
            }
        })
    }

    getVersoes(callback) {
        db.each("SELECT versao FROM versoes", (err, row) => {
            if (!err) {
                callback(row)
            }
        })
    }
}

const bible = new Bible()
bible.query('gn 1 1', 'ARA', () => {
    console.log(bible)
})

let n = 0
bible.getVersoes(versoes => {
    n++
    console.log(versoes, n)
})

module.exports = Bible