<html><head></head><body><script type="text/javascript" id="dcoder_script">function calculateBMI() {
    let weight = parseFloat(document.getElementById("weight").value);
    let height = parseFloat(document.getElementById("height").value);
    let resultBox = document.getElementById("result");
    let statusBox = document.getElementById("status-box");
    let statusMessage = document.getElementById("status-message");

    // التحقق من صحة الإدخال
    if (isNaN(weight) || isNaN(height) || weight <= 0 || height <= 0) {
        alert("⚠ الرجاء إدخال قيم صحيحة للوزن والطول.");
        return;
    }

    let apiUrl = `/calculate_bmi?weight=${weight}&height=${height}`;

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            let bmi = data.bmi.toFixed(2);
            let message = data.message;

            resultBox.innerHTML = `<p><strong>BMI:</strong> ${bmi}</p>`;
            resultBox.classList.add("show");

            statusMessage.innerText = message;
            statusBox.style.display = "block";
        })
        .catch(error => {
            console.error("خطأ:", error);
            resultBox.innerHTML = "⚠ حدث خطأ، تأكد من تشغيل API بشكل صحيح.";
        });
}</script></body></html>