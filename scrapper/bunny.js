var request = require('bluebird').promisifyAll(require('request')),
    cheerio = require('cheerio');



function bunny() {
	var url = 'http://joblist.bdjobs.com/jobsearch.asp?fcatId=8';
	var j = request.jar();
	j.setCookie(request.cookie('JOBSRPP=40'), url);   //set 40 results per page
	var options = {
        url: url,
        headers: {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'
        },
        jar: j
    };

    request.getAsync(options).spread(function(response, body) {
    	if (response.statusCode == 200)
        throw new Error('Unsuccessful attempt. Code: ' + response.statusCode);
    	console.log(body);
    	return body;
    }).then(function(data) {
    	console.log(data);
    }).catch(function(err){
    	console.log(err);
    });
}