/*
This library holds all the helper functions needed for the requests, including the database information.

Things to do:
- Load in the appropriate data from json
- iterate through the requirements and record anything that needs to be done and throw out otherwise
- spit out the things that need to be done
- sum the credit hours total of the classes based of querying courses api
*/


let file = require('./test.json');


var maj = ['CS','SE']


function major_requirements(arr) {
    var majors = [];
    var classes = [];

    arr.forEach(element => {
       majors.push(getKeys(file, element)); 
    });
    

    // arr.forEach(element => {
    //     var currMajor = file.
    //     reqs.forEach(element => {
    //         if (!classes.includes(element)) {
    //             classes.push(element);
    //         }
    //     })
    // });
    var name = "Computer Science"
    // console.log(file.Computer_Science.code);
    console.log(majors);
}

major_requirements(maj);


function getName(obj, code) {
    var objects = [];
    for (var i in obj) {
        if (!obj.hasOwnProperty(i)) continue;
        if (typeof obj[i] == 'object') {ß
            objects = objects.concat(getKeys(obj[i], code));
        } else if (obj[i] == code) {
            objects.push(i);
        }
    }
    return objects[0];
}

function checkCompletion(completed, requirement) {
    if (Array.isArray(requirement)) {
        requirement.forEach
    }
}