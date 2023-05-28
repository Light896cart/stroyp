$('.repair_house').click(function() {
    $('.house_price').css({
        'top':'10%',
        'display': 'block',
        'transition':' top .3s ease'
        });
    $('body').css({
        'overflow':'hidden'
        });
    $('.all_content').css({
        'background':'black'
        });
    $('.mini_all_content').css({
        'opacity':'0.6'
        });
    });
$('.repair_office').click(function() {
    $('.office_price').css({
        'display': 'block'
        });
    $('body').css({
        'overflow':'hidden'
        });
    $('.all_content').css({
        'background':'black'
        });
    $('.mini_all_content').css({
        'opacity':'0.6'
        });
    });
$('.close_price').click(function() {
    $('.house_price').css('display','');
    $('.office_price').css('display','');
    $('body').css('overflow','');
    $('.all_content').css('background','');
    $('.mini_all_content').css('opacity','');
    });