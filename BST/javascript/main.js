const fs = require('fs');
const Tree = require('./tree.js');

function getNumbers(path) {
    const content = fs.readFileSync(path, 'utf-8');
    const numbers = content.split(/\s+/).map(Number);
    return numbers;
}

function main() {
    const amount = parseInt(process.argv[2]);

    const addNumbers = getNumbers('/datasets/add.txt').slice(0, amount);
    const checkNumbers = getNumbers('/datasets/check.txt').slice(0, amount);
    const bst = new Tree();

    // Add elements
    let startTime = Date.now();
    for (let i of addNumbers) {
        bst.add(i);
    }
    let endTime = Date.now();
    console.log(`ADD_TEST:${(endTime - startTime) / 1000}`);

    // Check elements
    startTime = Date.now();
    for (let i of checkNumbers) {
        bst.contain(i);
    }
    endTime = Date.now();
    console.log(`CHECK_TEST:${(endTime - startTime) / 1000}`);

    // Len elements
    startTime = Date.now();
    for (let i = 0; i < 10; i++) {
        bst.length();
    }
    endTime = Date.now();
    console.log(`LEN_TEST:${(endTime - startTime) / 10000}`);

    // Height elements
    startTime = Date.now();
    for (let i = 0; i < 10; i++) {
        bst.height();
    }
    endTime = Date.now();
    console.log(`HEIGHT_TEST:${(endTime - startTime) / 10000}`);

    console.log(`VALIDATION:${bst.length()}:${bst.height()}`);
}

main();
