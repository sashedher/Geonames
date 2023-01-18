document.addEventListener('DOMContentLoaded', () => {
    var form = document.getElementById('my-form');
    var formData = new FormData(form);
    var cityName = document.getElementById('cityName');
    var city = document.getElementById('cityName');
    cityName.value = city.value;
    form.addEventListener('submit', (event)=>{
        getRespone(event, formData, form);
        form.reset();
    });
    
});

function getRespone(event, formData, form) {
    event.preventDefault();

    var output = document.getElementById('output');
    
    output.innerHTML = '<img style="margin-top:30px;" class="mx-auto d-block" src="../static/img/loading.gif"/>';

    var xhr = new XMLHttpRequest();
    xhr.open('POST', form.action, true);


    // Set up a handler for when the task for the request is complete.
    xhr.onload = function () {
    if (xhr.status === 200) {
        output.innerHTML = xhr.responseText;
      } else {
        output.innerHTML = 'An error occurred during the upload. Try again.';
      }
    };   
    var form = document.getElementById('my-form');
    var formData = new FormData(form);
    form.addEventListener('submit', (event)=>{
        getRespone(event, formData, form);
    });

    // Send the data.
    xhr.send(formData);
}

function closePopup(linkText){
    var city = document.getElementById('cityName');
    var title = document.getElementById('modal-title');
    city.value = linkText;
    title.innerText = linkText;
}

function submitData(){
    var form = document.getElementById('modal-form');
    var city = document.getElementById('cityName');
    var formData = new FormData(form);
    formData.append("city", city.value);
    getData(formData, form);
}

function getData(formData, form) {
    // event.preventDefault();

    var output = document.getElementById('output');
    
    output.innerHTML = '<img style="margin-top:30px;" class="mx-auto d-block" src="../static/img/loading.gif"/>';

    var xhr = new XMLHttpRequest();
    xhr.open('POST', form.action, true);


    // Set up a handler for when the task for the request is complete.
    xhr.onload = function () {
    if (xhr.status === 200) {
        output.innerHTML = xhr.responseText;
      } else {
        output.innerHTML = 'An error occurred during the upload. Try again.';
      }
    };

    // Send the data.
    xhr.send(formData);
}


