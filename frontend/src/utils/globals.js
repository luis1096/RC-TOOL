// convert to .env property
export const BE_URL = process.env.REACT_APP_BE || 'http://localhost:5000';
export const convertResponse = res => console.log(res)

// handler for cleaning promises in backend
export const handlePath = (pathPromise, message) => pathPromise
    .then(convertResponse)
    .then(res => message = res)
    .catch(err => console.log(`Error: ${err}`))