function parimpar(n){
    if(n == 0){
        return 'nulo'
    }else if(n%2 == 0){
        return 'par'
    }else{
        return 'ímpar'
    }
}
var n = 0
var parouimp = parimpar(n)
console.log(`${n} é um número ${parouimp}.`)