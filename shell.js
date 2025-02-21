var cds = require("child_process")
const readline = require('node:readline');
const { stdin: input, stdout: output } = require('node:process');
var answer=""
console.log('\033c\033[43;30m\n');
var t=true
var a=""
var inputString=""

const rl = readline.createInterface({ input , output});
for(i=0;i<1000;i++){
    rl.question('> : ', (answer) => {
    
    var w =cds.exec( "/usr/bin/"+answer  , function (err , out ,se){
	     console.log(`${out}\n`);
             if (err!=null) console.log(`${err}`);
         });
   
    rl.close();
   });
 };      
