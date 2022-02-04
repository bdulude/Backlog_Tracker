
function searchMovie(){
    let query = document.getElementById("searchInput").value
    query = encodeURIComponent(query.trim())
    query = "q=" + query
    document.getElementById("hidden").value = query
    document.getElementById("search").submit()
}


document.getElementById('searchInput').onkeydown = function(e){
    if(e.keyCode == 13){
        searchMovie()
    }
};











// function createMovieQuery() {
//     let query = document.getElementById("search").value
//     query = encodeURIComponent(query.trim())
//     return "q=" + query
// }
// createMovieQuery("Fellowship of the Ring")
// function parseMovieResponse(resp) {
//     let output = {}
//     output['title'] = resp.title
//     output['synopsis'] = resp.summary.plot
//     output['rating'] = resp.UserRating.rating
//     output['image'] = resp.small_poster
//     console.log(output)
//     return output
// }
// function getMovie() {
//     var url = "http://betterimdbot.herokuapp.com"
//     var xhr = new XMLHttpRequest()
//     xhr.open("POST", url)
//     xhr.setRequestHeader("accept", "application/json")
//     xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded")
//     xhr.setRequestHeader("Access-Control-Allow-Origin", '*')

//     var data = createMovieQuery("Fellowship of the Ring")
//     console.log(xhr)
//     xhr.send(data)
//     xhr.onreadystatechange = function () {
//         if (xhr.readyState === 4) {
//             console.log(xhr.status)
//             // console.log(JSON.parse(xhr.responseText)[1])
//             parseMovieResponse(JSON.parse(xhr.responseText)[1])
//     }}
// }
// // Example POST method implementation:
// async function postData(url = "https://betterimdbot.herokuapp.com", data = { 'data': "q=Fellowship%20of%20the%20Ring"}) {
//     // Default options are marked with *
//     const response = await fetch(url, {
//         method: 'POST', // *GET, POST, PUT, DELETE, etc.
//         mode: 'cors', // no-cors, *cors, same-origin
//         cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
//         credentials: 'omit', // include, *same-origin, omit
//         headers: {
//             'accept': 'application/json',
//             'Content-Type': 'application/x-www-form-urlencoded',
//             "Access-Control-Allow-Origin" : "*"
//         },
//         redirect: 'follow', // manual, *follow, error
//         crossDomain: true,
//         referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
//         body: JSON.stringify(data) // body data type must match "Content-Type" header
//     });
//     return response.json(); // parses JSON response into native JavaScript objects
//     }
    
//     postData('https://betterimdbot.herokuapp.com', { 'data': "q=Fellowship%20of%20the%20Ring"})
//     .then(data => {
//       console.log(data); // JSON data parsed by `data.json()` call
//     });


