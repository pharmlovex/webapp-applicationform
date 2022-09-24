const prevBtns = document.querySelectorAll(".btn-prev");
const nextBtns = document.querySelectorAll(".btn-next");
const progress = document.getElementById("progress");
const formSteps = document.querySelectorAll(".form-step");
const progressSteps = document.querySelectorAll(".progress-step");



let formStepsNum = 0;

nextBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    formStepsNum++;
    updateFormSteps();
    updateProgressbar();
  });
});

prevBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    formStepsNum--;
    updateFormSteps();
    updateProgressbar();
  });
});

function updateFormSteps() {
  formSteps.forEach((formStep) => {
    formStep.classList.contains("form-step-active") &&
      formStep.classList.remove("form-step-active");
  });

  formSteps[formStepsNum].classList.add("form-step-active");
}

function updateProgressbar() {
  progressSteps.forEach((progressStep, idx) => {
    if (idx < formStepsNum + 1) {
      progressStep.classList.add("progress-step-active");
    } else {
      progressStep.classList.remove("progress-step-active");
    }
  });

  const progressActive = document.querySelectorAll(".progress-step-active");

  progress.style.width =
    ((progressActive.length - 1) / (progressSteps.length - 1)) * 100 + "%";
}




console.log(formSteps);









let btnAdd = document.querySelector('.btn-add');

btnAdd.addEventListener('click', function(){
    addform = document.getElementById("repeatform").innerHTML
    inputform= document.getElementById("repeatform")
    document.insertBefore(addform, inputform)
});



// script>
// // Create a "li" element:
// const newNode = document.createElement("li");
// // Create a text node:
// const textNode = document.createTextNode("Water");
// // Append text node to "li" element:
// newNode.appendChild(textNode);

// // Insert before existing child:
// const list = document.getElementById("myList");
// list.insertBefore(newNode, list.children[0]);
// </script><