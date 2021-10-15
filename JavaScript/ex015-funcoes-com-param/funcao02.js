
//SITUAÇÃO 1
function soma(n1, n2){
    return n1 + n2
}
console.log(soma(2, 3))
//return 5


//SITUAÇÃO 2
function soma(n1, n2){
    return n1 + n2
}
console.log(soma(2))
//return NaN(Not a number), pq 2 + undefined = NaN


//SITUAÇÃO 3
//Se nenhum valor for definido para n1 ou n2, será considerado 0:
function soma(n1=0, n2=0){
    return n1 + n2
}
console.log(soma(2))
//return 2
