var fs = require("fs");
var cds = require("child_process")
var args= process.argv.slice(2);
const readline = require('node:readline');
const { stdin: input, stdout: output } = require('node:process');
var answer=""
console.log('\033c\033[43;30m\n');
var t=true
var a=""
var d=""
var inputString=""

fs.readFile ( args[0] , function  ( err , s ){
    
    ss=s.toString()    
   
    par=ss.split(",");
    for (i = 0 ; i < par.length ; i=i+1 ) {
             
        	  var w = cds.exec ( "/bin/sh -c '" + par[i] + "'" , function (err , out ,se) {
                      console.log( out.toString() + "\r\n"  );
          	   });
               
   	  }
   });