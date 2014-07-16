// create a content table on top
function updateContent(){
    $(function (){
        $('h1').each(function (i,n){
                               
            // set ids for heading tags
            var headingId = 'headingid'+i;
            $(n).prop('id',headingId);

            // create a link for the content table
            var headingText = $(n).html();
            var linkObj = $('<a/>')
                        .html(headingText)
                        .attr({
                            'href':'#'+headingId,
                            'class':'content',
                        });
            linkObj = linkObj.append('</br>');
            
            // create a content table entry
            $('#contentNav').append(
                linkObj
            );
        })
    })
}

function loadIframes(id, src){
        
    var slugs = ['rapid-prototyping-with-js','ohmyjs']; 
    var index = Math.round(Math.random()); 
    
    jQuery('#' + id).html(
        '<iframe frameBorder="0" scrolling="auto" width="40%" height="200px" src="'
		+ src 
		+ '"><font face="Arial, Helvetica, sans-serif" size="1">Sorry your browser does not support IFRAMES.</font></iframe>'
    );
}

