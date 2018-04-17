//Função responsável em carregar um formulário modal
$('#vincular_usuario_site').on('show.bs.modal', function(event) {
	var button = $(event.relatedTarget);
	var nome = button.data('nome_site');
	var url = button.data('url');
	var option = button.data('action')

	var modal = $(this);
	var form = modal.find('form');
	var action = form.attr('action');

	form.attr('action', url + '?action=' + option + '-usuario-site');
    modal.find('.modal-body span').html('');
    if (option=='desvincular'){
        modal.find('#btn-vincular-desvincular').html("Desvincular")
        modal.find('.modal-title').html('Desvincular usuários do site')
    }else{
        modal.find('#btn-vincular-desvincular').html("Vincular")
        modal.find('.modal-title').html('Vincular usuários do site')
    }
	get_form_vincular_usuario_site(url, option+'-usuario-site', modal);
});


function get_form_vincular_usuario_site(url, action, modal) {
        $.ajax({
        url: url,
        data: {
            'action': action
        },
        dataType: 'json',
        success: function (data) {
            modal.find('.modal-body p').html(data.result);
        }
    });
}