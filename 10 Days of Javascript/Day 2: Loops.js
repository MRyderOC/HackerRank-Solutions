'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function isVowel(ch) {
    const vowels = ["a", "e", "i", "o", "u"];
    for (let i = 0; i < vowels.length; i++)
        if (ch == vowels[i])
            return true;

    return false;
}
function vowelsAndConsonants(s) {
    for (let ch of s)
        if (isVowel(ch))
            console.log(ch);

    for (let ch of s)
        if (!isVowel(ch))
            console.log(ch);

}


function main() {
    const s = readLine();
    
    vowelsAndConsonants(s);
}