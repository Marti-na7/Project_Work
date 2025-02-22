document.getElementById("booking-form").addEventListener("submit", function(event) { 

    event.preventDefault(); 

 

    const codice_fiscale = document.getElementById("codice_fiscale").value; 

    const servizio = document.getElementById("servizio").value; 

    const data = document.getElementById("data").value; 

    const ora = document.getElementById("ora").value; 

    const consulente = document.getElementById("consulente").value; 

 

    fetch("http://127.0.0.1:5000/book", { 

        method: "POST", 

        headers: { "Content-Type": "application/json" }, 

        body: JSON.stringify({ codice_fiscale, servizio, data_appuntamento: data, ora, consulente }) 

    }) 

    .then(response => response.json()) 

    .then(data => alert(data.message)) 

    .catch(error => console.error("Errore:", error)); 

}); 
