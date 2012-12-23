$(document).ready(function(){
    $.ajax({
        url: '/getSponsor',
        method: 'GET',
        success: function(res){
            var sponsorEl = $('#random_sponsor');
            var html = '<a href="' + res.url + '"><img style="width: 120px" src="' + res.logo + '"></a><br><br>';
            sponsorEl.append(html);
        }
    });

});

function getAllSponsors(){
    var sponsorEl = $('#all_sponsor');
    sponsorEl.append('<h3>Våre Sponsorer: </h3><br><br>');
    $.ajax({
        url: '/getAllSponsors',
        method: 'GET',
        success: function(res){
            for(var i = 0; i < res.length; i++){
                data = '<h4>' + res[i].navn + ':</h4><br><a href="' + res[i].url + '"><img class="sponsors" src="' + res[i].logo + '"></a><br><br>';
                sponsorEl.append(data);
            }
            console.log(res)
            //sponsorEl.append(html);
        }
    });
}