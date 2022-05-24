import { reject_on_time_out } from "./modules/reject_on_time_out";

Promise
    .race([
        fetch('/get-banner-content'),
        reject_on_time_out(5000)
    ])
    .then(response => {
        if (response.ok === true) {
            return response.json();
        }
        throw new Error('Response received but was not OK');
    })
    .then(response => console.log(response))
    .catch(err => console.log(err));