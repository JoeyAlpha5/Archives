function logout(){
    document.location = '/logout/';
}

function displayPapers(data){
    var content = data.data;
    for (var x =0; x < content.length; x++){
        var subject = content[x].subject;
        var date = content[x].date;
        var file = content[x].file;
        $("#table").append("<tr> <th scope='row'>"+x+"</th><td>"+subject+"</td><td>"+date+"</td>  <td onclick='download("+JSON.stringify(file)+")'  class='download' id="+file+">Download</td></tr>");
    }
}



function displayVideos(videos){
    for (var x =0; x < videos.length; x++){
        var subject = videos[x].subject;
        var description = videos[x].description;
        var link = videos[x].link;
      $("#rightPane").append("<div class='card' style='width: 18rem;'><iframe frameborder='0' src="+link+" allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture'></iframe><div class='card-body'><h5 class='card-title'>"+subject+"</h5><p class='card-text'>"+description+"</p>");
    }
}

function displayAnnouncements(data){
    for (var x =0; x < data.length; x++){
        var ann = data[x].announcement;
        var date = data[x].date;
      $("#rightPane").append("<div id='card' class='card' style='width: 18rem;'><div class='card-header'>"+date+"</div> <div class='card-body'><h5 class='card-title'>"+ann+"</h5>");
    }
}



function download(file){
    window.open('https://res.cloudinary.com/uploaded/raw/upload/'+file+'.pdf', '_blank');
}