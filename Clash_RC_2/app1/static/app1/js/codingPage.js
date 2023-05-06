let editor1 = document.querySelector("#editor1");
ace.edit(editor1, {
  theme: "ace/theme/cobalt",
});

const langSelect = document.getElementById('langbtn');
// Create an Ace editor instance
const editor = ace.edit('editor1');

//added by me(prash) to hide vertical line and also select default value to python
editor.setShowPrintMargin(false);
//by prash
// editor.session.setMode(`ace/mode/python`);
// editor.session.setValue("");
// editor.session.setValue("#Write the Python code.....");


//by prash
const userDetails = JSON.parse(document.body.getAttribute('userDetails'));
console.log("user ",userDetails.user,"Question nuber ",userDetails.questionNumber)

// editor.session.setValue(" Select the language First and then Start the Coding .");

// Add an event listener to the select element
langSelect.addEventListener('change', function() {
 
  //by prash
  let userObject = JSON.parse(localStorage.getItem(userDetails.user));
  if (userObject){
    console.log("inside editor")
  }else{
    createUserWholeObject(userDetails.user,userDetails.questionNumber);
  }

  const selectedLang = langSelect.value;

  // Set the mode of the Ace editor based on the selected language  and set the boier plate accordingly   
    if(selectedLang ==='cpp'){
      console.log("inside editor cpp")
      var storedCode;
      try {
        storedCode = userObject[userDetails.questionNumber][1].cpp;
        console.log("code pyrkllj",storedCode)
      } catch (error) {
        createUserQuestionObject(userDetails.user,userDetails.questionNumber)
        storedCode = userObject[userDetails.questionNumber][1].cpp;
      }
      editor.session.setMode(`ace/mode/c_cpp`);
      // editor.session.setValue("");
      editor.session.setValue(storedCode); 
      
    }
    if(selectedLang ==='c'){
      console.log("inside editor c")
      editor.session.setMode(`ace/mode/c_cpp`);
      // editor.session.setValue("");
    //   let storedCode = userObject[userDetails.questionNumber][2].c;
    // console.log("code pyrkllj",storedCode)
    var storedCode;
      try {
        storedCode = userObject[userDetails.questionNumber][2].c;
        console.log("code pyrkllj",storedCode)
      } catch (error) {
        createUserQuestionObject(userDetails.user,userDetails.questionNumber)
        storedCode = userObject[userDetails.questionNumber][2].c;
      }
      editor.session.setValue(userObject[userDetails.questionNumber][2].c);
    }
  
  if(selectedLang ==='python'){
    console.log("inside editor py")
    editor.session.setMode(`ace/mode/${selectedLang}`);
    // editor.session.setValue("");
    // let storedCode = userObject[userDetails.questionNumber][0].py;
    // console.log("code pyrkllj",storedCode)
    var storedCode;
      try {
        storedCode = userObject[userDetails.questionNumber][0].py;
        console.log("code pyrkllj",storedCode)
      } catch (error) {
        createUserQuestionObject(userDetails.user,userDetails.questionNumber)
        storedCode = userObject[userDetails.questionNumber][0].py;
      }
    editor.session.setValue(userObject[userDetails.questionNumber][0].py);
    
  }

});





// code for choosing only the suppoirted files only c cpp and python 
const fileInput = document.getElementById("customFile");

fileInput.addEventListener("change", function() {
  const file = fileInput.files[0];
  const fileName = file.name;
  const fileExtension = fileName.split(".").pop();
  console.log(fileExtension)

  if (fileExtension !== "cpp" && fileExtension !== "c" && fileExtension !== "py") {
    fileInput.value = "";
    alert("Unsupported file format. Please select a C++, C, or Python file.");
    return;
  }
});




//code for scrolling on to the status div 


// const submitBtn = document.querySelector('#submit-btn');
const submitBtn = document.querySelector('#submit_code');
const consoleBtn=document.querySelector('#console-btn');
const statusDiv = document.querySelector('.Status');
const consoleDiv = document.querySelector('.consoleBlocks');

submitBtn.addEventListener('click', () => {
  statusDiv.scrollIntoView({ behavior: 'smooth' });
});
consoleBtn.addEventListener('click', () => {
  consoleDiv.scrollIntoView({ behavior: 'smooth' });
});



