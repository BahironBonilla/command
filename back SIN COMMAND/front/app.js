const apiUrl = "http://localhost:8000"; // Cambia esto si tu API está en otra dirección

async function sendCommand(endpoint) {
    try {
        // Realiza la solicitud con fetch
        const response = await fetch(`${apiUrl}${endpoint}`, { method: "POST" });

        // Verifica si la respuesta es correcta
        if (!response.ok) {
            throw new Error(`Error ${response.status}: ${response.statusText}`);
        }

        // Intenta obtener el resultado como JSON
        const result = await response.json();
        displayResponse(result);
    } catch (error) {
        // Muestra un error claro en la interfaz
        displayResponse({ error: error.message });
    }
}

function displayResponse(response) {
    const output = document.getElementById("output");
    output.textContent = JSON.stringify(response, null, 2);
}
