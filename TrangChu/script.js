
const games = [
    {
        name: "Minecraft",
        category: "Phiêu lưu",
        rating: "⭐⭐⭐⭐⭐",
        image: "https://images.unsplash.com/photo-1607513746994-51f730a44832?w=500",
        popular: true
    },
    {
        name: "Đua xe tốc độ",
        category: "Đua xe",
        rating: "⭐⭐⭐⭐⭐",
        image: "https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=500",
        popular: true
    },
    {
        name: "Chiến trường",
        category: "Bắn súng",
        rating: "⭐⭐⭐⭐",
        image: "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=500",
        popular: true
    },
    {
        name: "Bóng đá",
        category: "Thể thao",
        rating: "⭐⭐⭐⭐⭐",
        image: "https://images.unsplash.com/photo-1574629810360-7efbbe195018?w=500",
        popular: true
    },
    {
        name: "Phiêu lưu rừng xanh",
        category: "Phiêu lưu",
        rating: "⭐⭐⭐⭐",
        image: "https://images.unsplash.com/photo-1511497584788-876760111969?w=500",
        popular: false
    },
    {
        name: "Đấu trường",
        category: "Hành động",
        rating: "⭐⭐⭐⭐⭐",
        image: "https://images.unsplash.com/photo-1547394765-185e1e68f34e?w=500",
        popular: false
    },
    {
        name: "Thành phố tương lai",
        category: "Mô phỏng",
        rating: "⭐⭐⭐⭐",
        image: "https://images.unsplash.com/photo-1519608487953-e999c86e7455?w=500",
        popular: false
    },
    {
        name: "Thử thách trí tuệ",
        category: "Giải đố",
        rating: "⭐⭐⭐⭐⭐",
        image: "https://images.unsplash.com/photo-1606092195730-5d7b9af1efc5?w=500",
        popular: false
    }
];

function displayGames(data, elementId) {
    const container = document.getElementById(elementId);
    container.innerHTML = "";

    if (data.length === 0) {
        container.innerHTML = "<p>Không tìm thấy trò chơi!</p>";
        return;
    }

    data.forEach(game => {
        const card = document.createElement("div");
        card.className = "game-card";

        const img = document.createElement("img");
        img.src = game.image;
        img.alt = game.name;

        const info = document.createElement("div");
        info.className = "game-info";

        const title = document.createElement("h3");
        title.textContent = game.name;

        const category = document.createElement("p");
        category.textContent = game.category;

        const rating = document.createElement("div");
        rating.className = "rating";
        rating.textContent = game.rating;

        info.append(title, category, rating);
        card.append(img, info);
        container.appendChild(card);
    });
}

function filterGame(category) {
    const result = category === "all"
        ? games
        : games.filter(game => game.category === category);

    displayGames(result, "gameList");

    document.getElementById("newGames").scrollIntoView({
        behavior: "smooth"
    });
}

function searchGame() {
    const keyword = document.getElementById("searchInput")
        .value.trim().toLowerCase();

    const result = games.filter(game =>
        game.name.toLowerCase().includes(keyword)
    );

    displayGames(result, "gameList");
}

document.querySelectorAll(".sidebar a").forEach(item => {
    item.addEventListener("click", function() {
        filterGame(this.dataset.category);
    });
});

document.getElementById("searchButton")
    .addEventListener("click", searchGame);

document.getElementById("searchInput")
    .addEventListener("keydown", function(e) {
        if (e.key === "Enter") searchGame();
    });

document.getElementById("exploreButton")
    .addEventListener("click", function() {
        document.getElementById("newGames").scrollIntoView({
            behavior: "smooth"
        });
    });

displayGames(games, "gameList");
displayGames(
    games.filter(game => game.popular),
    "popularList"
);
