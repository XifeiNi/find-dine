 async function makeRequest (data, endpoint, type) {
    console.log('works')
    const url = `${window.location.origin}${endpoint}`;
    const body = JSON.stringify(data);
    const method = type;
    const headers = { 'content-type': 'application/json' };
    let response, status;
    try {
        if (type === 'POST')
            response = await fetch(url, {method, headers, body});
        else
            response = await fetch(url, {method});
        status = response.status;
        response = await response.json();
    } catch (e) {
        return { message: e.message };
    }
    if (status !== 200)
        return { message: `Error Status: ${status}` };
    return response;
}

makeElement = (label, id, data) => {
    const p = document.createElement('p');
    const key = document.createElement('span');
    const value = document.createElement('span');
    if (label)
        key.appendChild(document.createTextNode(label + ': '));
    value.appendChild(document.createTextNode(data));
    value.id = id;
    p.appendChild(key);
    p.appendChild(value);
    return p
};