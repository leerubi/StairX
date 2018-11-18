/*
***********************************************
* @description    : Front > 공통 JS
***********************************************
* DATE			AUTHOR		DESCRIPTION
* ---------------------------------------------
* 2017-08-00	남현철		최초작성
***********************************************
*/
$(function(){
	$( '.skip_navi a' ).each(function(){
		$(this).click(function(){
			var thishref = $(this).attr( 'href' );
			$(thishref).attr( 'tabindex','-1' );
			$(thishref).focus();
		});
	});

	/* top btn & scroll */

	var top_btn_html = '<a id="top_btn" href="#">위로</a>';
	$('body').append(top_btn_html);

	$('#top_btn').click(function(e){
		e.preventDefault();
		$( '#contents.main' ).animate({
			scrollTop:0
		}, 500, 'swing' ,function(){
			$('#top_btn').fadeOut();
		});
		return false;
	});

	$('#contents.main').scroll(function(){
		var _scrl = $('#contents.main').scrollTop();
		if( _scrl > 0 ){
			$('#top_btn').fadeIn();
		}else{
			$('#top_btn').fadeOut();
		}
	});
	
	hljs.initHighlightingOnLoad();
	
	subMenuAction();
});

function subMenuAction(){
		/* sub lnb */

		if($("#side_wrap").size() > 0){
			var $re_el = $("#side_wrap");
			
			//2017-09-08 nahosung add
			$("#tree_wrap").mCustomScrollbar({
				theme: "dark",
			       scrollButtons: {enable:true}
			});
			//2017-09-08 nahosung add
			
			$("#browser").treeview({
				animated:"fast",
				control:"#sidetreecontrol"
			});
			
			$re_el.resizable({
				handles: {w: $('#btn_resize')},
				maxWidth: $("body").width() / 2,
				grid: [1, 10000],
				minWidth: 187,
				resize: function(event, ui){
					var currentWidth = ui.size.width;
					$(this).width(currentWidth);
				}
			});

			$('#side_wrap #side_search .input_wrap input').on('keydown',function(e){
				if (!$('#side_wrap #search_result').hasClass('on')) {
					$('#side_wrap #search_result').toggleClass('on');
				}
				$('.dropdown_wrapper').removeClass('on');

			});

			$(document).on('click','.dropdown_wrapper .select_re', function(e){
				$('#side_wrap #search_result').removeClass('on');
				$('.dropdown_wrapper').toggleClass('on');
			});

			$(document).on('mouseenter','.dropdown_wrapper .dropdown_select a', function(e){
				$(this).closest('ul').find('li').removeClass('on');
				$(this).closest('li').addClass('on');
			});

			$('.dropdown_wrapper .dropdown_select').mousedown(function(e){
				var now_idx = $('.dropdown_wrapper .dropdown_select li.on').index();
				var re_txt = $('.dropdown_wrapper .dropdown_select li').eq(now_idx).text();
				$('.dropdown_wrapper .select_re').text(re_txt);
				$('.dropdown_wrapper').removeClass('on');
				
				$('.dropdown_wrapper .select_re').removeClass().addClass('select_re');

				switch (re_txt) {
					case 'Web':
						$('.dropdown_wrapper .select_re').addClass('web');
						break;
					case 'Android':
						$('.dropdown_wrapper .select_re').addClass('android');
						break;
					case 'iOS':
						$('.dropdown_wrapper .select_re').addClass('ios');
						break;
					case 'Web service':
						$('.dropdown_wrapper .select_re').addClass('webService');
						break;
				}
			});

			$(window).on('resize',function(){
				$('#side_wrap').height(window.innerHeight);
				$('#side_wrap #tree_wrap').height($('#side_wrap').height() - 243);
				$('#side_wrap #search_result').height($re_el.height() - 217);
				$('#contents').width($(window).width() - $('#side_wrap').width());
				$('#contents').height($('#side_wrap').height());
				$re_el.resizable({maxWidth: $("body").width() / 2});
			}).resize();
		}

};
