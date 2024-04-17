function openlisting(resortId) {
	resortId = resortId - 2; // We subtract 2 because the resortId Json starts from 2, but the array starts from 0
	learn_more = document.getElementById("learn_more_btn");
	rawResortData = learn_more.getAttribute("data-info");
	resortJson = rawResortData.replace(/'/g, '"');
	let resort = JSON.parse(resortJson)[resortId]; // resorts start from 1, but array starts from 0

	listing_card = document.getElementById("listing_card");
	listing_card.style.display = "block";

	resort_name = document.getElementById("resort_name");
	resort_image = document.getElementById("resort_image");
	resort_description = document.getElementById("resort_description");
	resort_shots = document.getElementById("resort_shots");
	resort_amenities = document.getElementById("resort_amenities");
	resort_trending = document.getElementById("resort_trending");

	resort_name.innerHTML = resort.name;
	resort_image.src = resort.image;
	resort_description.innerHTML = resort.desc;
	resort_trending.innerHTML = `Trending at the ${resort.name} `;
	resort;
	amenityArray = resort.amenities.split(",");
	for (i = 0; i < amenityArray.length; i++) {
		amenity_div = document.createElement("div");
		amenity_div.classList.add("border", "border-dark", "rounded", "amenity");
		text = document.createElement("p");
		text.innerHTML = amenityArray[i];

		// amenity_div.appendChild(icon);
		amenity_div.appendChild(text);

		resort_amenities.appendChild(amenity_div);
	}

	for (i = 0; i < images.length; i++) {
		shot_div = document.createElement("div");
		shot_div.classList.add("resort-shot");
		shot_div.draggable = false;

		image = document.createElement("img");
		image.src = images[i];
		image.alt = "Resort Image";

		dark_shade = document.createElement("div");
		dark_shade.classList.add("dark-shade");

		shot_div.appendChild(image);
		shot_div.appendChild(dark_shade);

		resort_shots.appendChild(shot_div);
	}
	const listingDisplayCard = document.getElementById("listing_card");
	listingDisplayCard.style.top = `${scrollY + 40}px`;
}

function closelisting() {
	console.log("Close listing clicked");
	listing_card = document.getElementById("listing_card");
	const elements_to_unstage = Array.from(document.querySelectorAll(".amenity #resort_trending"));
	elements_to_unstage.forEach((element) => {
		element.remove();
	});
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
			const h2Element = card.querySelector("#component_card_title"); // Retrieve the title element
			console.log("ELEMENT", h2Element.innerHTML);
			if (h2Element.innerHTML.toUpperCase().includes(input.value.toUpperCase())) { // Check if the title contains the searched value
				card.style.display = "block";
				console.log("found")
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

const images = [
	"https://images.pexels.com/photos/4825719/pexels-photo-4825719.jpeg?auto=compress&cs=tinysrgb&w=600",
	"https://images.pexels.com/photos/4993046/pexels-photo-4993046.jpeg?auto=compress&cs=tinysrgb&w=600",
	"https://images.pexels.com/photos/6394559/pexels-photo-6394559.jpeg?auto=compress&cs=tinysrgb&w=600",
	"https://images.pexels.com/photos/6130081/pexels-photo-6130081.jpeg?auto=compress&cs=tinysrgb&w=600",
	"https://images.pexels.com/photos/18185785/pexels-photo-18185785/free-photo-of-deckchairs-and-umbrellas-on-beach-in-alghero-italy.jpeg?auto=compress&cs=tinysrgb&w=600",
	"https://images.pexels.com/photos/18201284/pexels-photo-18201284/free-photo-of-thatched-houses-on-fishermans-island-in-le-barcares.jpeg?auto=compress&cs=tinysrgb&w=600",
	"https://images.pexels.com/photos/3144978/pexels-photo-3144978.jpeg?auto=compress&cs=tinysrgb&w=600",
	"https://images.pexels.com/photos/4577191/pexels-photo-4577191.jpeg?auto=compress&cs=tinysrgb&w=600",
	"https://images.pexels.com/photos/2631613/pexels-photo-2631613.jpeg?auto=compress&cs=tinysrgb&w=600",
	"https://images.pexels.com/photos/338504/pexels-photo-338504.jpeg?auto=compress&cs=tinysrgb&w=600",
];
