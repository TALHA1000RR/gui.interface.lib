var cds = require("child_process")
const readline = require('node:readline');
const { stdin: input, stdout: output } = require('node:process');
var answer=""
console.log('\033c\033[43;30m\n');
var t=true
var a=""
var inputString=""
for(i=0;i<1000;i++){
const rl = readline.createInterface({ input });

    rl.question('> : ', (answer) => {
    

    rl.close();
   });
   answer="ls"
   var w =cds.exec( "/usr/bin/"+answer  , function (err , out ,se){
	     console.log(`${out}\n`);
             if (err!=null) console.log(`${err}`);
         });
}