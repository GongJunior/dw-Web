function getRolls(){
    let array = new Uint8Array(1);
    let allRolls = "";

    for (let roll = 0; roll < 5; roll++){
        do {
           window.crypto.getRandomValues(array);
        }while (array[0] > 42 * 6)
        allRolls += (array[0]%6 + 1).toString();
    }
    return parseInt(allRolls);
}

function generateResult(listName){
    let rolls = "";
    let words = "";
    let numWords;
    let currentList = JSON.parse(localStorage.getItem(listName));

    numWords = document.getElementById('numOfWords').value;

    for (let roll = 0; roll < numWords; roll++) {
        let wordID = getRolls();
        rolls += wordID + " ";
        words += currentList[wordID] + " ";
    }
    sentOutputToPage(words,rolls);
}

function sentOutputToPage(words, rolls){
    document.getElementById("passphrase").innerHTML = words;
    document.getElementById("allrolls").innerHTML = rolls;
}

function rollTest(){
    document.getElementById("result").innerHTML = getRolls();
}

function loadDicewaretoMemory(package){
    for (const prop in package){
        if (!localStorage.getItem(prop)){
            localStorage.setItem(prop,JSON.stringify(package[prop]));
        }
    }
}