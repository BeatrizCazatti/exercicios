var s = 'JavaScript'
'Eu estou aprendendo s' //não faz intepolação
'Eu estou aprendendo' + s //usa concatenação
`Eu estou aprendendo ${s}` //usa template string

s.length //caracteres da string
s.toUpperCase() //tudo para 'MAIÚSCULAS'
s.toLowerCase() //tudo para 'minúsculas'


//Formatando Números
var n1 = 1543.5
n1.toFixed(2) //aproxima duas casas
n1.toLocaleString('pt-BR', {style: 'currency', currency:'BRL'}) //passa o valor para notação monetária brasileira('BRL'), estado unidense('USD') ou europeu('EUR')