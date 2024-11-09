function generatePassword() {
    const length = document.getElementById("passwordLength").value;
    const useLowercase = document.getElementById("useLowercase").checked;
    const useUppercase = document.getElementById("useUppercase").checked;
    const useNumbers = document.getElementById("useNumbers").checked;
    const useSymbols = document.getElementById("useSymbols").checked;
    const excludeSimilar = document.getElementById("excludeSimilar").checked;
    const excludeAmbiguous = document.getElementById("excludeAmbiguous").checked;

    fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            length: length,
            use_lowercase: useLowercase,
            use_uppercase: useUppercase,
            use_numbers: useNumbers,
            use_symbols: useSymbols,
            exclude_similar: excludeSimilar,
            exclude_ambiguous: excludeAmbiguous
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("passwordOutput").value = data.password;
    })
    .catch(error => console.error('Error:', error));
}

function copyToClipboard() {
    const passwordField = document.getElementById("passwordOutput");
    passwordField.select();
    document.execCommand("copy");
    alert("Password copied to clipboard!");
}
