console.log("Javascript conn  ected");

function openlisting(resortJson, resortId) {
	let resort = JSON.parse(resortJson)[resortId - 1]; // resorts start from 1, but array starts from 0
	listing_card = document.getElementById("listing_card");
	listing_card.style.display = "block";

	resort_name = document.getElementById("resort_name");
	resort_image = document.getElementById("resort_image");
	resort_description = document.getElementById("resort_description");
	resort_shots = document.getElementById("resort_shots");
	//resort_rating = document.getElementById("resort_rating");
	//resort_location = document.getElementById("resort_location");
	resort_amenities = document.getElementById("resort_amenities");
	//resort_url = document.getElementById("resort_url");

	console.log(resort);

	resort_name.innerHTML = resort.name;
	resort_image.src = resort.image;
	resort_description.innerHTML = resort.desc;
	//resort_rating.innerHTML = resort.rating;
	//resort_location.innerHTML = resort.location;
	//resort_url.href = resort.url;

	for (amenity in resort.amenity) {
		amenity_div = document.createElement("div");
		amenity_div.classList.add("border", "border-dark", "rounded", "amenity");

		icon = document.createElement("i");
		icon.classList.add(resort.amenityIcon[amenity], "amenity-icon");

		text = document.createElement("p");
		text.innerHTML = resort.amenity[amenity];

		amenity_div.appendChild(icon);
		amenity_div.appendChild(text);

		resort_amenities.appendChild(amenity_div);
	}

	for (shot in resort.shots) {
		shot_div = document.createElement("div");
		shot_div.classList.add("resort-shot");
		shot_div.draggable = false;

		image = document.createElement("img");
		image.src = resort.shots[shot];
		image.alt = "Resort Image";

		dark_shade = document.createElement("div");
		dark_shade.classList.add("dark-shade");

		shot_div.appendChild(image);
		shot_div.appendChild(dark_shade);

		resort_shots.appendChild(shot_div);
	}

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
