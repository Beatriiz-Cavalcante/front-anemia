document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('anemiaForm');

    form.addEventListener('submit', async function (event) {
        event.preventDefault();

        const data = {
            Number: 1,
            Sex: parseInt(form.campo1.value),
            "%Red Pixel": parseFloat(form.campo2.value),
            "%Blue pixel": parseFloat(form.campo3.value),
            "%Green pixel": parseFloat(form.campo4.value),
            Hb: parseFloat(form.campo5.value)
        };

        try {
            const response = await fetch("http://127.0.0.1:5000/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            });

            if (!response.ok) {
                const error = await response.json();
                throw new Error(error.erro || "Erro desconhecido na API.");
            }

            const result = await response.json();
            document.getElementById('resultado').innerHTML = `
                <p><strong>Resultado da Predição:</strong> ${result.predicao}</p>
            `;
        } catch (error) {
            console.error("Erro na requisição:", error.message);
            document.getElementById('resultado').innerHTML = `
                <p style="color:red;">Erro ao enviar os dados: ${error.message}</p>
            `;
        }
    });
});
