// Ref: https://stackoverflow.com/a/4550514/3357851
function randomElement(arr) {
    return arr[Math.floor(Math.random() * arr.length)];
}

// Ref: https://stackoverflow.com/a/46545530/3357851
function randomShuffle(arr) {
    return arr
        .map((a) => ({ key: Math.random(), value: a }))
        .sort((a, b) => a.key - b.key)
        .map((a) => a.value)
}

function updatePasswordLengthLabel(value) {
    document.getElementById('password-length').innerHTML = value;
}

function generatePassword() {
    const length = document.getElementById('password-length-input').value;
    document.getElementById('password-length').innerHTML = length;

    // Should we use digits? Special characters?
    const useDigits = document.getElementById('use-digits').checked;
    const useSpecial = document.getElementById('use-special').checked;

    // Ref: https://docs.python.org/3/library/string.html#string-constants
    const upperCaseLetters = Array.from("ABCDEFGHIJKLMNOPQRSTUVWXYZ");
    const lowerCaseLetters = Array.from("abcdefghijklmnopqrstuvwxyz");
    const digits = Array.from("0123456789");
    const specialCharacters = Array.from("!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~");

    // These are the sets we'll be picking random characters from
    const charSets = [upperCaseLetters, lowerCaseLetters];
    if (useDigits) { charSets.push(digits); }
    if (useSpecial) { charSets.push(specialCharacters); }

    // Pick a random character from each of the sets in turn
    let passwordChars = [];
    for (let i = 0; i < length; ++i) {
        const nextSet = charSets[i % charSets.length];
        const randomChar = randomElement(nextSet);
        passwordChars.push(randomChar);
    }
    // Shuffle the final array, and join it to form the password.
    passwordChars = randomShuffle(passwordChars)
    const password = passwordChars.join('');

    document.getElementById('password').value = password;
}
