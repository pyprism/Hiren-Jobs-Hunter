/**
 * Created by prism on 4/15/16.
 */
var request = require('request'),
    cheerio = require('cheerio');


module.exports = function () {
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

    request(options, function (error, response, body) {
        if (!error && response.statusCode == 200) {
            $ = cheerio.load(body);
            var res = $('.job_title_text').text();
            console.log(res);
            console.log(res.length);
        }
    })
}