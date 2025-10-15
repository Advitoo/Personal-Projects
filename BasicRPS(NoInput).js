console.log("Pick your Choice.")
console.log("1.Rock")
console.log("2.Paper")
console.log("3.Scissors.")
let player= "Rock"
let comp=(Math.floor(Math.random()*10))
if (comp>=0 && comp<=3){
    comp="Rock"
}
else if (comp>3 && comp<=6){
    comp="Paper"
}
else{
    comp="Scissors"
}
console.log("Player picked:",player)
console.log("Computer picked:",comp)
if (player==="Rock" && comp==="Scissors"){
    console.log("Player Won!")
}
else if (player==="Paper" && comp==="Rock"){
    console.log("Player Won!")
}
else if (player==="Scissors" && comp==="Paper"){
    console.log("Player Won!")
}
if (comp==="Rock" && player==="Scissors"){
    console.log("Computer Won!")
}
else if (comp==="Paper" && player==="Rock"){
    console.log("Computer Won!")
}
else if (comp==="Scissors" && player==="Paper"){
    console.log("Computer Won!")
}
else if(player===comp){
    console.log("Same Choice!, Tie!")
}