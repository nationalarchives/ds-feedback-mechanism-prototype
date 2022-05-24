/**
 * Returns a promise that will reject after the delay specified in the delay parameter
 * @param {number} delay - Delay in milliseconds before promise will reject
 * @returns {Promise}
 */

export const reject_on_time_out = delay => {
    return new Promise(function (resolve, reject) {
        setTimeout(() => reject(`Timed out after ${delay}`), delay)
    });
};