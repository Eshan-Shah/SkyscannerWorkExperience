

function submitUserData() {
    const name = document.getElementById("name");
    const nameValue = name.value;
    
    const email = document.getElementById('email');
    const emailValue = email.value;

    return [nameValue, emailValue]

}


async function getData() {


    let [name, email] = submitUserData()
    const url = `http://localhost:8000/form/?name=${name}&email=${email}`
    const response = await fetch(url)

    .then((response) => {
        return response.json()
    })

    .then((responseData) => {
        if (responseData == 'Thanks') {
            window.location.href = "submitted.html"
        }

        else {
            window.location.href = "invalid.html"
        }

    })

    // window.location.href()

}