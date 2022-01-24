
verificarPalindromo('Amor a Roma');

function verificarPalindromo (string){ 

    var gnirts = string.split('').reverse().join('');

    if(string.toLowerCase() === gnirts.toLowerCase()){
        console.log(`'${string}' é um palíndromo`)
    }else{
        console.log(`'${string}' não é um palíndromo`)
    }
}
let person = {
    name: Ana
}
console.log(person[name])
