/*
function changebody() {
  var element = document.body;
  element.classList.toggle("darkmode");
} */

const toggleBtn = document.getElementById("theme-toggler");
const body = document.body;
let darkMode = localStorage.getItem("dark-mode");

const enableDarkMode = () => {
  body.classList.add("darkmode");
  localStorage.setItem("dark-mode", "enabled");
};

const disableDarkMode = () => {
  body.classList.remove("darkmode");
  localStorage.setItem("dark-mode", "disabled");
};

if (darkMode === "enabled") {
  enableDarkMode(); // set state of darkMode on page load
}

toggleBtn.addEventListener("click", (e) => {
  darkMode = localStorage.getItem("dark-mode"); // update darkMode when clicked
  if (darkMode === "disabled") {
    enableDarkMode();
  } else {
    disableDarkMode();
  }
});