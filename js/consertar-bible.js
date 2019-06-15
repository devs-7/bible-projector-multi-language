const fs = require('fs');

const versoes = ['ara', 'arc', 'ntlh', 'nvi'];
var bible;

versoes.forEach(versao => {
    bible = fs.readFileSync('./data/bibles/' + versao + '.txt', 'utf-8');

    bible = bible.replace(/Miqueias/g, 'Miquéias');
    bible = bible.replace(/Oseias/g, 'Oséias');

    fs.writeFileSync('./data/bibles/' + versao + '.txt', bible);
});