console.log("Javascript conn  ected");

function openlisting(Obj) {
	listing_card = document.getElementById("listing_card");
	listing_card.style.display = "block";

	console.log(Obj);
}

function closelisting() {
	console.log("Close listing clicked");
	listing_card = document.getElementById("listing_card");
	listing_card.style.display = "none";
}

function search(search_or_cancel) {
	input = document.getElementById("search_input");
	cancel = document.getElementById("cancel_search");

	if (search_or_cancel == "search") {
		console.log(input.value);
		cancel.style.display = "block";
		cards = document.getElementsByClassName("card-component");
		for (i = 0; i < cards.length; i++) {
			card = cards[i];
			card.style.display = "none";
			if (card.innerHTML.toUpperCase().includes(input.value.toUpperCase())) {
				card.style.display = "block";
			}
		}
	} else if (search_or_cancel == "cancel") {
		input.value = "";
		cancel.style.display = "none";
		cards = document.getElementsByClassName("card-component");
		for (i = 0; i < cards.length; i++) {
			card = cards[i];
			card.style.display = "block";
		}
	}
}
