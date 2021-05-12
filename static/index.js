function productBuy(test) {
    fetch("/buy-product", {
      method: "POST",
      body: JSON.stringify({ test: test }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }