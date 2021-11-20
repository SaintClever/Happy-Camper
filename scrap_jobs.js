/*
CLASSES:
c-virtual_list__item
    c-message_kit__hover
        c-message_group
            c-message_group__header
            c-message_kit__actions c-message_kit__actions--above c-search_message__actions_container
*/





let getJobs = () => {
    let jobContainer = document.getElementsByClassName('c-message_kit__hover');
    let jobData = document.getElementsByClassName('c-search_message__body');
    let giveFeedback = document.getElementById('give-feedback-text-node')
    let jobs = [];

    for (let i = 0; i < jobContainer.length; i++) {  
        setInterval(() => {         
            while (giveFeedback == null) {
                jobs.push(jobData[0].innerHTML);
                // console.log(job_data[0].innerHTML);
                jobContainer[0].remove();
            }
        }, 5000);
    }
    // console.log(jobs);
    return jobs;
}

console.log(...getJobs());
// return ...getJobs();






// OR



// let getJobs = () => {
//     let jobContainer = document.getElementsByClassName('c-message_kit__hover');
//     let jobData = document.getElementsByClassName('c-search_message__body');
//     let giveFeedback = document.getElementById('give-feedback-text-node')
//     let jobs = [];

//     for (let i = 0; i < jobContainer.length; i++) {           
//         if (giveFeedback == null) {
//             jobs.push(jobData[0].innerHTML);
//             // console.log(job_data[0].innerHTML);
//             jobContainer[0].remove();
//         } else if (giveFeedback !== null) {
//             console.log('Jobs scraped');
//             clearInterval(setTime);
//         }
//     }
//     // console.log(jobs);
//     return jobs;
// }

// let totalJobs = [];
// let setTime = setInterval(() => {
//     totalJobs.push(...getJobs());
//     // console.log(getJobs());
// }, 5000);

// console.log(totalJobs);
// // return totalJobs;




// OR

/*
let test = () => {
    let jobContainer = document.getElementsByClassName('c-message_kit__hover');
    let jobData = document.getElementsByClassName('c-search_message__body');
    let giveFeedback = document.getElementById('give-feedback-text-node')
    let jobs = [];
    let totalJobs = [];

    let setTime = setInterval(() => {

        for (let i = 0; i < jobContainer.length; i++) {           
            if (giveFeedback == null) {
                jobs.push(jobData[0].innerHTML);
                // console.log(job_data[0].innerHTML);
                jobContainer[0].remove();
            } else if (giveFeedback !== null) {
                console.log('Jobs scraped');
                clearInterval(setTime);
            }
        }

        totalJobs.push(...jobs);
    }, 1000);

    console.log(totalJobs);
}
    return totalJobs
*/