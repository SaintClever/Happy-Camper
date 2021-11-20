let email = document.getElementById('email');
let password = document.getElementById('password');
let job_search = document.getElementById('job_search');
let lazy_apply = document.getElementById('lazy_apply');
let add_job = document.getElementById('add_job');

let jobSearch = (userEmail, userPassword) => {
    userEmail = email.value;
    userPassword = password.value;
    eel.job_search(userEmail, userPassword);
}

job_search.addEventListener('click', () => {
    jobSearch();
    email.value = password.value = '';
})


eel.expose(addJob)
function addJob(jobListing) {
    add_job.innerHTML += jobListing + '<br><hr><br>';
}

