const URL_API = "http://127.0.0.1:5000/";

function generateChart(name, min, max) {
    let ctx = document.getElementById(name)
    let myChart = new Chart(ctx, {
        type: 'line',
        data: {
            datasets: [{
                backgroundColor: [
                    'rgba(54, 162, 235, 0.2)',
                ],
                borderColor: [
                    'rgba(255,99,132,1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                xAxes: [{
                    type:       "time",
                    distribution: 'linear',
                    time: {
                        unit: 'minute'
                    },
                        scaleLabel: {
                            display: true,
                            labelString: 'Date'
                        },
                    ticks: {
                        source: 'data'
                    }
                }],
                yAxes: [{
                    distribution: 'linear',
                    ticks: {
                        min: min,
                        max: max
                    }
                }]
            }
        }
    });

    setInterval(() => {
        fetch(URL_API + "chart/" + name, {method: 'GET',
               headers: new Headers(),
               mode: 'cors'})
            .then((response) => {
                return response.json();
            })
            .then((data) => {
                if(data != "null" && data != "") {
                    let dataChart = myChart.data.datasets[0].data;
                    if(dataChart.length > 14) {
                        dataChart.shift();
                    }
                    dataChart.push(data);

                    console.log("Update : " + data['x']);
                    myChart.update();
                }
            })
            .catch((error) => {
                console.log("Error : " + error);
            });
    }, 1000);
}

function generateToast(text, config) {
    let toastContainer = document.getElementById("toast-container");

    let toast = document.createElement("div");
    toast.setAttribute("class", "toast");
    switch (config.type) {
        case 'info':
            toast.classList.add("toast-info");
            break;
        case 'error':
            toast.classList.add("toast-error");
            break;
    default:

}

    toast.innerHTML = text;
    toastContainer.appendChild(toast);

    setTimeout(() => {
        reduceToast(toast);
    }, (Math.random() * (3000 - 1000) + 3000));
}

function reduceToast(e) {
    var ih = e.clientHeight;
    var duration = 500;
    var rep = ih / duration;
    var t = 0;
    e.style.opacity = '1';
    var id2;

    var id = setInterval(function () {
            var h = e.clientHeight - 2;
             e.style.height = h + 'px';

             var o = parseFloat(e.style.opacity)
             e.style.opacity = o - 0.01;
             t += 1;

            if(h <= 0) {
                t = e.parentNode.clientHeight;
                console.log(t);
                id2 = setInterval(function() {
                    var a = 0;
                    t -= 3;
                    t = ( t <= 0) ? 0 : t;
                    e.parentNode.style.height = t + 'px';
                    if(t <= -100) {
                        e.parentNode.style.display = "none";
                        e.parentNode.removeChild(e);
                        clearInterval(id2);
                    }
                }, 20);
                clearInterval(id);
            }
    }, 5);
}

function sendData(element) {
    let formParent = element.parentNode;
    let formData = new FormData(formParent);

    var myInit = {  method: 'POST',
                    mode: 'no-cors',
                    body: formData,
                    header: { 'Content-Type' : 'multipart/form-data'}
                 };

    fetch("http://127.0.0.1:5000/user", myInit)
        .then((response) => {
          console.log("Cool");
          generateToast("Données envoyées", {'type': 'info'});
        })
        .catch((error) => {
            generateToast("Erreur", {'type': 'error'});
        });
}

function updateActionneur(url, value) {
    var config = {  method: 'PUT',
                    mode: 'no-cors',
                    body: { 'value': value},
                    header: { 'Content-Type' : 'application/json'}
                 };

    fetch(url, config)
        .then((response) => {
            generateToast("Données envoyées", {'type': 'info'});
        })
        .catch((error) => {
            generateToast("Erreur", {'type' : 'error'});
        })
}
