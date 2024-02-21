const button = document.createElement("button");
const input = document.createElement("input");

button.disabled = true;
button.textContent = "Submit Task";

input.addEventListener("input", function () {
	button.disabled = false;
});

//to allow enter key to submit easily
window.addEventListener("keyup", function (event) {
	if (event.key === "Enter") {
		button.click();
	}
});

button.addEventListener("click", function () {
	let task = input.value;
	input.value = "";
	button.disabled = true;
	input.focus();
	let li = document.createElement("li");
	li.textContent = task;
	document.body.appendChild(li);
	return false;
});

document.body.appendChild(button);
document.body.appendChild(input);
