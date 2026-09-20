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
  enableDarkMode(); 
}

toggleBtn.addEventListener("click", (e) => {
  darkMode = localStorage.getItem("dark-mode"); 
  if (darkMode === "disabled") {
    enableDarkMode();
  } else {
    disableDarkMode();
  }
});