//console buttons onclicke events 

var consoleBtnn = document.getElementById("console-btn");
var consoleBtnDown = consoleBtnn.querySelector(".down");
var consoleBtnUp = consoleBtnn.querySelector(".up");

consoleBtnn.addEventListener("click", function() {
  if (consoleBtnDown.classList.contains("hidden")) {
    consoleBtnDown.classList.remove("hidden");
    consoleBtnUp.classList.add("hidden");
  } else {
    consoleBtnDown.classList.add("hidden");
    consoleBtnUp.classList.remove("hidden");
  }
});



// console.log(user_code)
// user={
//   1:{
//     "py"="code",
//     "cpp"="code",
//   },
//   2:{
//     "ip":"ipppp"
//   },
// }


editor.getSession().on('change', function() {
  // let userDetails = JSON.parse(document.body.getAttribute('userDetails'));


  let code_lang = $("#langbtn").val();
  var userCode = editor.getValue();
  // console.log(userCode);
  // console.log("lang ",code_lang);
  let userObject = JSON.parse(localStorage.getItem(userDetails.user));
  if (userObject){
    console.log("User is present");
    // console.log(typeof(userObject))
    if(userObject[userDetails.questionNumber]){
      // console.log("question ",userObject[userDetails.questionNumber],"is present")
        // userObject[userDetails.questionNumber[code_lang]] = userCode;
      if (code_lang === "python"){
        console.log("in python")
        userObject[userDetails.questionNumber][0].py = userCode;
      }else if(code_lang === "cpp"){
        console.log("in cpppp")
        userObject[userDetails.questionNumber][1].cpp = userCode;
      }else if(code_lang === "c"){
        console.log("in ccccccccc")
        userObject[userDetails.questionNumber][2].c = userCode;
      }else{
        alert("something dkjskjfsod");
      }
      localStorage.setItem(userDetails.user,JSON.stringify(userObject));
    }else{
      console.log("question is createing")
      createUserQuestionObject(userDetails.user,userDetails.questionNumber);
      // let questionNumberList = userObject[userDetails.questionNumber];
      // questionNumberList.push({code_lang:userCode});
      // userObject[userDetails.questionNumber] = questionNumberList;
    }
  }else{
    // localStorage.setItem(userDetails.user,JSON.stringify({userObject[userDetails.questionNumber]:}));
    createUserWholeObject(userDetails.user,userDetails.questionNumber);
  }
  // Do something with the user's code here
});

// var user = JSON.parse(document.body.getAttribute('userDetails'));
// console.log("user deta",user)
// console.log("user deta",user.questionNumber)

function createUserWholeObject(userr,questionNumberr) {
  qu = parseInt(questionNumberr)
  // console.log("userr ",userr,"questionnumber",typeof(qu),qu);
  let codeLangList = [{"py":"#Write the Python code....."},
  {"cpp":"#include<bits/stdc++.h>\nusing namespace std;\nint main(){\n\n\n\t\t//write your code here \n\t\treturn 0;\n}"},
  {"c":"#include<stdio.h>\n\n void main(){\n\n\n\t\t//write your code here \n\t\treturn 0;\n}"}
  ];
  let questionNumberObject={};
  questionNumberObject[qu] =codeLangList;
  localStorage.setItem(userr,JSON.stringify(questionNumberObject));
  // l = JSON.parse(localStorage.getItem(userr));
  // console.log("dfsfs",l);
}
function createUserQuestionObject(userr,questionNumberr) {
  qu = parseInt(questionNumberr)
  // console.log("userr ",userr,"questionnumber",typeof(qu),qu);
  let codeLangList = [{"py":"#Write the Python code....."},
  {"cpp":"#include<bits/stdc++.h>\nusing namespace std;\nint main(){\n\n\n\t\t//write your code here \n\t\treturn 0;\n}"},
  {"c":"#include<stdio.h>\n\n void main(){\n\n\n\t\t//write your code here \n\t\treturn 0;\n}"}
  ];
  let userObjectr = JSON.parse(localStorage.getItem(userr));
  console.log("inside createUserQuestionObject before ",userObjectr);
  userObjectr[qu]=codeLangList;
  localStorage.setItem(userr,JSON.stringify(userObjectr));
}




