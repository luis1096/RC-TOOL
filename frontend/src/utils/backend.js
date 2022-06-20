import axios from 'axios';
import { BE_URL, convertResponse } from './globals';

// Should wait for temperature and extruder
export const getTestTemp = async buffer => {
    let message;

    await axios.get(`${BE_URL}/test`) 
        .then(res => message = "Backend Response: " + JSON.stringify(res.data, null, '\t'))
        .catch(err => console.log(`Error: ${err}`))
        
    buffer.value += `${message}\n`
}

// should cancel any jobs
// should cancel specific job [optional]
export const postTestTemp = async (buffer, temperature) => {
    let message;
    const data = {temperature}

    await axios.post(`${BE_URL}/post-test`, data)
        .then(res => message = JSON.stringify(res.data))
        .catch(err => console.log(`Error: ${err}`))

    buffer.value += `${message}\n`
}

export const postTestExtrude = async (buffer, extrudeRate) => {
    let message;
    const data = {extrudeRate}

    await axios.post(`${BE_URL}/post-test`, data)
        .then(res => message = JSON.stringify(res.data))
        .catch(err => console.log(`Error: ${err}`))

    buffer.value += `${message}\n`
}


// [check setInterval and how to cancel it]
export const checkTemperature = axios.get(`${BE_URL}/`) // should be called by sendPrintJob 