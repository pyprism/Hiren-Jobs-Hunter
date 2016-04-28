/**
 * Created by prism on 4/15/16.
 */
/*
var request = require('request'),
    cheerio = require('cheerio').
    async = require('async');


//module.exports = function () {
function  x () {
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

    var url = [];
    request(options, function (error, response, body) {
        if (!error && response.statusCode == 200) {
            $ = cheerio.load(body);
           // var res = $('.job_title_text a').text();
            var res = $('.job_title_text a').get();
            res.map(function (x) {
               // url.push('http://joblist.bdjobs.com/' + x['attribs']['href']);
                var option = {
                    url: 'http://joblist.bdjobs.com/' + x['attribs']['href'],
                    jar: j
                };
                i = 0
                request(option, function (error, response, body) {
                    if (!error && response.statusCode == 200) {
                        $ = cheerio.load(body);
                       var text = $('.comp_wrapper').text();
                        //new RegExp($('.comp_wrapper').text(), 'ig');
                        if(text.match(/nodejs/ig))
                            url['python'] = 'http://joblist.bdjobs.com/' + x['attribs']['href'];
                        i = i + 1;
                        console.log(i)
                    }
                    console.log(url);
                    });
                //console.log(url);
            });
        }
    })


}

x();*/
var request = require('request-promise'),
    cheerio = require('cheerio');


function x() {
    var url = 'http://joblist.bdjobs.com/jobsearch.asp?fcatId=8',
    bunny = request.jar();
    bunny.setCookie(request.cookie('JOBSRPP=40'), url);   //set 40 results per page

    var options = {
        url: url,
        headers: {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'
        },
        jar: bunny
    };

    var urls = [];
    var keywords = ['python', 'nodejs', 'node', 'laravel', 'django', 'node.js'];

    request(options).then(function(html) {
        $ = cheerio.load(html);
        var res = $('.job_title_text a').get();
        //console.log(res);
        res.map(function(x) {
            var option = {
                url: 'http://joblist.bdjobs.com/' + x['attribs']['href'],
                jar: bunny
            };
            request(option).then(function (body) {
                $ = cheerio.load(body);
                var text = $('.comp_wrapper').text();
                //console.log(text);

                keywords.map(function (key) {
                    if(text.match(/key/ig)) {
                        urls[key] = 'http://joblist.bdjobs.com/' + x['attribs']['href'];
                        console.log(key + ' ' + 'http://joblist.bdjobs.com/' + x['attribs']['href']);
                    }
                })
            }).catch(function (err) {
                console.log(err);
            })
        })
    }).catch(function (err) {
        console.log(err);
    }).finally(function () {
        //console.log(urls);
    });

    console.log(urls);
}

x();