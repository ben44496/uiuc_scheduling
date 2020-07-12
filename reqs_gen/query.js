var json = {"Computer Science":{"code":"CS","title":"Computer Science","elective_credit":65,"min_technical_gpa":2,"min_overall_gpa":2,"credits_needed":128,"core":["CS 100","CS 210","ENG 100","MATH 221","MATH 231","MATH 241","MATH 415","PHYS 211","PHYS 212","CS 125","CS 126","CS 173","CS 225","CS 233","CS 241","CS 361","CS 357","CS 374","CS 421"]},"Systems Engineering & Design":{"code":"SE","title":"Systems Engineering & Design","elective_credit":46,"min_technical_gpa":2,"min_overall_gpa":2,"credits_needed":128,"core":["ENG 100","SE 100","SE 290","CHEM 102","CHEM 103","MATH 221","MATH 231","MATH 241","MATH 285","MATH 415","PHYS 211","PHYS 212","PHYS 213","CS 101","ECE 110","ECE 211","IE 300","IE 310","SE 101","SE 261","SE 310","SE 311","SE 312","SE 320","SE 424","SE 494","SE 495","TAM 211","TAM 212","TAM 251","TAM 335"]},"Mechanical Engineering":{"code":"ME","title":"Mechanical Engineering","elective_credit":47,"min_technical_gpa":2,"min_overall_gpa":2,"credits_needed":128,"core":["ENG 100","ME 290","CHEM 102","CHEM 103","MATH 221","MATH 231","MATH 241","MATH 285","MATH 415","PHYS 211","PHYS 212","CS 101","ECE 205","ECE 206","ME 170","ME 270","ME 200","ME 310","ME 320","ME 330","ME 340","ME 360","ME 370","ME 371","ME 470","TAM 210","TAM 212","TAM 251"]},"Aerospace Engineering":{"code":"AE","title":"Aerospace Engineering","elective_credit":null,"min_technical_gpa":2,"min_overall_gpa":128,"credits_needed":null,"core":["AE 100","ENG 100","CHEM 102","CHEM 103","MATH 221","MATH 225","MATH 231","MATH 241","MATH 285","PHYS 211","PHYS 212","AE 140","AE 202","AE 311","AE 312","AE 321","AE 323","AE 352","AE 353","AE 370","AE 433","AE 442","AE 443","AE 460","AE 461","AE 483","CS 101","ECE 205","ME 200","MSE 280","TAM 210","TAM 212"]},"Electrical Engineering":{"code":"EE","title":"Electrical Engineering","elective_credit":66,"min_technical_gpa":2,"min_overall_gpa":2,"credits_needed":128,"core":["ENG 100","CHEM 102","CHEM 103","MATH 221","MATH 231","MATH 241","MATH 286","PHYS 211","PHYS 212","PHYS 213","PHYS 214","ECE 110","ECE 120","ECE 220","ECE 210","ECE 313","ECE 329","ECE 340","ECE 385","ECE 445"]}};
var majors = [];
var selected_majors = [];
var classes_set = new Set();

for (var i = 0; i < Object.keys(json).length; i++) {
    var key = Object.keys(json)[i];
    majors.push(json[key]["title"]);
}

autocomplete(document.getElementById("major"), majors); 

function addMajor() {
    var major_entered = document.getElementById("major").value;
    if (!Object.keys(json).includes(major_entered)) alert("You entered an invalid major.");
    else {
        document.getElementById("major").value = "";
        selected_majors.push(major_entered);
        if (selected_majors.length == 1) 
            document.getElementById("selected_majors").innerHTML += major_entered;
        else 
            document.getElementById("selected_majors").innerHTML += ", " + major_entered;
    }
    getDegreeReqs();    
}

function getDegreeReqs() {
    var cards = document.getElementsByClassName("cards")[0];
    cards.innerHTML = "";
    for (var i = 0; i < selected_majors.length; i++) {
        for (var j = 0; j < json[selected_majors[i]]["core"].length; j++) {
            classes_set.add(json[selected_majors[i]]["core"][j]);
        }
    }
    classes_set.forEach(course => { cards.innerHTML += "<div class='card'><center>" + course + "</center></div>"});
    document.getElementById("deg_req_banner").style.display = "block";
    document.getElementById("deg_req_banner").innerHTML = "Degree Requirements (" + classes_set.size + " core): ";    
}


// helper method to provide autocomplete on major input text field
// ignore
function autocomplete(inp, arr) {    
    var currentFocus;    
    inp.addEventListener("input", function(e) {
        var a, b, i, val = this.value;        
        closeAllLists();
        if (!val) { return false;}
        currentFocus = -1;
        a = document.createElement("DIV");
        a.setAttribute("id", this.id + "autocomplete-list");
        a.setAttribute("class", "autocomplete-items");        
        this.parentNode.appendChild(a);        
        for (i = 0; i < arr.length; i++) {
            if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {            
            b = document.createElement("DIV");            
            b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
            b.innerHTML += arr[i].substr(val.length);            
            b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";            
                b.addEventListener("click", function(e) {                
                inp.value = this.getElementsByTagName("input")[0].value;            
                closeAllLists();
            });
            a.appendChild(b);
            }
        }
    });    
    inp.addEventListener("keydown", function(e) {
        var x = document.getElementById(this.id + "autocomplete-list");
        if (x) x = x.getElementsByTagName("div");
        if (e.keyCode == 40) {            
            currentFocus++;            
            addActive(x);
        } else if (e.keyCode == 38) { 
            currentFocus--;            
            addActive(x);
        } else if (e.keyCode == 13) {         
            e.preventDefault();
            if (currentFocus > -1) {            
            if (x) x[currentFocus].click();
            }
        }
    });
    function addActive(x) {        
        if (!x) return false;        
        removeActive(x);
        if (currentFocus >= x.length) currentFocus = 0;
        if (currentFocus < 0) currentFocus = (x.length - 1);        
        x[currentFocus].classList.add("autocomplete-active");
    }
    function removeActive(x) {        
        for (var i = 0; i < x.length; i++) {
        x[i].classList.remove("autocomplete-active");
        }
    }
    function closeAllLists(elmnt) {
        var x = document.getElementsByClassName("autocomplete-items");
        for (var i = 0; i < x.length; i++) {
        if (elmnt != x[i] && elmnt != inp) {
        x[i].parentNode.removeChild(x[i]);
        }
    }
    }    
    document.addEventListener("click", function (e) {
        closeAllLists(e.target);
    });
    }