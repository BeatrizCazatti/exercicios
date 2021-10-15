var num = [5, 8, 2, 9, 3]
num.push(1)
num.sort()
console.log(num)
console.log(`O vetor tem ${num.length} posições`)
console.log(`O primeiro vetor é o número ${num[0]}`)
var n = 10
var pos = num.indexOf(n)
//console.log(num.indexOf(2))

if(pos == -1){
    console.log(`o valor ${n} não foi encontrado!`)
}else {
    console.log(`O valor ${n} está na posição ${pos}`)
}


