let csrf = document.querySelector("input[name=csrfmiddlewaretoken]").value

function createOrder() {
    return fetch("http://localhost:8000/order",
        {
            "credentials": "include",
            "headers": {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control": "max-age=0",
                "content-type": "application/x-www-form-urlencoded",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1"
            },
            "referrer": "http://localhost:8000/",
            "referrerPolicy": "no-referrer-when-downgrade",
            "body": "csrfmiddlewaretoken=" + csrf + "&product=1&qty=1&customer_id=100&is_vip=on&submit=add",
            "method": "POST",
            "mode": "cors",
            "redirect": "manual"
        });
}

function deleteOrder(id) {
    return fetch("http://localhost:8000/order/" + id + "/",
        {
            "credentials": "include",
            "headers": {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control": "max-age=0",
                "content-type": "application/x-www-form-urlencoded",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1"
            },
            "referrer": "http://localhost:8000/",
            "referrerPolicy": "no-referrer-when-downgrade",
            "body": "csrfmiddlewaretoken=" + csrf + "&method=DELETE",
            "method": "POST",
            "mode": "cors",
            "redirect": "manual"
        });
}

// base = should be db auto increment current number for order table
let base = 0
let length = 50

// // create 50 order
let start = base
let end = start + length
for (let i = start; i < end; i++) {
    setTimeout(function () {
        createOrder()
    }, 1)
}

// trying to create and delete at the same time
for (let i = start; i < end; i++) {
    setTimeout(function () {
        deleteOrder(i)
        createOrder()
    }, 1000)
}

// delete 50 orders
start = end
end = end + length
for (let i = start; i <= end; i++) {
    setTimeout(function () {
        deleteOrder(i)
    }, 1500)
}

// check the product 1 stock pcs
// there is no order exists product 1 stock pcs should be the same as before we test
