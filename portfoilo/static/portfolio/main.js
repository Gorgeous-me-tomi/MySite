$(document).ready(function(){


    // Scrolling automatically
    // window.scrollTo(0, 0);

    // $(".wrapperanimate").fadeOut();

    // getting battery

    // device_name = navigator.userAgent.toUpperCase().split(' ')[4]
    
    function battery_change(){
        navigator.getBattery().then(function(battery) {
            deviceBatteryLevel = Math.round(battery.level * 100)
            includedText = ` Just want to let you know your device battery is `

            chargingReview = ''

            if (deviceBatteryLevel >= 50){
                chargingReview = `${includedText} ${deviceBatteryLevel}% 😜.`
            }
            
            else{
                if (battery.charging == true){
                chargingReview = `${includedText} ${deviceBatteryLevel}% kind of low but i'm happy it's charging 😊`
                }
                
                else{
                chargingReview = `${includedText} ${deviceBatteryLevel}% kind of low and not currently charging. Please charge 😊`
                }
                
            }

            $('.battery-status-review').html(chargingReview)

            battery.onlevelchange = () => {
                battery_change()
            }
    
            battery.addEventListener('chargingchange', () => {
                battery_change()
            });

        });

        
    }


    battery_change()
    
    


    // bootstrap modal show
    $(".modal-1").modal('show');

    $(window).scroll(function(){ 

        if($(window).scrollTop() > 100){
            $(".navbar").css({"background-color": 'black', "margin-top":'0px'});
        }

        else{
            $(".navbar").css({"background-color":"transparent","margin-top":'20px'});
        } 
        
    })

    // dark mode and d other toggle
    $(".toggle-bg").click(function(){

        if($(".toggle-bg").hasClass("dark-mode")){
            $(".toggle-bg").removeClass("dark-mode");
            $("body").css({"background-color": "rgba(0, 0, 0, 0.9)"});
            $(".title-shadow").css({"color": "rgba(255, 255, 255, 0.5)"});
            $(".title-text").css({"color": "rgba(255, 255, 255, 0.9)"});
            $("#cover").css({"background": "linear-gradient(to top left,#0275d8, #555)"});
            $(".details .pag-contents").css({"color": "rgba(255, 255, 255, 0.9)"});
            $("#blog .blog-card .first-row .title").css({"color": "rgba(255, 255, 255, 0.7)"});
            $("#blog .blog-card .first-row .info span").css({"color": "rgba(255, 255, 255, 0.6)"});
            $("#blog .blog-card .second-row .content").css({"color": "rgba(255, 255, 255, 0.7)"});
            $(".contact-box .contact-form").css({"color": "rgba(255, 255, 255, 0.8)",'box-shadow': '2px 2px 10px rgba(255, 255, 255, 0.4)' });
            $(".contact-form form input, .contact-form form textarea").css({"color": "white"});
 

        }


        else if($(".toggle-bg").not("dark-mode")){
            $(".toggle-bg").addClass("dark-mode");
            $("body").css({"background-color": "white"});
            $(".title-shadow").css({"color": "rgba(0, 0, 0, 0.5)"});
            $(".title-text").css({"color": "inherit"});
            $("#cover").css({"background": "linear-gradient(to top left,#0275d8, #766dff)"});
            $(".details .pag-contents").css({"color": "#555"});
            $("#blog .blog-card .first-row .title").css({"color": "inherit"});
            $("#blog .blog-card .first-row .info span").css({"color": "rgba(0, 0, 0, 0.4)"});
            $("#blog .blog-card .second-row .content").css({"color": "rgba(0, 0, 0, 0.7)"});
            $(".contact-box .contact-form").css({"color": "inherit",'box-shadow': '2px 2px 10px rgba(0, 0, 0, 0.4)'});
            $(".contact-form form input, .contact-form form textarea").css({"color": "black "});

        }

        
      
    });

})



function pagination(page){
    
    let pagContents = document.getElementsByClassName('pag-contents')
    for (let index = 0; index < pagContents.length; index++) {

        if (page == index) {
            pagContents[index].style.display='block'
        }

        else {
            pagContents[index].style.display='none'
        }

        
    }
}


function hide_show() {
    let toggleWhat = document.getElementsByClassName('toggle-view')[0]
    let whatToToggle = document.getElementsByClassName('toggle-row')[0]

    if (toggleWhat.innerText.toLowerCase() == 'show more') {
        whatToToggle.style.display='flex'
        toggleWhat.innerHTML = 'show less<i class="bi bi-box-arrow-in-right"></i>'

    }

    else {
        whatToToggle.style.display ='none'
        toggleWhat.innerHTML = 'show more<i class="bi bi-box-arrow-in-right"></i>'

    }

}


function copy(id){

    let link = document.getElementsByClassName('link-to-copy')[id-1].innerHTML;
    let icon = document.getElementsByClassName('clipboard')[id-1];
    
    navigator.clipboard.writeText(link);
    // alert('link copied')
    $('.copy-toast').toast('show');
    // icon.outerHTML = '<i class="bi bi-check-circle-fill clipboard copied"></i>'
    

}


// Online Offline Dectector
window.addEventListener('online',  onlineStatus);
window.addEventListener('offline',  onlineStatus);

function onlineStatus(){
    var elem = $('.form-submit')

    if(navigator.onLine == false){
        elem.attr('value', 'You are currently offline');
        elem.attr('disabled', '');
        elem.css({"cursor": "not-allowed"})
    }

    else{
        elem.attr('value', 'Send Message');
        elem.removeAttr('disabled');
        elem.css({"cursor": "pointer"})
    }
}


function chosenService(obj){
    var textArea = document.getElementById('id_message')
    let service = obj.innerHTML
    let userText = textArea.value
    textArea.value = `I Want Your ${service} Service\n ${userText}`
}

// Get Location
// function getCountryFlag(){
//     if(navigator.geolocation) {
//         navigator.geolocation.getCurrentPosition(async function(position) {
//             var latitude = position.coords.latitude;
//             var longitude = position.coords.longitude;
//             var api_key = 'b58011e327d54433852230eba9dc0890'
            
//             const api_url = `https://www.latlong.net/c/?lat=0.000000&long=0.000000`
//             const response = await fetch(api_url);
//             // const data = response.json();
//             console.log(response)
//             // alert('yup')
//         });

//     }

//     else{
//         alert('nope')
//     }
// }

// getCountryFlag()

// Reloding Iframe

// function reloadIframe(num){
//     // alert(num)
//     document.getElementsByClassName('iframeclass')[num-1].src = document.getElementsByClassName('iframeclass')[num-1].src
// }


// setInterval(function () {


// },1000);
