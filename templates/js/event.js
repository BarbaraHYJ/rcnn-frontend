function changeFileName(name) {
	$('#filename h1 span').html(name);
}

var file;

jQuery(document).ready(function($) {
	// 事件绑定
	$('#input').click(function(event) {})
			   .change(function(event) {
			   		file = this.files[0];
			   		changeFileName(file.name);
			   });

	$('#datain').bind('click', function(event) {
		$('#input').trigger('click');
	});

	$('#datakmeans').bind('click', function(event) {
		var fr = new FileReader();
		fr.readAsText(file);
		fr.onload = function(e) {
			let datas = fr.result;
			
		} 
	});

	$('#dataout').bind('click', function(event) {
		
	});

});

