/* 
CURRENT STATE  1.0.0
- *should* work for many STEM majors... I tried - CS, MechE, IndustrialE, AerospaceE, SystemsE, EE - all of which worked
- lacks "take MATH XXX OR MATH XXX" functionality
- incompatible with CS + X, Math, and some LAS majors (still need to test it out with more)
- specific majors I tried that didn't work - Accountancy, Jazz Performance (LOL)
*/
const got = require('got');
const cheerio = require('cheerio');
const chalk = require('chalk');
const fs = require('fs');

// CHANGE THESE VARIABLES TO THE MAJOR YOU WANT TO SCRAPE
const MAJOR_TITLE = "Electrical Engineering";
const MAJOR_CODE = "EE";
const DEG_URL = "http://catalog.illinois.edu/undergraduate/engineering/electrical-engineering-bs/#degreerequirementstext";

var db; 
fs.readFile('db.json', 'utf8', function (err, data) {
    db = JSON.parse(data);
    // initialize object for this major
    var major = {};
    major["code"] = MAJOR_CODE;
    major["title"] = MAJOR_TITLE;
    var core = [];
    major["elective_credit"] = 0;

    // get response HTML from degree reqs page
    got(DEG_URL).then(response => {
        const $ = cheerio.load(response.body);
        var div = $('div #degreerequirementstextcontainer');
        // h3s correspond to category titles, tables correspond to list of classes in each category
        var h3s = div.find("h3");        
        var tables = div.find(".sc_courselist");                  
            
        // get stats on major
        var minTechGPA = parseInt($($('h4', div)[0]).text().replace(/[^0-9\.]+/g,""));
        var minOverallGPA = parseInt($($('h4', div)[1]).text().replace(/[^0-9\.]+/g,""));
        var numCredits = parseInt($($('h4', div)[2]).text().replace(/[^0-9\.]+/g,"")); 
    
        var hourSum = 0;
        for (var i = 0; i < h3s.length; i++) {    
            // Get category title
            var sectionTitle = h3s[i].lastChild.children[0].data;           
            // Ignore section if this is an Electives section
            if (!sectionTitle.includes("Elective")) {   
                var hours = 0;       
                // check if section has an explicit listsum class
                if ($('tr', 'tbody', tables[i]).hasClass("listsum")) {                
                    hours = parseInt($('.hourscol', $('.listsum', 'tbody', tables[i])).text());                
                } else {
                    // if it doesn't, we need to go through each row to find Total Hours row
                    $('tr', 'tbody', tables[i]).each((i, elem) => {
                        var comment = $('.courselistcomment', $('td', elem))[0];
                        if ($(comment).text().includes("Total")) {
                            hours = parseInt($('.hourscol', elem).text())
                        }
                    });                
                }                        
                hourSum+=hours;            
                console.log(chalk.redBright(chalk.bold(sectionTitle + " - " + hours + " hours")));
                // parse through each row of section to get each class
                $('tr', 'tbody', tables[i]).each((i, elem) => {
                    if ($('a', elem).length==1) {
                        var href = $('a', elem)[0].attribs.title;  
                        core.push(href);                  
                        console.log(chalk.green(href));
                    } else {
                        var comment = $('.courselistcomment', $('td', elem))[0];
                        if ($(comment).text().includes("elective")) {
                            // if this row has a comment indicating elective, then break out of loop (refer to CS degree reqs for example)
                            return false;
                        }                    
                    }
                });
            }                   
        }
    
        // calculate elective hours based on core credits and ttl credits needed
        var electives = numCredits - hourSum;
        console.log(chalk.bold(chalk.redBright("Electives (All Categories): " + electives + " hours")))

        // build JSON object for this major
        major["elective_credit"] = electives;
        major["min_technical_gpa"] = minTechGPA;
        major["min_overall_gpa"] = minOverallGPA;
        major["credits_needed"] = numCredits;
        major["core"] = core;
        db[MAJOR_TITLE] = major;
        // update JSON file
        fs.writeFile ('db.json', JSON.stringify(db), function(err) {
            if (err) {
                response.send("Error Updating DB: " + err.message);                
            } else {
                console.log("Updated DB");
            }
        }); 
    }).catch(err => {
        console.log(err);
    });
});

